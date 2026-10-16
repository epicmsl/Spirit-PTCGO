import os
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID

SETS = ["BW1", "CEL25", "Promo_SWSH", "SWSH45"]
BASE = Path(__file__).resolve().parent.parent.parent / "spirit" / "game" / "scripts" / "cards"
# Type column labels (New Entity vs Alt-Art -> target). Seeded from the audit via
# port_type_labels.py; maintained by hand thereafter. Keys are "SET/collector".
LABELS_PATH = Path(__file__).resolve().parent / "type_labels.json"
TYPE_LABELS = json.loads(LABELS_PATH.read_text(encoding="utf-8")) if LABELS_PATH.exists() else {}
missing_label_keys = []

def format_cost(cost):
    if not cost:
        return ""
    parts = []
    for etype, count in cost.items():
        parts.append(f"{etype.name} x{count}")
    return ", ".join(parts)

def extract_card(filepath):
    ns = {}
    code = filepath.read_text(encoding="utf-8")
    exec(compile(code, str(filepath), "exec"), ns)
    card = ns["card"]
    return card

def type_label_for(set_name, collector_number):
    label = TYPE_LABELS.get(f"{set_name}/{collector_number}")
    if label is None:
        missing_label_keys.append(f"{set_name}/{collector_number}")
        return "New Entity"
    return label

def card_to_row(set_name, filepath):
    card = extract_card(filepath)
    name = card.display_name or card.name.split(".")[-1]
    if filepath.stem.endswith("_Combined"):
        # V-UNION combined/display script: same collector as piece 1, so suffix
        # the name to keep (code, name) keys unique while keeping both rows.
        name = f"{name} (Combined)"
    col_num = card.collector_number

    hp_val = card.extra_attributes.get(str(AttrID.HP.value), {})
    hp = hp_val.get("value", "-") if isinstance(hp_val, dict) else "-"

    attacks = []
    abilities = []
    # Not every CardDefinition subclass carries .abilities (EnergyCardDef and
    # VUnionPieceCardDef do not); pieces display only the combined card's
    # attacks, so they row out as "-" instead of exploding into ERROR rows.
    for ab in getattr(card, "abilities", None) or []:
        if isinstance(ab, Attack):
            cost_str = format_cost(ab.cost)
            dmg = ab.damage if ab.damage else "-"
            op = ab.damage_operator if ab.damage_operator else ""
            attacks.append(f"{ab.title} ({cost_str}) {op}{dmg} dmg")
        elif isinstance(ab, Ability):
            text = ab.game_text if ab.game_text else ab.title
            if len(text) > 150:
                text = text[:147] + "..."
            abilities.append(f"{ab.title}: {text}")

    # PNG on disk is always named after the script stem (display names can
    # contain spaces/!/' that the asset files do not use).
    png_name = f"{filepath.stem}.png"
    type_label = type_label_for(set_name, col_num)

    attacks_str = " | ".join(attacks) if attacks else "-"
    abilities_str = " | ".join(abilities) if abilities else "-"

    return f"| {set_name}/{col_num} | {name} | {hp} | {attacks_str} | {abilities_str} | {png_name} | {type_label} |", type_label

def _num_key(p):
    tail = p.stem.split("_")[-1]
    # Non-numeric tails (e.g. *_Combined) sort after the numerics; the stem
    # tiebreaker keeps output deterministic regardless of glob order.
    return (0, int(tail), p.stem) if tail.isdigit() else (1, 0, p.stem)

sections = []
set_stats = {}
error_rows = 0
total = 0
alt_total = 0
ne_total = 0
for s in SETS:
    card_files = sorted((BASE / s).glob("*.py"), key=_num_key)
    rows = []
    alt = ne = 0
    for fp in card_files:
        try:
            row, label = card_to_row(s, fp)
            rows.append(row)
            if label.startswith("Alt-Art"):
                alt += 1
            else:
                ne += 1
        except Exception as e:
            rows.append(f"| {s} | ERROR: {fp.name} | - | {e} | - | - |")
            error_rows += 1
    count = len(card_files)
    sections.append((s, rows))
    set_stats[s] = (count, alt, ne)
    total += count
    alt_total += alt
    ne_total += ne

lines = []
lines.append(f"# Added Cards Reference ({total} cards across {len(SETS)} sets)")
lines.append("")
lines.append("Generated from card script files in `spirit/game/scripts/cards/`.")
lines.append("")
lines.append("## Summary")
lines.append("")
lines.append("| Set | Card Count | Alt-Arts | New Entities |")
lines.append("|-----|-----------|----------|--------------|")
for s in SETS:
    count, alt, ne = set_stats[s]
    lines.append(f"| {s} | {count} | {alt} | {ne} |")
lines.append(f"| **Total** | **{total}** | **{alt_total}** | **{ne_total}** |")
lines.append("")
lines.append("## Card Details")
for s, rows in sections:
    lines.append("")
    lines.append(f"### {s}")
    lines.append("")
    lines.append("| Code | Name | HP | Attacks | Abilities | PNG | Type |")
    lines.append("|------|------|----|---------|-----------|-----|------|")
    lines.extend(rows)

output = Path(__file__).resolve().parent / "added_cards_reference.md"
output.write_text("\n".join(lines), encoding="utf-8")
print(f"Written {len(lines)} lines to {output}")
print(f"Rows: {total} ({alt_total} Alt-Arts, {ne_total} New Entities), ERROR rows: {error_rows}")
if missing_label_keys:
    uniq = sorted(set(missing_label_keys))
    print(f"WARNING: {len(uniq)} collector key(s) missing from type_labels.json, "
          f"labeled 'New Entity': {uniq[:20]}{' ...' if len(uniq) > 20 else ''}")
