"""Headless live AgentSeat duel harness.

Boots the matchmaking stack in-process (no TCP sockets), enqueues a fake
human client into a solo queue, lets the MiMo fill watchdog seat an
AgentSeat opponent once the duel-bridge heartbeat is fresh, then auto-drives
BOTH sides of the duel:

  * the human NetworkPlayer is driven by capturing the packets the fake
    client receives and answering via GameSession.receive_player_action;
  * the AgentSeat is driven through the real file bridge (outbox tail ->
    policy -> inbox reply lines), exactly like tools/mimo_duel_cli.py.

The run ends when the game completes (GameCompletedMessage / game_result),
on --timeout, or after --max-replies policy replies, and always tears the
seat bridge task down so nothing leaks.

Usage (from the repo root):
    .\\venv\\Scripts\\python.exe tools\\live_agent_duel.py
    .\\venv\\Scripts\\python.exe tools\\live_agent_duel.py --deck "Charizard VSTAR" --timeout 240
    .\\venv\\Scripts\\python.exe tools\\live_agent_duel.py --concede-after 25
"""

import argparse
import asyncio
import json
import logging
import os
import sys
import time

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from spirit import config  # noqa: E402
from spirit.game.content.bot_decks import BOT_DECK_LISTS  # noqa: E402
from spirit.game.content.starter import build_deck_data  # noqa: E402
from spirit.game.session import game_session as gs_mod  # noqa: E402,F401
from spirit.game.session.agent_seat import AgentSeat, write_heartbeat  # noqa: E402
from spirit.game.session.constants import (  # noqa: E402
    TARGET_TYPE_ACTIVE,
    TARGET_TYPE_BENCH,
)
from spirit.game.session.game_session import GameSession  # noqa: E402,F401
from spirit.game.session.legal_actions import (  # noqa: E402
    ACTION_ATTACH_TOOL,
    ACTION_EVOLVE,
    ACTION_PLAY_ENERGY,
    ACTION_PLAY_POKEMON,
    ACTION_PLAY_STADIUM,
    ACTION_USE_ABILITY,
    ACTION_USE_ATTACK,
    ACTION_USE_TRAINER,
)
from spirit.game.session.manager import GameSessionManager  # noqa: E402

# Offer message names worth reacting to (mirrors tools/mimo_duel_cli.py).
OFFER_NAMES = {
    "SelectionWithTargetsAndActionsRequired",
    "SelectionWithTargetsRequired",
    "SelectionRevealArea",
    "CustomChoiceRequired",
    "CoinFlipChoiceRequired",
    "GoFirstChoiceRequired",
    "MulliganChoiceRequired",
}

# Same greedy order the stock AI turn uses (game_session.AI_ACTION_PRIORITY),
# minus retreat (a passed turn is a safer last resort for the harness).
AGENT_ACTION_PRIORITY = (
    ACTION_PLAY_POKEMON,
    ACTION_PLAY_ENERGY,
    ACTION_EVOLVE,
    ACTION_USE_TRAINER,
    ACTION_PLAY_STADIUM,
    ACTION_ATTACH_TOOL,
    ACTION_USE_ABILITY,
    ACTION_USE_ATTACK,
)


# ---------------------------------------------------------------------------
# Fake server / client (the surface add_to_queue + NetworkPlayer touch)
# ---------------------------------------------------------------------------

class FakeServer:
    def __init__(self):
        self.clients_by_account = {}


class FakeClient:
    """Stands in for ClientHandler: queue membership, sends, offer capture."""

    def __init__(self, player_profile, server):
        self.player = player_profile
        self.server = server
        self.addr = ("harness", 0)
        self.running = True
        self.sent = []                       # every packet dict, in order
        self.offer_queue = asyncio.Queue()   # offer-shaped SequenceMessages

    async def send_packet(self, packet, request_id=0, flags=0):
        if not isinstance(packet, dict):
            return
        self.sent.append(packet)
        inner_name, inner_value = _offer_inner(packet)
        if inner_name in OFFER_NAMES:
            await self.offer_queue.put((inner_name, inner_value))

    async def send_packets(self, packets):
        for packet, _request_id, _flags in packets:
            await self.send_packet(packet)
        return True

    async def flush_outbound(self):
        return True


