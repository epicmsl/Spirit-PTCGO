"""MiMo Duel Seat bridge CLI.

Keeps the duel-bridge heartbeat alive (so matchmaking fills with the agent
seat instead of the stock bot) and lets the MiMo agent read offers / write
replies for a live duel.

Usage (from the repo root, alongside the server):

    python tools/mimo_duel_cli.py serve [--bridge DIR] [--beat SECONDS]
        Heartbeat loop + outbox tail. Ctrl+C stops; after the heartbeat goes
        stale the next queue fill falls through to the AI bot.

    python tools/mimo_duel_cli.py status [--bridge DIR]
        Heartbeat age and bridge files.

    python tools/mimo_duel_cli.py show [--bridge DIR] [--player ID] [--last N] [--full]
        Prints recent outbox packets. Default filters to prompt offers;
        --full prints every packet (board sync, animations included).

    python tools/mimo_duel_cli.py reply --player ID [--counter N] --selection JSON [--bridge DIR]
        Appends a reply line to the player's inbox. --selection is wire
        format JSON (see _parse_action_reply in game_session.py); the literal
        `null` ends the turn / passes a pick. --counter defaults to the
        counter of the latest offer in the outbox.

    python tools/mimo_duel_cli.py end-turn --player ID [--counter N] [--bridge DIR]
        Shorthand for `reply --selection null`.

    python tools/mimo_duel_cli.py set-deck [DECK.txt|PATH|default] [--bridge DIR]
        Pins the MiMo agent seat's deck for the next queue fill. DECK.txt is
        resolved against spirit/tools/Test Decks/ when not a real path;
        `default` (or no argument) clears the override so the seat falls back
        to SPIRIT_MIMO_AGENT_DECK_FILE / SPIRIT_MIMO_AGENT_DECK_DIR / the
        curated BOT_DECKS pool. Takes effect on the next pairing, no restart.
"""
import argparse
import glob
import json
import os
import sys
import time

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from spirit import config  # noqa: E402
from spirit.game.session.agent_seat import write_heartbeat  # noqa: E402

# Offer-shaped message names worth surfacing to the agent (everything else in
# the outbox is board sync / animation traffic).
OFFER_NAMES = {
    "SelectionWithTargetsAndActionsRequired",
    "SelectionWithTargetsRequired",
    "SelectionRevealArea",
    "CustomChoiceRequired",
    "CoinFlipChoiceRequired",
    "GoFirstChoiceRequired",
    "MulliganChoiceRequired",
}


def _bridge_dir(args) -> str:
    return args.bridge or config.MIMO_BRIDGE_DIR


def _read_jsonl(path):
    if not os.path.exists(path):
        return []
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                rows.append({"raw": line})
    return rows


def _offer_inner(packet):
    """Returns (inner_name, inner_value) when the packet carries an offer."""
    if packet.get("name") != "SequenceMessage":
        return None, None
    msg = (packet.get("value") or {}).get("msg") or {}
    return msg.get("name"), msg.get("value")


def _find_players(bridge):
    players = set()
    for path in glob.glob(os.path.join(bridge, "outbox-*.jsonl")):
        base = os.path.basename(path)
        players.add(base[len("outbox-"):-len(".jsonl")])
    return sorted(players)


def _latest_counter(bridge, player_id):
    rows = _read_jsonl(os.path.join(bridge, f"outbox-{player_id}.jsonl"))
    for packet in reversed(rows):
        inner_name, inner_value = _offer_inner(packet)
        if inner_name and isinstance(inner_value, dict) and "counter" in inner_value:
            return inner_value["counter"]
    return None


def cmd_serve(args):
    bridge = _bridge_dir(args)
    os.makedirs(bridge, exist_ok=True)
    print(f"[mimo-duel] serving heartbeat on {bridge} every {args.beat:g}s "
          f"(max age {config.MIMO_HEARTBEAT_MAX_AGE_SECONDS:g}s). Ctrl+C to stop.")
    offsets = {}
    try:
        while True:
            write_heartbeat(bridge)
            for path in glob.glob(os.path.join(bridge, "outbox-*.jsonl")):
                try:
                    size = os.path.getsize(path)
                except OSError:
                    continue
                offset = offsets.get(path, 0)
                if size <= offset:
                    continue
                with open(path, "r", encoding="utf-8") as f:
                    f.seek(offset)
                    chunk = f.read()
                    offsets[path] = f.tell()
                for line in chunk.splitlines():
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        packet = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    inner_name, inner_value = _offer_inner(packet)
                    if inner_name in OFFER_NAMES:
                        counter = (inner_value or {}).get("counter")
                        print(f"[OFFER] player={packet.get('player_id')} "
                              f"msg={inner_name} counter={counter}")
                        print(f"        {json.dumps(inner_value, default=str)[:400]}")
                        print(f"        -> reply: python tools/mimo_duel_cli.py reply "
                              f"--player {packet.get('player_id')} --counter {counter} "
                              f"--selection '<json>'")
                    elif inner_name:
                        pass  # sequence traffic (animations, board sync)
                    elif packet.get("name") != "SequenceMessage":
                        print(f"[{packet.get('name')}] player={packet.get('player_id')}")
            time.sleep(args.beat)
    except KeyboardInterrupt:
        print("\n[mimo-duel] stopped; heartbeat will go stale and the queue "
              "falls back to the AI bot.")


