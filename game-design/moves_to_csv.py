import os
import json
import csv

# === CONFIG ===
MOVES_DIR = "./res/battle/moves"
OUTPUT_CSV = "moves.csv"

# === TRANSLATIONS ===
CLASS_MAP = {
    "CLASS_PHYSICAL": "Physical",
    "CLASS_SPECIAL": "Special",
    "CLASS_STATUS": "Status",
}

TYPE_MAP = {
    "TYPE_NORMAL": "Normal",
    "TYPE_FIGHTING": "Fighting",
    "TYPE_FLYING": "Flying",
    "TYPE_POISON": "Poison",
    "TYPE_GROUND": "Ground",
    "TYPE_ROCK": "Rock",
    "TYPE_BUG": "Bug",
    "TYPE_GHOST": "Ghost",
    "TYPE_STEEL": "Steel",
    "TYPE_MYSTERY": "Mystery",
    "TYPE_FIRE": "Fire",
    "TYPE_WATER": "Water",
    "TYPE_GRASS": "Grass",
    "TYPE_ELECTRIC": "Electric",
    "TYPE_PSYCHIC": "Psychic",
    "TYPE_ICE": "Ice",
    "TYPE_DRAGON": "Dragon",
    "TYPE_DARK": "Dark",
    "TYPE_FAIRY": "Fairy",
}

RANGE_MAP = {
    "RANGE_SINGLE_TARGET": "Single Target",
    "RANGE_SINGLE_TARGET_SPECIAL": "Single Target (Special)",
    "RANGE_RANDOM_OPPONENT": "Random Opponent",
    "RANGE_ADJACENT_OPPONENTS": "Adjacent Opponents",
    "RANGE_ALL_ADJACENT": "All Adjacent",
    "RANGE_USER": "User",
    "RANGE_USER_SIDE": "User Side",
    "RANGE_FIELD": "Field",
    "RANGE_OPPONENT_SIDE": "Opponent Side",
    "RANGE_ALLY": "Ally",
    "RANGE_USER_OR_ALLY": "User or Ally",
    "RANGE_SINGLE_TARGET_ME_FIRST": "Single Target (Me First)",
}

FLAGS = [
    "MAKES_CONTACT",
    "CAN_PROTECT",
    "CAN_MAGIC_COAT",
    "CAN_SNATCH",
    "CAN_MIRROR_MOVE",
    "TRIGGERS_KINGS_ROCK",
    "HIDES_HP_GAUGES",
    "HIDES_SHADOWS",
]

def find_move_files(base_dir):
    """Find all data.json files in move folders."""
    move_files = []
    for root, dirs, files in os.walk(base_dir):
        if "data.json" in files:
            move_files.append(os.path.join(root, "data.json"))
    return move_files

def load_move(file_path):
    """Load a single move JSON."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def translate(value, mapping):
    """Translate a value using a mapping dict."""
    return mapping.get(value, value)

def process_move(data):
    """Convert raw move data into a flat CSV row."""
    row = {}

    row["name"] = data.get("name", "")
    row["class"] = translate(data.get("class"), CLASS_MAP)
    row["type"] = translate(data.get("type"), TYPE_MAP)
    row["power"] = data.get("power", "")
    row["accuracy"] = data.get("accuracy", "")
    row["pp"] = data.get("pp", "")
    row["priority"] = data.get("priority", "")

    # Effect
    effect = data.get("effect", {})
    row["effect_type"] = effect.get("type", "")
    row["effect_chance"] = effect.get("chance", "")

    # Range
    row["range"] = translate(data.get("range"), RANGE_MAP)

    # Flags → Y/N columns
    move_flags = set(data.get("flags", []))
    for flag in FLAGS:
        row[flag] = "Y" if flag in move_flags else "N"

    return row

def main():
    move_files = find_move_files(MOVES_DIR)
    rows = []

    move_files.sort()
    for file in move_files:
        data = load_move(file)
        row = process_move(data)
        rows.append(row)

    # Define CSV columns
    fieldnames = [
        "name", "class", "type", "power", "accuracy", "pp",
        "priority", "effect_type", "effect_chance", "range"
    ] + FLAGS

    # Write CSV
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Exported {len(rows)} moves to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()