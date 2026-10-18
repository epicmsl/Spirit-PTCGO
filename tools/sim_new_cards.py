"""Headless smoke test for the 4 newly scripted sets (Promo_SWSH, SWSH45, BW1,
CEL25 -- 561 card scripts).

Builds random 60-card decks that obey the 20 Pokemon / 15 Trainer / 15 Energy
structure the real client enforces, dealing as many of those slots as possible
to the NEW cards and filling the remainder from the older (already-shipped)
sets so every deck is playable.  Both seats are generic AI (no strategic
brain), so a game completing means the cards themselves don't crash the engine.

Usage (from repo root):
    .\\venv\\Scripts\\python.exe tools\\sim_new_cards.py --games 4
    .\\venv\\Scripts\\python.exe tools\\sim_new_cards.py --games 2 --trace
    .\\venv\\Scripts\\python.exe tools\\sim_new_cards.py --seed 7 --games 4
    .\\venv\\Scripts\\python.exe tools\\sim_new_cards.py --focus Cresselia_114
    .\\venv\\Scripts\\python.exe tools\\sim_new_cards.py --games 4 --sweep-never
"""

import argparse
import asyncio
import gc
import logging
import random
import sys
import time
import warnings
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from spirit.game.attributes import AttrID, CardType  # noqa: E402
from spirit.game.content.definitions import (  # noqa: E402
    Attack,
    def_for,
    evolves_from_chain,
)
from spirit.game.scripts.cards import loader as card_loader  # noqa: E402
from spirit.game.session import game_session as gs_mod  # noqa: E402
from spirit.game.session.game_session import GameSession  # noqa: E402

NEW_SETS = {"PROMO_SWSH", "SWSH45", "BW1", "CEL25"}

# --seed value, stashed so run_focus_sweep can re-seed global random per game
# (the engine draws from global random, not the local deckbuilding rng).
GLOBAL_SEED = None

DECK_POKEMON = 20
DECK_TRAINER = 15
DECK_ENERGY = 15
DECK_TOTAL = DECK_POKEMON + DECK_TRAINER + DECK_ENERGY  # 50

# V-UNION pieces are LegentHalf halves: they are unplayable on their own and
# would only dilute the test, so piece scripts are excluded from the Pokemon
# slot (the assembled combined defs stay in the loader's registry).
LEGEND_HALF = CardType.LEGEND_HALF


def _card_type(card) -> CardType:
    try:
        return CardType(card.get_attribute_value(AttrID.CARD_TYPE))
    except (TypeError, ValueError):
        return CardType.UNSET


def _basic_energy(card) -> bool:
    """Free_Energy / basic Energy cards that any deck can attach."""
    return card.key.upper() == "FREE_ENERGY"


def _is_new(card) -> bool:
    return card.key.upper() in NEW_SETS


def _name_is_new(name: str, pools: dict) -> bool:
    """True if a display name belongs to one of the 4 new sets.

    The AI log lines name cards by display_name (attack entries name the
    ability instead), so this maps the played-card name back to its set.
    """
    for card in pools["new_pokemon"]:
        if (getattr(card, "display_name", "") or "") == name:
            return True
    for card in pools["new_trainer"]:
        if (getattr(card, "display_name", "") or "") == name:
            return True
    return False


def _is_new_basic_pokemon(card) -> bool:
    return (_is_new(card)
            and _card_type(card) == CardType.POKEMON
            and getattr(card, "stage", None) == 0)


def _energy_name(card) -> str:
    return (getattr(card, "display_name", "") or "").lower()


