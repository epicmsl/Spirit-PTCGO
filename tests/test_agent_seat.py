import asyncio
import json
import os
import tempfile
import unittest
from types import SimpleNamespace
from unittest import mock

from spirit.game.session.agent_seat import (
    AgentSeat,
    bridge_is_fresh,
    write_heartbeat,
)
from spirit.game.session.constants import GamePhase
from spirit.game.session.game_session import GameSession
from spirit.network.message_names import OutboundMsg


class _StubSession:
    def __init__(self):
        self.game_id = "game-1"
        self.actions = []

    async def receive_player_action(self, account_id, action_data, client_handler=None):
        self.actions.append((account_id, action_data))


def _make_seat(bridge_dir, session=None):
    session = session or _StubSession()
    seat = AgentSeat(
        account_id="agent-1",
        username="MiMo",
        deck_data={},
        session=session,
        bridge_dir=bridge_dir,
    )
    return seat, session


class AgentSeatBridgeTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.bridge = self._tmp.name
        self.addCleanup(self._tmp.cleanup)

    async def _cleanup_seat(self, seat):
        task = seat._bridge_task
        if task is not None and not task.done():
            task.cancel()
            await asyncio.gather(task, return_exceptions=True)

    async def test_send_packet_appends_to_outbox(self):
        seat, _ = _make_seat(self.bridge)
        self.addAsyncCleanup(self._cleanup_seat, seat)

        await seat.send_packet("SomeMessage", {"foo": 1})

        with open(seat.outbox_path, "r", encoding="utf-8") as f:
            rows = [json.loads(line) for line in f if line.strip()]
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["name"], "SomeMessage")
        self.assertEqual(rows[0]["value"], {"foo": 1})
        self.assertEqual(rows[0]["player_id"], "agent-1")
        self.assertEqual(rows[0]["game_id"], "game-1")

    async def test_inbox_reply_forwards_to_session_once(self):
        seat, session = _make_seat(self.bridge)
        self.addAsyncCleanup(self._cleanup_seat, seat)

        with open(seat.inbox_path, "w", encoding="utf-8") as f:
            f.write(json.dumps({"counter": 7, "selection": [[12, 3]]}) + "\n")

        await seat._drain_inbox()
        self.assertEqual(
            session.actions,
            [("agent-1", {"selection": [[12, 3]], "counter": 7})],
        )

        # A second drain must not re-deliver consumed lines (offset tracking).
        await seat._drain_inbox()
        self.assertEqual(len(session.actions), 1)

    async def test_inbox_skips_malformed_lines(self):
        seat, session = _make_seat(self.bridge)
        self.addAsyncCleanup(self._cleanup_seat, seat)

        with open(seat.inbox_path, "w", encoding="utf-8") as f:
            f.write("not-json\n")
            f.write(json.dumps({"counter": 1}) + "\n")  # missing selection
            f.write(json.dumps({"counter": 2, "selection": None}) + "\n")

        await seat._drain_inbox()
        self.assertEqual(session.actions, [("agent-1", {"selection": None, "counter": 2})])

    async def test_heartbeat_freshness(self):
        self.assertFalse(bridge_is_fresh(self.bridge, 30.0))
        write_heartbeat(self.bridge)
        self.assertTrue(bridge_is_fresh(self.bridge, 30.0))
        self.assertFalse(bridge_is_fresh(self.bridge, -1.0))


class AgentSeatSessionTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.bridge = self._tmp.name
        self.addCleanup(self._tmp.cleanup)
        patcher = mock.patch(
            "spirit.game.session.game_session.config.MIMO_BRIDGE_DIR", self.bridge
        )
        patcher.start()
        self.addCleanup(patcher.stop)

    def make_session(self):
        session = object.__new__(GameSession)
        session.game_id = "game-1"
        session.game_phase = GamePhase.TURN_LOOP
        session._connection_resumed = asyncio.Event()
        session._connection_resumed.set()
        session._connection_pause_event = asyncio.Event()
        session._disconnected = set()
        session._reconnecting = set()
        session._offers_to_restore = set()
        session._restoring_offers = set()
        session._wire_lock = asyncio.Lock()
        session._state_checkpoint = asyncio.Event()
        session._state_checkpoint.set()
        session._state_unit_tasks = {}
        session._prompt_checkpoint_tasks = set()
        session.choreography_pauses = False
        session.players = {}
        return session

    async def wait_for(self, predicate, timeout=1.0):
        async def loop():
            while not predicate():
                await asyncio.sleep(0.01)

        await asyncio.wait_for(loop(), timeout=timeout)

    def test_seat_factory_honors_agent_flag(self):
        session = self.make_session()
        session.pairing = {
            "players": {
                "seat-1": {
                    "client": None,
                    "deck": {"deckName": "Test"},
                    "ready": True,
                    "agent": True,
                }
            }
        }
        session._initialize_players()

        seat = session.players["seat-1"]
        self.assertIsInstance(seat, AgentSeat)
        self.assertEqual(seat.username, "MiMo")
        self.assertEqual(seat.deck_data, {"deckName": "Test"})

    def test_seat_factory_still_builds_ai_without_flag(self):
        session = self.make_session()
        session.pairing = {
            "players": {
                "bot-1": {"client": None, "deck": {}, "ready": True}
            }
        }
        session._initialize_players()

        from spirit.game.session.ai_player import AIPlayer

        self.assertIsInstance(session.players["bot-1"], AIPlayer)

    async def test_bridge_reply_resolves_prompt(self):
        session = self.make_session()
        seat, _ = _make_seat(self.bridge, session=session)
        session.players["agent-1"] = seat

        prompt = asyncio.create_task(
            session.prompt_selection_message(
                seat,
                OutboundMsg.SELECTION_WITH_TARGETS_AND_ACTIONS_REQUIRED.value,
                {"counter": 7},
                expected_counter=7,
            )
        )
        await self.wait_for(lambda: os.path.exists(seat.outbox_path)
                            and os.path.getsize(seat.outbox_path) > 0)

        with open(seat.inbox_path, "w", encoding="utf-8") as f:
            f.write(json.dumps({"counter": 7, "selection": None}) + "\n")
        await seat._drain_inbox()

        reply = await asyncio.wait_for(prompt, timeout=1)
        self.assertEqual(reply, {"selection": None, "counter": 7})
        task = seat._bridge_task
        if task is not None and not task.done():
            task.cancel()
            await asyncio.gather(task, return_exceptions=True)

    async def test_watchdog_timeout_returns_null_selection(self):
        session = self.make_session()
        seat, _ = _make_seat(self.bridge, session=session)
        session.players["agent-1"] = seat

        with mock.patch(
            "spirit.game.session.game_session.config.MIMO_PROMPT_TIMEOUT_SECONDS",
            0.05,
        ):
            reply = await session.prompt_selection_message(
                seat,
                OutboundMsg.SELECTION_WITH_TARGETS_AND_ACTIONS_REQUIRED.value,
                {"counter": 9},
                expected_counter=9,
            )

        self.assertTrue(reply["_timed_out"])
        self.assertIsNone(reply["selection"])
        self.assertEqual(reply["counter"], 9)
        # AgentSeat is untimed on the wire: no idle-timer packets, no force.
        self.assertEqual(
            [name for name, _, _ in self._seat_outbox(seat)],
            [OutboundMsg.SEQUENCE_MESSAGE.value],
        )
        self.assertIsNone(seat.pending_choice_future)
        self.assertIsNone(seat._pending_offer)
        task = seat._bridge_task
        if task is not None and not task.done():
            task.cancel()
            await asyncio.gather(task, return_exceptions=True)

    def _seat_outbox(self, seat):
        # send_packet appends to the JSONL; reconstruct the (name, value, flags)
        # tuples for packet-shape assertions.
        rows = []
        with open(seat.outbox_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    row = json.loads(line)
                    rows.append((row["name"], row["value"], 0))
        return rows


if __name__ == "__main__":
    unittest.main()
