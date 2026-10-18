import asyncio
import json
import logging
import os
import time
from typing import Any, Dict, Optional

from .player_abstract import GamePlayer


class AgentSeat(GamePlayer):
    """A live seat driven through the file bridge (the MiMo duel seat).

    Neither AIPlayer nor NetworkPlayer: the engine sends it the same offers a
    human client receives and waits for `receive_player_action` replies, so the
    seat answers every prompt kind (turn actions, browsers, buttons, prizes,
    coin flip, placement, mulligan) through the bridge. Outbound packets are
    appended to the bridge outbox JSONL; reply lines placed in the inbox JSONL
    are forwarded to the session. The engine enforces reply legality
    (compute_legal_actions + _parse_action_reply) before anything reaches the
    rules.
    """

    def __init__(
        self,
        account_id: str,
        username: str,
        deck_data: Dict[str, Any],
        session: Any,
        bridge_dir: str,
    ):
        super().__init__(account_id=account_id, username=username, deck_data=deck_data)
        self.session = session
        self.bridge_dir = bridge_dir
        self.outbox_path = os.path.join(bridge_dir, f"outbox-{account_id}.jsonl")
        self.inbox_path = os.path.join(bridge_dir, f"inbox-{account_id}.jsonl")
        self._inbox_offset = 0
        self._bridge_task: Optional[asyncio.Task] = None
        try:
            os.makedirs(bridge_dir, exist_ok=True)
        except OSError as e:
            logging.error(f"[AgentSeat {account_id}] Bridge dir unavailable ({bridge_dir}): {e}")

    async def send_packet(self, name: str, value: Dict[str, Any], flags: int = 0):
        self._append_line(self.outbox_path, {
            "ts": time.time(),
            "game_id": getattr(self.session, "game_id", None),
            "player_id": self.account_id,
            "name": name,
            "value": value,
        })
        self._ensure_bridge_task()

    async def prompt_selection(self, prompt_packet: Dict[str, Any]):
        # Never called by the engine (prompt_selection_message talks to the
        # seat directly via send_packet / pending_choice_future).
        pass

    def _ensure_bridge_task(self):
        if self._bridge_task is not None and not self._bridge_task.done():
            return
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            return
        self._bridge_task = loop.create_task(self._inbox_loop())

    async def _inbox_loop(self):
        while True:
            try:
                await self._drain_inbox()
            except asyncio.CancelledError:
                raise
            except Exception as e:
                logging.error(f"[AgentSeat {self.account_id}] Inbox drain failed: {e}")
            await asyncio.sleep(0.5)

    async def _drain_inbox(self):
        """Reads new reply lines and forwards them to the session."""
        if not os.path.exists(self.inbox_path):
            return
        with open(self.inbox_path, "r", encoding="utf-8") as f:
            f.seek(self._inbox_offset)
            chunk = f.read()
            self._inbox_offset = f.tell()
        for line in chunk.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                reply = json.loads(line)
            except json.JSONDecodeError:
                logging.warning(
                    f"[AgentSeat {self.account_id}] Skipping unparseable inbox line: {line[:200]}"
                )
                continue
            if not isinstance(reply, dict) or "selection" not in reply:
                logging.warning(
                    f"[AgentSeat {self.account_id}] Inbox line missing 'selection': {line[:200]}"
                )
                continue
            action = {
                "selection": reply.get("selection"),
                "counter": reply.get("counter"),
            }
            await self.session.receive_player_action(self.account_id, action)

    @staticmethod
    def _append_line(path: str, obj: Dict[str, Any]):
        try:
            with open(path, "a", encoding="utf-8") as f:
                f.write(json.dumps(obj, default=str) + "\n")
        except OSError as e:
            logging.error(f"[AgentSeat] Failed appending to {path}: {e}")


def bridge_is_fresh(bridge_dir: str, max_age_seconds: float) -> bool:
    """True when the bridge heartbeat file exists and is within max_age."""
    path = os.path.join(bridge_dir, "heartbeat.json")
    try:
        return (time.time() - os.path.getmtime(path)) <= max_age_seconds
    except OSError:
        return False


def write_heartbeat(bridge_dir: str):
    """Writes/refreshes the bridge heartbeat (called by the MiMo CLI serve loop)."""
    os.makedirs(bridge_dir, exist_ok=True)
    path = os.path.join(bridge_dir, "heartbeat.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"ts": time.time()}, f)