def _build_pools(rng: random.Random):
    """Partition the loaded cards into the four deck-slot pools.

    Pokemon/Trainer pools are split new-vs-old so the builder can spend the new
    budget first and only dip into old cards for the remainder.  Energy is
    deliberately all-basic (basic Energy is universal attachment fuel; special
    energies in random decks just strand attackers).
    """
    cards = card_loader.load_all()
    if not card_loader.cards:
        card_loader.load_all()
    cards = card_loader.cards

    new_pokemon, old_pokemon = [], []
    new_trainer, old_trainer = [], []
    basic_energy = []
    for card in cards:
        ctype = _card_type(card)
        if ctype == CardType.POKEMON:
            (new_pokemon if _is_new(card) else old_pokemon).append(card)
        elif ctype == CardType.TRAINER:
            (new_trainer if _is_new(card) else old_trainer).append(card)
        elif ctype == CardType.ENERGY and _basic_energy(card):
            basic_energy.append(card)

    # A random deck that draws only Stage-1/2 Pokemon never gets a legal
    # opener, so guarantee a floor of Basic Pokemon in the Pokemon slot.
    new_basics = [c for c in new_pokemon if getattr(c, "stage", None) == 0]
    old_basics = [c for c in old_pokemon if getattr(c, "stage", None) == 0]
    rng.shuffle(new_pokemon)
    rng.shuffle(old_pokemon)
    rng.shuffle(new_trainer)
    rng.shuffle(old_trainer)
    rng.shuffle(basic_energy)
    return {
        "new_pokemon": new_pokemon,
        "old_pokemon": old_pokemon,
        "new_trainer": new_trainer,
        "old_trainer": old_trainer,
        "basic_energy": basic_energy,
        "new_basics": new_basics,
        "old_basics": old_basics,
    }


def build_random_deck(rng: random.Random, pools: dict, min_new: int = 30):
    """Build one 50-card deck: 20 Pokemon / 15 Trainer / 15 Energy.

    New cards fill the Pokemon and Trainer slots first (targeting ``min_new``
    of the 35 non-energy slots), basics are guaranteed in the opener, and the
    rest is filled from older sets.  Energy is basic only.  Up to two
    same-name copies keep random lists from being 35 one-ofs (a deck of pure
    singles rarely develops an attacker, which turns games into stall-fests
    that never exercise attacks).
    """
    pokemon, trainer = [], []

    # --- Pokemon (20) ---
    new_poke = list(pools["new_pokemon"])
    old_poke = list(pools["old_pokemon"])
    rng.shuffle(new_poke)
    rng.shuffle(old_poke)

    # Basics first so the deck can actually open.
    basics_target = 10
    new_basics = [c for c in new_poke if getattr(c, "stage", None) == 0]
    old_basics = [c for c in old_poke if getattr(c, "stage", None) == 0]
    for src in (new_basics, old_basics):
        for card in src:
            if len(pokemon) >= basics_target:
                break
            if card.guid not in {p.guid for p in pokemon}:
                pokemon.append(card)

    # Remainder of the Pokemon slot, new cards first (any stage).
    max_copies = 3
    for src in (new_poke, old_poke):
        for card in src:
            if len(pokemon) >= DECK_POKEMON:
                break
            if len([p for p in pokemon if p.guid == card.guid]) >= max_copies:
                continue
            pokemon.append(card)

    # --- Trainer (15) ---
    new_tr = list(pools["new_trainer"])
    old_tr = list(pools["old_trainer"])
    rng.shuffle(new_tr)
    rng.shuffle(old_tr)
    for src in (new_tr, old_tr):
        for card in src:
            if len(trainer) >= DECK_TRAINER:
                break
            if len([t for t in trainer if t.guid == card.guid]) >= max_copies:
                continue
            trainer.append(card)

    # --- Energy (15): basic only, spread across types ---
    energy = []
    pool_energy = list(pools["basic_energy"])
    rng.shuffle(pool_energy)
    for card in pool_energy:
        if len(energy) >= DECK_ENERGY:
            break
        energy.append(card)
    # If fewer than 15 distinct basic energies exist, repeat-fill the slot.
    i = 0
    while len(energy) < DECK_ENERGY and pool_energy:
        energy.append(pool_energy[i % len(pool_energy)])
        i += 1

    deck = pokemon + trainer + energy
    assert len(deck) == DECK_TOTAL, f"deck built {len(deck)} != {DECK_TOTAL}"
    return deck