def _offer_inner(packet):
    """(inner_name, inner_value) when a packet wraps a nested offer message.

    Handles both wire shapes:
      * FakeClient packets from NetworkPlayer.send_packet:
        {sequenceID, gameID, msg: {...}, messageName: "SequenceMessage"}
      * AgentSeat outbox lines:
        {ts, game_id, player_id, name: "SequenceMessage", value: {msg: {...}}}
    """
    name = packet.get("messageName") or packet.get("name")
    if name != "SequenceMessage":
        return None, None
    msg = packet.get("msg")
    if not isinstance(msg, dict):
        value = packet.get("value")
        if isinstance(value, dict):
            msg = value.get("msg")
    if not isinstance(msg, dict):
        return None, None
    inner_name = msg.get("name")
    inner = msg.get("value")
    return inner_name, inner if isinstance(inner, dict) else None


# ---------------------------------------------------------------------------
# Shared reply policy (both seats)
# ---------------------------------------------------------------------------

class SeatState:
    """Per-seat policy bookkeeping."""

    def __init__(self):
        self.replies = 0
        self.benches_placed = 0
        self.attempted = set()   # (entityID, actionID) tried this turn


HARNESS_STATE = {"max_bench": 2, "reply_cap_hit": False}


def _harvest_pick(value):
    """Builds a targetResponses reply from whatever validTargets the offer
    declares (prize fans, composite-reveal browsers, single-node picks)."""
    picked = []
    target_map = value.get("targetMap")
    nodes = []
    if isinstance(target_map, dict):
        for entry in target_map.values():
            if isinstance(entry, list):
                nodes.extend(entry)
    elif isinstance(target_map, list):
        nodes.extend(entry for entry in target_map if isinstance(entry, dict))
    for node in nodes:
        valid = [t for t in (node.get("validTargets") or []) if isinstance(t, str)]
        if not valid:
            for sel in node.get("selections") or []:
                if isinstance(sel, dict):
                    valid = [t for t in (sel.get("validTargets") or []) if isinstance(t, str)]
                    if valid:
                        break
        if not valid:
            for info in node.get("targetInfoLst") or []:
                if isinstance(info, dict):
                    valid = [t for t in (info.get("validTargets") or []) if isinstance(t, str)]
                    if valid:
                        break
        want = node.get("numberToSelect") or 1
        try:
            want = max(1, int(want))
        except (TypeError, ValueError):
            want = 1
        picked.extend(valid[:want])
    if not picked:
        return None
    return {"targetResponses": [{"entityList": picked}]}


def _agent_main_action(value, state):
    """Picks the highest-priority legal action the seat hasn't tried this turn."""
    target_map = value.get("targetMap") or []
    by_action = {}
    for entry in target_map:
        if not isinstance(entry, dict):
            continue
        action = entry.get("selectableAction") or {}
        key = (entry.get("entityID"), action.get("actionID"))
        if key in state.attempted:
            continue
        by_action.setdefault(action.get("description"), []).append(entry)
    for description in AGENT_ACTION_PRIORITY:
        for entry in by_action.get(description, []):
            targets = []
            for info in entry.get("targetInfoLst") or []:
                valid = [t for t in (info.get("validTargets") or []) if isinstance(t, str)]
                want = info.get("numberToSelect") or 1
                try:
                    want = max(1, int(want))
                except (TypeError, ValueError):
                    want = 1
                targets.extend(valid[:want])
            state.attempted.add((entry.get("entityID"),
                                 (entry.get("selectableAction") or {}).get("actionID")))
            return [[entry["entityID"],
                     entry["selectableAction"]["actionID"]],
                    [{"entityList": targets}]]
    return None  # nothing left to do: end the turn