def cmd_status(args):
    bridge = _bridge_dir(args)
    hb = os.path.join(bridge, "heartbeat.json")
    try:
        age = time.time() - os.path.getmtime(hb)
        print(f"heartbeat: fresh ({age:.1f}s old)")
    except OSError:
        print("heartbeat: MISSING (queue will fill with the AI bot)")
    players = _find_players(bridge)
    if not players:
        print("no bridge players yet")
    for pid in players:
        out_rows = len(_read_jsonl(os.path.join(bridge, f"outbox-{pid}.jsonl")))
        in_rows = len(_read_jsonl(os.path.join(bridge, f"inbox-{pid}.jsonl")))
        print(f"player {pid}: outbox={out_rows} lines, inbox={in_rows} lines")
    agent_deck = os.path.join(bridge, "agent_deck.txt")
    if os.path.exists(agent_deck):
        try:
            with open(agent_deck, "r", encoding="utf-8-sig") as f:
                banner = next((l.strip() for l in f if l.strip()), "")
        except OSError:
            banner = "<unreadable>"
        print(f"agent deck: {os.path.getsize(agent_deck)} bytes from {agent_deck}; "
              f"{banner[:60]}")
    else:
        print("agent deck: none (env keys / BOT_DECKS pool)")


def cmd_show(args):
    bridge = _bridge_dir(args)
    players = [args.player] if args.player else _find_players(bridge)
    if not players:
        print("no bridge players yet")
        return
    for pid in players:
        rows = _read_jsonl(os.path.join(bridge, f"outbox-{pid}.jsonl"))
        if not args.full:
            rows = [r for r in rows if _offer_inner(r)[0] in OFFER_NAMES
                    or r.get("name") in OFFER_NAMES]
        for row in rows[-args.last:]:
            print(json.dumps(row, default=str))
        print(f"--- player {pid}: showed {min(args.last, len(rows))}/{len(rows)}")


def cmd_reply(args):
    bridge = _bridge_dir(args)
    counter = args.counter
    if counter is None:
        counter = _latest_counter(bridge, args.player)
    try:
        selection = json.loads(args.selection)
    except json.JSONDecodeError as e:
        print(f"invalid --selection JSON: {e}")
        sys.exit(2)
    line = {"counter": counter, "selection": selection}
    inbox = os.path.join(bridge, f"inbox-{args.player}.jsonl")
    with open(inbox, "a", encoding="utf-8") as f:
        f.write(json.dumps(line, default=str) + "\n")
    print(f"queued reply -> {inbox}: {json.dumps(line, default=str)[:200]}")


def cmd_end_turn(args):
    args.selection = "null"
    cmd_reply(args)


def cmd_set_deck(args):
    bridge = _bridge_dir(args)
    os.makedirs(bridge, exist_ok=True)
    target = os.path.join(bridge, "agent_deck.txt")
    name = (args.deck or "default").strip()
    if name.lower() in ("default", "clear", "none", "off"):
        if os.path.exists(target):
            os.remove(target)
            print(f"cleared {target}; agent seat falls back to env keys / BOT_DECKS pool.")
        else:
            print("no agent deck override set")
        return
    candidates = [name]
    if not os.path.isabs(name):
        candidates.append(os.path.join(_REPO_ROOT, name))
        candidates.append(os.path.join(_REPO_ROOT, "spirit", "tools", "Test Decks", name))
        if not name.lower().endswith(".txt"):
            candidates.append(os.path.join(_REPO_ROOT, "spirit", "tools", "Test Decks",
                                           name + ".txt"))
    path = next((p for p in candidates if os.path.isfile(p)), None)
    if not path:
        print(f"deck file not found: {name} (tried: {', '.join(candidates)})")
        sys.exit(2)
    with open(path, "r", encoding="utf-8-sig") as f:
        text = f.read()
    with open(target, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"agent deck <- {path}")
    print(f"wrote {target} ({len(text)} bytes); effective on the NEXT queue fill.")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("serve", help="heartbeat + outbox tail")
    p.add_argument("--bridge", default=None)
    p.add_argument("--beat", type=float, default=10.0)
    p.set_defaults(func=cmd_serve)

    p = sub.add_parser("status", help="bridge heartbeat / files")
    p.add_argument("--bridge", default=None)
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("show", help="print recent outbox packets")
    p.add_argument("--bridge", default=None)
    p.add_argument("--player", default=None)
    p.add_argument("--last", type=int, default=20)
    p.add_argument("--full", action="store_true")
    p.set_defaults(func=cmd_show)

    p = sub.add_parser("reply", help="append a reply to the inbox")
    p.add_argument("--bridge", default=None)
    p.add_argument("--player", required=True)
    p.add_argument("--counter", type=int, default=None)
    p.add_argument("--selection", required=True)
    p.set_defaults(func=cmd_reply)

    p = sub.add_parser("end-turn", help="reply with a null selection (end turn)")
    p.add_argument("--bridge", default=None)
    p.add_argument("--player", required=True)
    p.add_argument("--counter", type=int, default=None)
    p.set_defaults(func=cmd_end_turn)

    p = sub.add_parser("set-deck", help="pin the agent seat's deck for the next fill")
    p.add_argument("deck", nargs="?", default="default",
                   help="deck .txt (resolved in spirit/tools/Test Decks/) or 'default' to clear")
    p.add_argument("--bridge", default=None)
    p.set_defaults(func=cmd_set_deck)

    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