def _decklist_entry(card):
    """(count, set_code, collector_number) triple for starter.build_deck_data."""
    num = card.get_attribute_value(AttrID.COLLECTOR_NUMBER)
    return (1, card.key.upper(), int(num))


def deck_data_from_cards(deck, name):
    """Resolve a list of Card objects into a client-shaped deck dict."""
    guids = [c.guid for c in deck]
    return {
        "deckID": f"sim-{name}",
        "deckName": name,
        "piles": {"deck": guids},
        "attributes": [],
    }


# --- Focused per-card forcing (item 4) -------------------------------
# Random 50-card decks rarely develop a given card: a Stage-2 whose pre-evo is
# not in the deck, or a Basic that sits on the bench all game, shows up as
# "never played" forever.  A focused deck instead hands the target 4 copies,
# its whole evolution chain, and energy biased toward its attack costs, so the
# target is actually exercised instead of just dealt.

_THE_BASIC_TYPES = ("water", "fire", "grass", "lightning", "psychic",
                    "fighting", "darkness", "metal", "fairy", "dragon")


def _def_for(card):
    return def_for(getattr(card, "guid", None)) if card is not None else None


def _logic_name(card):
    d = _def_for(card)
    if d is None:
        return ""
    spec = d.extra_attributes.get(str(AttrID.EVOLUTION_LOGIC_NAME.value))
    v = spec.get("value") if isinstance(spec, dict) else None
    return v if isinstance(v, str) else ""


_LOGIC_INDEX = None
_LOGIC_INDEX_SRC = None


def _logic_index(pools):
    global _LOGIC_INDEX, _LOGIC_INDEX_SRC
    src = id(card_loader.cards)
    if _LOGIC_INDEX is not None and _LOGIC_INDEX_SRC == src:
        return _LOGIC_INDEX
    index = {}
    for card in card_loader.cards:
        name = _logic_name(card)
        if name:
            index.setdefault(name, []).append(card)
    _LOGIC_INDEX = index
    _LOGIC_INDEX_SRC = src
    return index


def _pre_evo_card(logic_name, target, pools):
    """A playable Card for a pre-evolution logic name, biased to same set
    first, then any new set, then older sets."""
    candidates = _logic_index(pools).get(logic_name) or []
    new, old = None, None
    for card in candidates:
        if card.guid == target.guid:
            continue
        if card.key.upper() == target.key.upper():
            return card
        if card.key.upper() in NEW_SETS:
            new = new or card
        else:
            old = old or card
    return new or old


def _type_of_basic(card):
    name = (getattr(card, "display_name", "") or "").lower()
    for t in _THE_BASIC_TYPES:
        if t in name:
            return t
    return ""


def _focus_energy(target, pools, cap):
    """`cap` basic energies, up-weighted toward the target's attack costs."""
    need = []
    d = _def_for(target)
    if d is not None:
        for ability in getattr(d, "abilities", None) or []:
            if isinstance(ability, Attack):
                for t in ability.cost:
                    name = getattr(t, "name", "").lower()
                    if name and name != "colorless" and name not in need:
                        need.append(name)
    energy, used = [], set()
    for name in need:
        for card in pools["basic_energy"]:
            if _type_of_basic(card) == name:
                for _ in range(8):
                    if len(energy) >= cap:
                        break
                    energy.append(card)
                used.add(card.guid)
                break
    rest = [c for c in pools["basic_energy"] if c.guid not in used]
    for card in rest:
        if len(energy) >= cap:
            break
        energy.append(card)
    i = 0
    while len(energy) < cap and pools["basic_energy"]:
        energy.append(pools["basic_energy"][i % len(pools["basic_energy"])])
        i += 1
    return energy


def _fill_until(slot, candidates, cap, rng, max_copies=3):
    rng.shuffle(candidates)
    for card in candidates:
        if len(slot) >= cap:
            break
        if sum(1 for c in slot if c.guid == card.guid) >= max_copies:
            continue
        slot.append(card)