def plan_reply(offer_name, value, state, is_agent, max_bench):
    """Returns the 'selection' payload for one offer (counter travels along)."""
    if offer_name in ("CoinFlipChoiceRequired", "GoFirstChoiceRequired"):
        return 0  # call Heads; winner chooses to go first
    if offer_name == "CustomChoiceRequired":
        return 0  # first button (Yes / accept)
    if offer_name == "MulliganChoiceRequired":
        return None
    if offer_name == "SelectionWithTargetsAndActionsRequired":
        if is_agent:
            return _agent_main_action(value, state)
        return None  # passive human: always end the turn
    if offer_name in ("SelectionWithTargetsRequired", "SelectionRevealArea"):
        target_type = value.get("targetType")
        target_map = value.get("targetMap")
        if target_type == TARGET_TYPE_BENCH and isinstance(target_map, dict):
            if target_map and state.benches_placed < max_bench:
                state.benches_placed += 1
                return {"entityID": next(iter(target_map))}
            return None  # done benching
        if target_type == TARGET_TYPE_ACTIVE and isinstance(target_map, dict):
            # Active placement / promote-after-KO: pick the first offered card.
            return {"entityID": next(iter(target_map))} if target_map else None
        return _harvest_pick(value)
    return None


# ---------------------------------------------------------------------------
# Seat drivers
# ---------------------------------------------------------------------------

async def drive_human(session, human_id, client, state, stop, max_replies, log):
    """Consumes captured offer packets and replies through the session."""
    while not stop.is_set():
        try:
            offer_name, value = await asyncio.wait_for(client.offer_queue.get(), 0.25)
        except asyncio.TimeoutError:
            if session.gameplay_task is not None and session.gameplay_task.done():
                return
            continue
        counter = (value or {}).get("counter")
        selection = plan_reply(offer_name, value or {}, state, is_agent=False,
                               max_bench=HARNESS_STATE["max_bench"])
        state.replies += 1
        log.info("[human] %s counter=%s -> %s", offer_name, counter,
                 json.dumps(selection, default=str)[:160])
        await session.receive_player_action(
            human_id, {"selection": selection, "counter": counter})
        if state.replies >= max_replies:
            HARNESS_STATE["reply_cap_hit"] = True
            stop.set()
            return
        await asyncio.sleep(0.02)


async def drive_agent(session, seat, state, stop, max_replies, log):
    """Tails the seat outbox and writes inbox replies (the real bridge)."""
    outbox = seat.outbox_path
    inbox = seat.inbox_path
    offset = 0
    # The outbox appears on the seat's first send_packet (MatchFound).
    while not stop.is_set() and not os.path.exists(outbox):
        if session.gameplay_task is not None and session.gameplay_task.done():
            return
        await asyncio.sleep(0.05)
    while not stop.is_set():
        try:
            with open(outbox, "r", encoding="utf-8") as f:
                f.seek(offset)
                chunk = f.read()
                offset = f.tell()
        except OSError:
            await asyncio.sleep(0.1)
            continue
        for line in chunk.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                packet = json.loads(line)
            except json.JSONDecodeError:
                continue
            inner_name, inner_value = _offer_inner(packet)
            if inner_name == "ActivePlayerSet":
                state.attempted.clear()  # new turn: allow every action again
            if inner_name not in OFFER_NAMES:
                continue
            counter = (inner_value or {}).get("counter")
            selection = plan_reply(inner_name, inner_value or {}, state,
                                   is_agent=True,
                                   max_bench=HARNESS_STATE["max_bench"])
            state.replies += 1
            log.info("[agent ] %s counter=%s -> %s", inner_name, counter,
                     json.dumps(selection, default=str)[:160])
            with open(inbox, "a", encoding="utf-8") as out:
                out.write(json.dumps({"counter": counter, "selection": selection},
                                     default=str) + "\n")
            if state.replies >= max_replies:
                HARNESS_STATE["reply_cap_hit"] = True
                stop.set()
                return
        if session.gameplay_task is not None and session.gameplay_task.done():
            return
        await asyncio.sleep(0.1)


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------

