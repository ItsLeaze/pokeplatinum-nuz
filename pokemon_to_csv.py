import os
import json
import csv

# === CONFIG ===
POKEMON_DIR = "res/pokemon"
OUTPUT_CSV = "pokemon.csv"

# === TYPE TRANSLATION (same as moves) ===
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

def find_pokemon_files(base_dir):
    """Find all data.json files in pokemon folders."""
    files_found = []
    for root, dirs, files in os.walk(base_dir):
        if "data.json" in files:
            files_found.append(os.path.join(root, "data.json"))
    return files_found

def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def translate_type(type_value):
    return TYPE_MAP.get(type_value, type_value)

def clean_ability(ability):
    """Remove ABILITY_ prefix."""
    if ability.startswith("ABILITY_"):
        return ability[len("ABILITY_"):]
    return ability

def get_pokemon_name_from_path(path):
    """Extract folder name as Pokémon name."""
    return os.path.basename(os.path.dirname(path))

def process_pokemon(data, file_path):
    row = {}

    # Name from folder
    row["name"] = get_pokemon_name_from_path(file_path)

    # Types (always 2)
    types = data.get("types", ["", ""])
    row["type1"] = translate_type(types[0])
    row["type2"] = translate_type(types[1])

    # Abilities (usually 2)
    abilities = data.get("abilities", ["", ""])
    row["ability1"] = clean_ability(abilities[0])
    row["ability2"] = clean_ability(abilities[1])

    # Base stats
    stats = data.get("base_stats", {})
    row["hp"] = stats.get("hp", "")
    row["attack"] = stats.get("attack", "")
    row["defense"] = stats.get("defense", "")
    row["special_attack"] = stats.get("special_attack", "")
    row["special_defense"] = stats.get("special_defense", "")
    row["speed"] = stats.get("speed", "")

    return row

def main():
    files = find_pokemon_files(POKEMON_DIR)
    rows = []

    for file in files:
        data = load_json(file)
        row = process_pokemon(data, file)
        rows.append(row)

    # CSV columns
    fieldnames = [
        "name",
        "type1", "type2",
        "ability1", "ability2",
        "hp", "attack", "defense",
        "special_attack", "special_defense", "speed"
    ]

    # Write CSV
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Exported {len(rows)} Pokémon to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()