def build_focus_deck(target, rng, pools):
    """Build a 50-card deck that forces the target into play and into acting.

    Pokemon targets are dealt as a pure single-family deck -- 4 copies of the
    target plus 4 copies of each pre-evolution -- so the target (or the base it
    evolves from) is the only Basic and is therefore the starting Active, with
    energy biased to its attack costs.  Trainer targets sit as 4 copies in a
    normal deck and are played by the AI's trainer logic."""
    is_pokemon = _card_type(target) == CardType.POKEMON
    pokemon, trainer = [], []

    def _push(slot, card, copies):
        have = sum(1 for c in slot if c.guid == card.guid)
        for _ in range(copies - have):
            slot.append(card)

    if is_pokemon:
        _push(pokemon, target, 4)
        for logic in evolves_from_chain(target.guid):
            rep = _pre_evo_card(logic, target, pools)
            if rep is not None:
                _push(pokemon, rep, 4)
        # A Stage target whose base is missing from the pool must still open.
        if not any(getattr(c, "stage", None) == 0 for c in pokemon):
            _fill_until(pokemon, pools["new_basics"] + pools["old_basics"],
                        4, rng, max_copies=1)
        _fill_until(trainer, pools["new_trainer"] + pools["old_trainer"],
                    DECK_TRAINER, rng)
    else:
        _push(trainer, target, 4)
        _fill_until(pokemon, pools["new_basics"] + pools["old_basics"],
                    DECK_POKEMON, rng, max_copies=4)
        _fill_until(trainer, pools["new_trainer"] + pools["old_trainer"],
                    DECK_TRAINER, rng)

    energy_cap = DECK_TOTAL - len(pokemon) - len(trainer)
    deck = pokemon + trainer + _focus_energy(target, pools, energy_cap)
    assert len(deck) == DECK_TOTAL, f"focus deck built {len(deck)} != {DECK_TOTAL}"
    return deck


def _target_titles(target):
    """([attack titles], [selectable/triggered ability titles]) for a card."""
    d = _def_for(target)
    attacks, abilities = [], []
    if d is not None:
        for ability in getattr(d, "abilities", None) or []:
            if isinstance(ability, Attack):
                attacks.append(ability.title)
            elif ability.activation is not None or ability.trigger is not None \
                    or callable(ability.effect):
                abilities.append(ability.title)
    return attacks, abilities


def _target_activated(lines, entities, seat, target):
    """(played, attacked_titles, used_ability_titles) for one focused game.

    `played` is true if the target's GUID ever appeared on the board (covers the
    starting Active, which is placed without a 'plays' log) or was logged as
    played from hand."""
    d = _def_for(target)
    display = (getattr(d, "display_name", None)
               if d is not None else None) or \
        (getattr(target, "display_name", "") or "")
    attacks, abilities = _target_titles(target)
    played = target.guid in entities \
        or any(f"AI {seat} plays {display} (" in line for line in lines)
    used_atk = set()
    for line in lines:
        for t in attacks:
            if f"attacks with '{t}'" in line:
                used_atk.add(t)
    used_ab = set()
    for line in lines:
        if f"AI {seat} plays " not in line or "(UsePokemonAbility)" not in line:
            continue
        name = line.split(f"AI {seat} plays ")[1].rsplit(" (", 1)[0]
        if name in abilities:
            used_ab.add(name)
    return played, used_atk, used_ab