async def wait_for_session(manager, human_id, timeout):
    deadline = time.time() + timeout
    while time.time() < deadline:
        session = manager.get_session_by_player_id(human_id)
        if session is not None and any(
                isinstance(p, AgentSeat) for p in session.players.values()):
            return session
        await asyncio.sleep(0.1)
    return None


async def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--queue", default="Standard",
                        help="matchmaking queue name (default: Standard)")
    parser.add_argument("--deck", default="Charizard VSTAR",
                        choices=sorted(BOT_DECK_LISTS),
                        help="deck the fake human plays")
    parser.add_argument("--account", default="mimo_harness",
                        help="DB account username (created if missing)")
    parser.add_argument("--bridge", default=None,
                        help="bridge dir (default: duel_bridge/harness_<ts>)")
    parser.add_argument("--timeout", type=float, default=300.0,
                        help="wall-clock seconds before the run is aborted")
    parser.add_argument("--max-replies", type=int, default=600,
                        help="total policy replies before forcing a concede")
    parser.add_argument("--max-bench", type=int, default=2,
                        help="benches each seat places during setup")
    parser.add_argument("--concede-after", type=int, default=0,
                        help="concede once the human has replied this many times (0=off)")
    parser.add_argument("--keep-account", action="store_true",
                        help="do not create the DB account if missing")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO, format="%(message)s", stream=sys.stdout, force=True)
    log = logging.getLogger("live_agent_duel")
    HARNESS_STATE["max_bench"] = args.max_bench

    bridge = args.bridge or os.path.join(
        config.MIMO_BRIDGE_DIR, f"harness_{time.strftime('%Y%m%d_%H%M%S')}")
    os.makedirs(bridge, exist_ok=True)
    # Point every bridge consumer (fill watchdog, AgentSeat factory) at the
    # per-run dir so stale players from earlier runs can never be discovered.
    config.MIMO_BRIDGE_DIR = bridge
    log.info("bridge dir: %s", bridge)

    # --- database (same boot steps as spirit/main.py) ---
    from spirit.database import Base, engine
    from spirit.database.accounts import create_account, get_account_by_username
    from spirit.database.migrations import run_light_migrations
    Base.metadata.create_all(engine)
    try:
        run_light_migrations()
    except Exception as exc:  # non-fatal: migrations are idempotent add-ons
        log.warning("run_light_migrations failed (continuing): %s", exc)

    account = get_account_by_username(args.account)
    if account is None:
        if args.keep_account:
            log.error("account %r missing and --keep-account set", args.account)
            return 2
        log.info("creating DB account %r", args.account)
        account = create_account(args.account, "harness")
        if account is None:
            log.error("failed to create account %r", args.account)
            return 2

    from spirit.game.models.player import Player
    profile = Player(account)
    human_id = profile.account_id
    log.info("human account: %s (%s)", profile.username, human_id)

    deck_data = build_deck_data(args.deck, BOT_DECK_LISTS[args.deck])
    log.info("human deck: %s (%d cards)", args.deck,
             len(deck_data.get("piles", {}).get("deck", [])))

    # --- heartbeat must be fresh before the 7s fill check ---
    write_heartbeat(bridge)
    stop_heartbeat = asyncio.Event()

    async def heartbeat_loop():
        while not stop_heartbeat.is_set():
            write_heartbeat(bridge)
            try:
                await asyncio.wait_for(stop_heartbeat.wait(), timeout=5.0)
            except asyncio.TimeoutError:
                pass

    heartbeat_task = asyncio.create_task(heartbeat_loop())

    server = FakeServer()
    client = FakeClient(profile, server)
    server.clients_by_account[human_id] = client

    manager = GameSessionManager()
    stop = asyncio.Event()
    driver_tasks = []
    seat = None
    session = None
    exit_code = 1
    started = time.time()
    try:
        log.info("enqueuing into '%s' (agent fill at %gs, AI fallback at %gs)...",
                 args.queue, config.MIMO_FILL_SECONDS, config.AI_MATCH_TIMEOUT)
        await manager.add_to_queue(client, args.queue, deck_data, {}, 0)

        session = await wait_for_session(
            manager, human_id, config.MIMO_FILL_SECONDS + config.AI_MATCH_TIMEOUT + 15)
        if session is None:
            log.error("no AgentSeat session appeared (fill fell through to the "
                      "AI bot or the queue never paired); aborting")
            return 2
        session.choreography_pauses = False
        seat = next(p for p in session.players.values() if isinstance(p, AgentSeat))
        log.info("session %s seated; agent seat %s (outbox %s)",
                 session.game_id, seat.account_id, seat.outbox_path)

        human_state = SeatState()
        agent_state = SeatState()
        driver_tasks = [
            asyncio.create_task(drive_human(
                session, human_id, client, human_state, stop, args.max_replies, log)),
            asyncio.create_task(drive_agent(
                session, seat, agent_state, stop, args.max_replies, log)),
        ]

        # Kick the initial dispatch: only NetworkPlayers gate gameplay start.
        await session.mark_player_ready(human_id, client_handler=client)
        deadline = started + args.timeout
        while time.time() < deadline:
            if session.game_result is not None:
                break
            if session.gameplay_task is not None and session.gameplay_task.done():
                break
            if HARNESS_STATE["reply_cap_hit"]:
                break
            if args.concede_after and human_state.replies >= args.concede_after:
                log.info("conceding at human reply #%d (--concede-after)",
                         human_state.replies)
                await session.concede(human_id)
                break
            await asyncio.sleep(0.2)

        if session.game_result is None and not HARNESS_STATE["reply_cap_hit"]:
            if time.time() >= deadline:
                log.error("timeout after %.0fs with no result; conceding to exit",
                          args.timeout)
            await session.concede(human_id)

        # Wait briefly for the gameplay task to unwind (end_game -> GameOver).
        if session.gameplay_task is not None:
            try:
                await asyncio.wait_for(asyncio.shield(session.gameplay_task), 20)
            except (asyncio.TimeoutError, asyncio.CancelledError, Exception):
                pass

        result = session.game_result or {}
        log.info("=" * 60)
        log.info("RESULT: winner=%s reason=%r turns=%s", result.get("winner"),
                 result.get("reason"), session.turn_state.turn_number)
        log.info("human replies: %d | agent replies: %d | elapsed: %.1fs",
                 human_state.replies, agent_state.replies, time.time() - started)
        log.info("human packets captured: %d | agent outbox lines: %d",
                 len(client.sent), _count_lines(seat.outbox_path))
        exit_code = 0 if result else 2
    finally:
        stop.set()
        for task in driver_tasks:
            task.cancel()
        await asyncio.gather(*driver_tasks, return_exceptions=True)
        stop_heartbeat.set()
        heartbeat_task.cancel()
        await asyncio.gather(heartbeat_task, return_exceptions=True)
        # AgentSeat._bridge_task is NOT cancelled by session.cleanup() --
        # cancel it here or the inbox poller leaks past the harness run.
        if seat is not None and seat._bridge_task is not None \
                and not seat._bridge_task.done():
            seat._bridge_task.cancel()
            await asyncio.gather(seat._bridge_task, return_exceptions=True)
        if session is not None:
            try:
                await manager.remove_from_queue(client, send_left_packet=False)
            except Exception:
                pass
            try:
                manager.remove_session(session.game_id, log=False)
            except Exception:
                pass
        server.clients_by_account.clear()
    return exit_code


def _count_lines(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return sum(1 for line in f if line.strip())
    except OSError:
        return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