async def run_focus_sweep(targets, pools, rng, trace, grace, focus_games=1):
    """One focused game per target card; streams a live line per card so a
    long run can be aborted (Ctrl-C) without losing completed results."""
    reports = []
    for i, target in enumerate(targets, 1):
        attacks, abilities = _target_titles(target)
        report = None
        for game in range(1, focus_games + 1):
            deck1 = build_focus_deck(target, rng, pools)
            deck2 = build_random_deck(rng, pools)
            dd1 = deck_data_from_cards(deck1, f"Focus{game}-{i}A")
            dd2 = deck_data_from_cards(deck2, f"Focus{game}-{i}B")
            if GLOBAL_SEED is not None:
                random.seed(GLOBAL_SEED * 1_000_003 + i * 1000 + game)
            res = await run_game(i * 100 + game, dd1, dd2, trace, grace,
                                 _test_strategy())
            played, used_atk, used_ab = _target_activated(
                res["lines"], res.get("entities") or set(), "ai1", target)
            d = _def_for(target)
            stem = (getattr(d, "display_name", None) or
                    getattr(target, "display_name", "") or target.guid)
            if report is None:
                report = {
                    "stem": stem,
                    "played": played,
                    "attacks": set(),
                    "abilities": set(),
                    "acted_game": 0,
                    "errors": [],
                    "skipped_attacks": attacks,
                    "skipped_abilities": abilities,
                }
                reports.append(report)
            report["played"] = report["played"] or played
            report["attacks"] |= used_atk
            report["abilities"] |= used_ab
            if played and (used_atk or used_ab):
                report["acted_game"] += 1
            report["errors"] += res["errors"][:3]
        flag = ("ACTED" if report["played"]
                and (report["attacks"] or report["abilities"])
                else "PLAYED" if report["played"] else "NEVER")
        print(f"[focus:{flag}] {i}/{len(targets)} {report['stem']} "
              f"atk={sorted(report['attacks'])[:4]} "
              f"ab={sorted(report['abilities'])[:4]} "
              f"errs={len(report['errors'])}", flush=True)
        for line in report["errors"][:3]:
            print(f"        ERROR: {line[:300]}", flush=True)
    return reports


def _new_cards_by_stem():
    """Stem filename -> [new-set Card (s)] using the loader's own references,
    so the exact script-stem names (Cresselia_114) resolve unambiguously."""
    index = {}
    for ref, definition in card_loader.definitions.items():
        if (getattr(definition, "key", "") or "").upper() not in NEW_SETS:
            continue
        card = card_loader.cards_by_guid.get(getattr(definition, "guid", None))
        if card is not None:
            index.setdefault(Path(ref).stem, []).append(card)
    return index


def _resolve_focus_stems(stems, pools):
    targets, unknown = [], []
    by_stem = _new_cards_by_stem()
    for stem in stems:
        candidates = by_stem.get(stem) or []
        if not candidates or not any(
                _card_type(c) in (CardType.POKEMON, CardType.TRAINER)
                for c in candidates):
            unknown.append(stem)
            continue
        targets.append(next(c for c in candidates
                            if _card_type(c) in (CardType.POKEMON,
                                                 CardType.TRAINER)))
    return targets, unknown


def _resolve_focus_names(names, pools):
    """Names (from the never-played report) -> one new-set Card each."""
    by_name = {}
    for card in pools["new_pokemon"] + pools["new_trainer"]:
        by_name.setdefault((getattr(card, "display_name", "") or ""), []).append(
            card)
    targets, unresolved = [], []
    for name in names:
        candidates = by_name.get(name) or []
        if candidates:
            targets.append(candidates[0])
        else:
            unresolved.append(name)
    return targets, unresolved


class CaptureHandler(logging.Handler):
    def __init__(self):
        super().__init__(level=logging.INFO)
        self.lines = []

    def emit(self, record):
        try:
            message = record.getMessage()
            if record.exc_info and record.exc_info[0] is not None:
                message += "\n" + logging.Formatter().formatException(record.exc_info)
            self.lines.append(message)
        except Exception:
            pass


def record_is_error(line):
    return ("Error in gameplay sequence" in line
            or "Traceback (most recent call last)" in line
            or "was never awaited" in line
            or "Task exception was never retrieved" in line
            or "RuntimeWarning" in line)


# Abilities the generic AI must never fire on its own: each one ends the turn
# (or burns the VSTAR power) and a brainless bot would just throw games with
# them instead of developing a board.  Everything else is fair game -- the
# point of the smoke test is to exercise the new cards' Ability/attack code,
# and the generic AI skips ACTION_USE_ABILITY entirely unless a strategy
# allow-lists it (game_session._choose_ai_action).
_TURN_ENDING_ABILITIES = frozenset({
    "Intrepid Sword", "Iron Hands", "Reversal Energy", "Peon",
})


def _check_board_invariants(session) -> list:
    """Structural oracles run at every state-unit boundary.

    A card can never live under two parents at once, and every entity the board
    registered must stay reachable from the playmat. Violations of either almost
    always mean an effect silently duplicated or stranded a card.
    """
    board = getattr(session, "board_state", None)
    if board is None or getattr(board, "playmat", None) is None:
        return []
    problems = []

    reachable = set()
    stack = [board.playmat]
    dup = set()
    while stack:
        ent = stack.pop()
        if ent.entity_id in reachable:
            dup.add(ent.entity_id)
            continue
        reachable.add(ent.entity_id)
        stack.extend(ent.children)
    for eid in sorted(dup):
        problems.append(f"DUPLICATE entity reachable twice: {eid}")

    cache = getattr(board, "_entity_cache", None)
    if cache is not None:
        orphans = set(cache.keys()) - reachable
        for eid in sorted(orphans):
            ent = cache.get(eid)
            name = ent.get_entity_name() if ent is not None else "?"
            problems.append(f"ORPHAN entity not under playmat: {eid} ({name})")
    return problems


def _test_strategy():
    """A permissive brain: allow every non-turn-ending Ability, rank attacks
    by printed damage, and otherwise fall back to the greedy priority order.

    The generic AI (no strategy) never uses Pokemon Abilities at all, so
    handing both seats this minimal brain is what makes the smoke test
    actually reach the new cards' ability code instead of stalling 30 turns.
    """

    def allow_action(description, name, ctx):
        if description == gs_mod.ACTION_USE_ABILITY:
            return name not in _TURN_ENDING_ABILITIES
        return True

    def attack_score(name, damage, ctx):
        return float(damage or 0)

    def action_score(description, name, ctx):
        return 0.0

    return {
        "allow_action": allow_action,
        "attack_score": attack_score,
        "action_score": action_score,
    }


async def run_game(game_no, deck1, deck2, trace, grace_seconds, brain=None):
    pairing = {
        "players": {
            "ai1": {"client": None, "deck": deck1, "ready": True},
            "ai2": {"client": None, "deck": deck2, "ready": True},
        },
        "is_solo": False,
    }
    session = GameSession(f"sim-new-{game_no}", pairing)
    session.choreography_pauses = False
    # Generic AI on both seats; optionally hand both seats the same permissive
    # brain so Pokemon Abilities (which the generic AI never touches) are
    # exercised too -- the point is testing cards, not winning.
    session.players["ai1"].deck_strategy = brain
    session.players["ai2"].deck_strategy = brain

    invariant_hits = []
    entities_seen = set()
    orig_run_unit = session._run_state_unit

    async def _checked_run_unit(awaitable):
        result = await orig_run_unit(awaitable)
        board = getattr(session, "board_state", None)
        if board is not None and getattr(board, "playmat", None) is not None:
            stack = [board.playmat]
            visited = set()
            while stack:
                ent = stack.pop()
                if ent.entity_id in visited:
                    continue
                visited.add(ent.entity_id)
                guid = getattr(ent, "archetype_id", None)
                if guid:
                    entities_seen.add(guid)
                stack.extend(ent.children)
        for problem in _check_board_invariants(session):
            if problem not in invariant_hits:
                invariant_hits.append(problem)
        return result

    session._run_state_unit = _checked_run_unit

    capture = CaptureHandler()
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    root.addHandler(capture)
    gs_mod.AI_PROMPT_GRACE_SECONDS = grace_seconds

    started = time.time()
    timeout = False
    warning_lines = []
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        try:
            await session.start()
            await session.mark_player_ready("ai1")
            assert session.gameplay_task is not None, "gameplay never spawned"
            try:
                await asyncio.wait_for(asyncio.shield(session.gameplay_task), 240)
            except asyncio.TimeoutError:
                timeout = True
                session.gameplay_task.cancel()
                try:
                    await session.gameplay_task
                except (asyncio.CancelledError, Exception):
                    pass
            except asyncio.CancelledError:
                if session.game_result is None and not timeout:
                    pass
        finally:
            root.removeHandler(capture)
        # Force dangling coroutines to be garbage-collected inside the capture
        # window so any "coroutine ... was never awaited" RuntimeWarning is seen.
        gc.collect()
        for w in caught:
            warning_lines.append(f"{w.category.__name__}: {w.message}")

    elapsed = time.time() - started
    result = session.game_result or {}
    winner = result.get("winner")
    reason = result.get("reason") or ("timeout" if timeout else "no result")
    errors = [line for line in capture.lines if record_is_error(line)]
    errors += [line for line in warning_lines if record_is_error(line)]
    errors += [f"INVARIANT: {p}" for p in invariant_hits]

    if trace:
        print(f"--- game {game_no} trace ---")
        for line in capture.lines:
            if (" plays " in line and "AI ai" in line) or "deck search picks" in line \
                    or "damage counters" in line or "(AI) ends turn" in line \
                    or record_is_error(line):
                print("   ", line)

    return {
        "game": game_no,
        "winner": winner,
        "reason": reason,
        "turns": session.turn_state.turn_number,
        "seconds": round(elapsed, 1),
        "errors": errors,
        "lines": capture.lines,
        "entities": entities_seen,
    }


async def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--games", type=int, default=None,
                        help="random coverage games (default 4; 0 with --focus)")
    parser.add_argument("--trace", action="store_true",
                        help="print every AI decision line per game")
    parser.add_argument("--seed", type=int, default=None,
                        help="seed the deck RNG for reproducible decks")
    parser.add_argument("--grace", type=float, default=3.0,
                        help="AI prompt grace seconds (stall guard)")
    parser.add_argument("--abilities", action="store_true", default=True,
                        help="give both seats the permissive test brain so "
                             "Pokemon Abilities get exercised (default on)")
    parser.add_argument("--no-abilities", dest="abilities",
                        action="store_false",
                        help="use the plain generic AI (Abilities never used)")
    parser.add_argument("--focus", nargs="+", metavar="STEM",
                        help="run one focused game per script stem "
                             "(e.g. --focus Cresselia_114 HisuianBasculin_273)")
    parser.add_argument("--sweep-never", action="store_true",
                        help="after the random coverage games, force-activate "
                             "every card the random games never played")
    parser.add_argument("--focus-games", type=int, default=1,
                        help="focused games per target card (default 1)")
    parser.add_argument("--sweep-limit", type=int, default=0,
                        help="cap a --sweep-never run to N cards (0 = all)")
    parser.add_argument("--sweep-offset", type=int, default=0,
                        help="skip the first N never-played cards (chunking)")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        stream=sys.stdout,
        force=True,
    )

    rng = random.Random(args.seed)
    # The engine draws from the GLOBAL random module (coin flips, deck/prize
    # shuffles, AI tie-breaks -- game_session/effects/product), not the local
    # deckbuilding rng. An unseeded global random made the coverage list drift
    # between processes, which broke --sweep-offset chunking (the never-played
    # list reordered itself, so chunks overlapped or dropped cards). Seeding it
    # from --seed makes a whole run reproducible and the chunks stable.
    if args.seed is not None:
        random.seed(args.seed)
    global GLOBAL_SEED
    GLOBAL_SEED = args.seed
    pools = _build_pools(rng)
    print(f"[pools] new pokemon={len(pools['new_pokemon'])} "
          f"old pokemon={len(pools['old_pokemon'])} "
          f"new trainer={len(pools['new_trainer'])} "
          f"old trainer={len(pools['old_trainer'])} "
          f"basic energy={len(pools['basic_energy'])}")

    results = []
    played_names = set()
    attack_names = set()
    new_cards_seen = set()
    games_to_run = args.games
    if games_to_run is None:
        games_to_run = 0 if (args.focus and not args.sweep_never) else 4
    for n in range(1, games_to_run + 1):
        deck1 = build_random_deck(rng, pools)
        deck2 = build_random_deck(rng, pools)
        new_cards_seen.update(c.guid for c in deck1 if _is_new(c))
        new_cards_seen.update(c.guid for c in deck2 if _is_new(c))
        new_in_1 = sum(1 for c in deck1 if _is_new(c))
        new_in_2 = sum(1 for c in deck2 if _is_new(c))
        dd1 = deck_data_from_cards(deck1, f"NewCardsA-{n}")
        dd2 = deck_data_from_cards(deck2, f"NewCardsB-{n}")
        print(f"[deck {n}] ai1 new-cards={new_in_1}/50  ai2 new-cards={new_in_2}/50")

        if args.seed is not None:
            random.seed(args.seed * 1000 + n)
        res = await run_game(n, dd1, dd2, args.trace, args.grace,
                             _test_strategy() if args.abilities else None)
        for line in res["lines"]:
            if " plays " in line and "AI ai" in line and line.endswith(")."):
                played_names.add(line[line.rfind("(") + 1:-2])
                played_names.add(line.split(" plays ")[1].rsplit(" (", 1)[0])
            if "attacks with '" in line:
                attack_names.add(line.split("attacks with '")[1].split("'")[0])
        results.append(res)
        print(
            f"Game {res['game']}: winner={res['winner']} ({res['reason']}) "
            f"turns={res['turns']} time={res['seconds']}s"
        )
        for line in res["errors"][:5]:
            print(f"    ERROR: {line[:300]}")

    print("\n=== summary ===")
    wins = {"ai1": 0, "ai2": 0}
    for res in results:
        if res["winner"] in wins:
            wins[res["winner"]] += 1
    print(f"ai1 wins: {wins['ai1']}/{len(results)}")
    print(f"ai2 wins: {wins['ai2']}/{len(results)}")
    crash = sum(1 for r in results if "game error" in r["reason"].lower())
    print(f"crash-fallback results: {crash}/{len(results)}")
    total_errors = sum(len(r["errors"]) for r in results)
    print(f"gameplay errors: {total_errors}")

    new_played = {n for n in played_names if _name_is_new(n, pools)}
    print(f"\n=== coverage ===")
    print(f"new cards dealt into decks: {len(new_cards_seen)}/561")
    print(f"distinct new cards played/activated: {len(new_played)}")
    print(f"distinct attacks used (any set): {len(attack_names)}")

    all_new_names = {(getattr(c, "display_name", "") or "")
                     for c in pools["new_pokemon"] + pools["new_trainer"]}
    all_new_names.discard("")
    never = sorted(all_new_names - new_played)
    print(f"new cards NEVER played/activated: {len(never)}/{len(all_new_names)}")
    for name in never[:60]:
        print(f"    - {name}")

    focus_errors = 0
    if args.focus or args.sweep_never:
        if args.focus:
            targets, unknown = _resolve_focus_stems(args.focus, pools)
            for stem in unknown:
                print(f"[focus] UNKNOWN stem: {stem}")
        else:
            targets, unresolved = _resolve_focus_names(never, pools)
            for name in unresolved:
                print(f"[focus] no new-set card for never-played name: "
                      f"{name!r}")
            total = len(targets)
            if args.sweep_offset:
                targets = targets[args.sweep_offset:]
            if args.sweep_limit:
                targets = targets[:args.sweep_limit]
            print(f"\n=== focused sweep: {len(targets)} of {total} "
                  f"never-played card(s) "
                  f"(offset={args.sweep_offset}, limit={args.sweep_limit}) ===")
        reports = await run_focus_sweep(targets, pools, rng, args.trace,
                                        args.grace, args.focus_games)
        acted = [r for r in reports if r["played"]
                 and (r["attacks"] or r["abilities"])]
        played_only = [r for r in reports if r["played"]
                       and not r["attacks"] and not r["abilities"]]
        never_acted = [r for r in reports if not r["played"]]
        focus_errors = sum(len(r["errors"]) for r in reports)
        print(f"=== focused summary: acted={len(acted)}/{len(reports)}  "
              f"played-only={len(played_only)}  never={len(never_acted)}  "
              f"errors={focus_errors} ===")
    return 0 if total_errors == 0 and crash == 0 and focus_errors == 0 else 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
