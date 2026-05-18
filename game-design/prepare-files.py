#!/usr/bin/env python3

import json
from pathlib import Path
from collections import defaultdict

# ============================================================================
# CONFIG
# ============================================================================

RESULT_ROOT = Path(".")
ROOT = Path("..")

POKEMON_DIR = ROOT / "res" / "pokemon"
MOVES_DIR = ROOT / "res" / "battle" / "moves"
ENCOUNTERS_DIR = ROOT / "res" / "field" / "encounters"
HONEY_TREE_FILE = ENCOUNTERS_DIR / "encounters_honey_tree.json"

OUTPUT_FILE = RESULT_ROOT / "compiled_battle_data.json"

ENABLE_ITEM_HEURISTIC = True

# ============================================================================
# MOVE TAG COLLECTIONS
# Fill these later with move identifiers like "MOVE_FIRE_PUNCH"
# ============================================================================

PUNCHING_MOVES = set((
    "ICE_PUNCH",
    "FIRE_PUNCH",
    "THUNDER_PUNCH",
    "MACH_PUNCH",
    "FOCUS_PUNCH",
    "DIZZY_PUNCH",
    "DYNAMIC_PUNCH",
    "HAMMER_ARM",
    "MEGA_PUNCH",
    "COMET_PUNCH",
    "METEOR_MASH",
    "SHADOW_PUNCH",
    "DRAIN_PUNCH",
    "BULLET_PUNCH",
    "SKY_UPPERCUT"
))

BITING_MOVES = set((
    "BITE",
    "CRUNCH",
    "FIRE_FANG",
    "HYPER_FANG",
    "ICE_FANG",
    "POISON_FANG",
    "THUNDER_FANG"
))

SLICING_MOVES = set((
    "AERIAL_ACE",
    "AIR_CUTTER",
    "AIR_SLASH",
    "FURY_CUTTER",
    "LEAF_BLADE",
    "NIGHT_SLASH",
    "PSYCHO_CUT",
    "SHADOW_CLAW",
    "SLASH",
    "X_SCISSOR",
    "CROSS_POISON",
    "CRUSH_CLAW",
    "CUT",
    "DRAGON_CLAW",
    "METAL_CLAW",
    "RAZOR_LEAF"
))

PULSE_MOVES = set((
    "AURA_SPHERE",
    "DARK_PULSE",
    "DRAGON_PULSE",
    "WATER_PULSE"
))

# ============================================================================
# STATIC ENCOUNTERS (starters, gifts, in-game trades, etc.)
# ============================================================================

STATIC_ENCOUNTERS = {
    "starter": [
        "turtwig",
        "chimchar",
        "piplup"
    ],

    "jubilife_briefcase": [
        "bulbasaur",
        "charmander",
        "squirtle"
    ],

    "oreburgh_gift": [
        "seedot"
    ],

    "floaroma_briefcase": [
        "qwilfish",
        "dunsparce",
        "shuckle"
    ],

    "eterna_gift": [
        "togepi"
    ],

    "eterna_trade": [
        "electrike"
    ],

    "fossils_1": [
        "omanyte",
        "kabuto",
        "anorith",
        "lileep"
    ],

    "hearthome_gift": [
        "eevee"
    ],

    "cafe_briefcase": [
        "mime_jr",
        "bonsly",
        "smoochum"
    ],

    "veilstone_briefcase": [
        "hitmontop",
        "hitmonlee",
        "hitmonchan"
    ],

    "veilstone_gift": [
        "shellder"
    ],

    "iron_island_gift": [
        "riolu"
    ],

    "snowpoint_trade": [
        "grimer"
    ]
}

# ============================================================================
# HELPERS
# ============================================================================

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def safe_int(value, default=0):
    if value is None:
        return default
    return int(value)


def normalize_species(species):
    """
    SPECIES_AIPOM -> aipom
    """
    return species.removeprefix("SPECIES_").lower()


# ============================================================================
# LOAD MOVES
# ============================================================================

def load_moves():
    moves = {}

    for move_dir in sorted(MOVES_DIR.iterdir()):
        if not move_dir.is_dir():
            continue

        data_file = move_dir / "data.json"

        if not data_file.exists():
            continue

        move_data = load_json(data_file)

        move_name = move_dir.name

        moves[move_name] = {
            "name": move_name,
            "class": move_data.get("class"),
            "type": move_data.get("type"),
            "power": safe_int(move_data.get("power")),
            "accuracy": safe_int(move_data.get("accuracy"), 100),
            "effect_type": move_data.get("effect", {}).get("type"),
            "priority": safe_int(move_data.get("priority")),
        }

    return moves


# ============================================================================
# EFFECTIVE POWER CALCULATION
# ============================================================================

def calculate_effective_power(pokemon_data, move_data, ability):
    """
    Effective power formula:
    offensive_stat * move_power * modifiers
    """

    move_power = move_data["power"]

    if move_power <= 0:
        return 0

    move_class = move_data["class"]
    move_type = move_data["type"] if ability != "ABILITY_NORMALIZE" else "TYPE_NORMAL"
    effect_type = move_data["effect_type"]

    base_stats = pokemon_data["base_stats"]
    speed_stat = base_stats["speed"]

    if move_class == "CLASS_PHYSICAL":
        offensive_stat = base_stats["attack"]
    else:
        offensive_stat = base_stats["special_attack"]

    modifier = 1.0

    # ----------------------------------------------------------------------
    # STAB
    # ----------------------------------------------------------------------

    if move_type in pokemon_data["types"]:
        if ability == "ABILITY_ADAPTABILITY":
            modifier *= 2.0
        else:
            modifier *= 1.5

    # ----------------------------------------------------------------------
    # Huge Power / Pure Power
    # ----------------------------------------------------------------------

    if (
        move_class == "CLASS_PHYSICAL"
        and ability in ("ABILITY_HUGE_POWER", "ABILITY_PURE_POWER")
    ):
        modifier *= 2.0

    # ----------------------------------------------------------------------
    # Technician
    # ----------------------------------------------------------------------

    if (
        ability == "ABILITY_TECHNICIAN"
        and move_power <= 60
    ):
        modifier *= 1.5

    # ----------------------------------------------------------------------
    # Multi-hit
    # ----------------------------------------------------------------------

    if effect_type == "BATTLE_EFFECT_MULTI_HIT":
        if ability == "ABILITY_SKILL_LINK":
            modifier *= 5.0
        else:
            modifier *= 2.5
    if effect_type == "BATTLE_EFFECT_HIT_TWICE" or effect_type == "BATTLE_EFFECT_POISON_MULTI_HIT":
        modifier *= 2.0
    if effect_type == "BATTLE_EFFECT_HIT_THREE_TIMES":
        modifier *= 3.0

    # ----------------------------------------------------------------------
    # Multi-hit
    # ----------------------------------------------------------------------

    if effect_type == "BATTLE_EFFECT_DOUBLE_POWER_EACH_TURN_LOCK_INTO":
        modifier *= 2.0

    # ----------------------------------------------------------------------
    # Double-Damage if moving after
    # ----------------------------------------------------------------------

    if effect_type == "BATTLE_EFFECT_DOUBLE_POWER_IF_HIT" and (speed_stat < 80 or move_data["priority"] < 0):
        modifier *= 2.0

    # ----------------------------------------------------------------------
    # Iron Fist
    # ----------------------------------------------------------------------

    if (
        ability == "ABILITY_IRON_FIST"
        and move_data["name"].upper() in PUNCHING_MOVES
    ):
        modifier *= 1.2

    # ----------------------------------------------------------------------
    # Sharpness
    # ----------------------------------------------------------------------

    if (
        ability == "ABILITY_SHARPNESS"
        and move_data["name"].upper() in SLICING_MOVES
    ):
        modifier *= 1.5

    # ----------------------------------------------------------------------
    # Mega Launcher
    # ----------------------------------------------------------------------

    if (
        ability == "ABILITY_MEGA_LAUNCHER"
        and move_data["name"].upper() in PULSE_MOVES
    ):
        modifier *= 1.5

    # ----------------------------------------------------------------------
    # Strong Jaw
    # ----------------------------------------------------------------------

    if (
        ability == "ABILITY_STRONG_JAW"
        and move_data["name"].upper() in BITING_MOVES
    ):
        modifier *= 1.5

    # ----------------------------------------------------------------------
    # Guts / Facade
    # ----------------------------------------------------------------------

    if ability == "ABILITY_GUTS":
        modifier *= 1.5

    if effect_type == "BATTLE_EFFECT_DOUBLE_POWER_WHEN_STATUSED":
        modifier *= 2

    # ----------------------------------------------------------------------
    # Reckless
    # ----------------------------------------------------------------------

    if effect_type.startswith("BATTLE_EFFECT_RECOIL") or effect_type == "BATTLE_EFFECT_CRASH_ON_MISS":
        if ability == "ABILITY_RECKLESS":
            modifier *= 1.2

    if ENABLE_ITEM_HEURISTIC:
        if ability != "ABILITY_GUTS" and (
            ability == "ABILITY_COMPOUND_EYES"
            or ability == "ABILITY_NO_GUARD"
            or move_data["accuracy"] == 0
            or move_data["accuracy"] == 100
            or (ability == "ABILITY_SNOW_WARNING" and move_data["name"] == "blizzard")
            or effect_type == "BATTLE_EFFECT_DOUBLE_POWER_WHEN_STATUSED"
        ):
            modifier *= 1.2

    return round(offensive_stat * move_power * modifier, 2)


# ============================================================================
# LOAD POKEMON
# ============================================================================

def load_pokemon(moves):
    pokemon = {}

    for pokemon_dir in sorted(POKEMON_DIR.iterdir()):
        if not pokemon_dir.is_dir():
            continue

        data_file = pokemon_dir / "data.json"

        if not data_file.exists():
            continue

        data = load_json(data_file)

        pokemon_name = pokemon_dir.name

        abilities = data.get("abilities", [])
        types = data.get("types", [])

        compiled_moves = []

        for level, move_id in data.get("learnset", {}).get("by_level", []):

            move_key = move_id.removeprefix("MOVE_").lower()

            if move_key not in moves:
                continue

            move_data = moves[move_key]

            move_entry = {
                "level": level,
                "move": move_key,
                "power": move_data["power"],
                "accuracy": move_data["accuracy"],
                "class": move_data["class"],
                "type": move_data["type"],
                "effect_type": move_data["effect_type"],
                "effective_power": {}
            }

            for ability in abilities:
                move_entry["effective_power"][ability] = (
                    calculate_effective_power(
                        {
                            "base_stats": data["base_stats"],
                            "types": types
                        },
                        move_data,
                        ability
                    )
                )

            compiled_moves.append(move_entry)

        # ------------------------------------------------------------------
        # Evolutions
        # ------------------------------------------------------------------

        evolutions = []

        for evo in data.get("evolutions", []):
            if len(evo) < 3:
                continue

            method = evo[0]
            parameter = evo[1]
            target_species = evo[2]

            # Default fallback level
            level = 33

            # Any level-based evolution keeps its actual level parameter
            if method.startswith("EVO_LEVEL") and method != "EVO_LEVEL_KNOW_MOVE" and method != "EVO_LEVEL_WITH_HELD_ITEM_NIGHT" and method != "EVO_LEVEL_WITH_HELD_ITEM_DAY" and method != "EVO_LEVEL_SPECIES_IN_PARTY":
                level = safe_int(parameter, level)

            evolutions.append({
                "method": method,
                "target": normalize_species(target_species),
                "level": level
            })

        pokemon[pokemon_name] = {
            "name": pokemon_name,
            "base_stats": data.get("base_stats", {}),
            "types": types,
            "abilities": abilities,
            "evolutions": evolutions,
            "moves": compiled_moves
        }

    return pokemon


# ============================================================================
# ENCOUNTER PARSING
# ============================================================================

def deduplicate_encounters(encounters, use_min_level=False):
    """
    Keeps only the lowest level occurrence per species.
    """

    result = {}

    for entry in encounters:

        species = normalize_species(entry["species"])

        if use_min_level:
            level = safe_int(entry.get("level_min"))
        else:
            level = safe_int(entry.get("level"))

        if species not in result:
            result[species] = level
        else:
            result[species] = min(result[species], level)

    return [
        {
            "species": species,
            "level": level
        }
        for species, level in sorted(result.items())
    ]


def load_encounters():
    encounter_data = {}

    for encounter_file in sorted(ENCOUNTERS_DIR.glob("*.json")):

        data = load_json(encounter_file)

        location_name = encounter_file.stem

        encounter_data[location_name] = {
            "location": location_name,

            "land": deduplicate_encounters(data.get("land_encounters", [])),
            "surf": deduplicate_encounters(data.get("surf_encounters", []), use_min_level=True),
            "old_rod": deduplicate_encounters(data.get("old_rod_encounters", []), use_min_level=True),
            "good_rod": deduplicate_encounters(data.get("good_rod_encounters", []), use_min_level=True),
            "super_rod": deduplicate_encounters(data.get("super_rod_encounters", []), use_min_level=True),
        }

    # ----------------------------------------------------------------------
    # Inject static encounters
    # ----------------------------------------------------------------------

    for static_group_name, species_list in STATIC_ENCOUNTERS.items():

        encounter_data[static_group_name] = {
            "location": static_group_name,
            "land": [
                {"species": species, "level": 10}
                for species in species_list
            ],
            "surf": [],
            "old_rod": [],
            "good_rod": [],
            "super_rod": []
        }

    # ----------------------------------------------------------------------
    # Inject honey tree encounters
    # ----------------------------------------------------------------------

    if HONEY_TREE_FILE.exists():
        honey_data = load_json(HONEY_TREE_FILE)

        for rarity in ["common", "uncommon", "rare"]:
            honey_encounters = []

            for species in honey_data.get(rarity, []):

                honey_encounters.append({
                    "species": normalize_species(species),
                    "level": 10
                })

            encounter_data["honey_tree_" + rarity] = {
                "location": "honey_tree_" + rarity,
                "land": honey_encounters,
                "surf": [],
                "old_rod": [],
                "good_rod": [],
                "super_rod": []
            }

    return encounter_data


# ============================================================================
# MAIN
# ============================================================================

def main():
    print("Loading moves...")
    moves = load_moves()

    print(f"Loaded {len(moves)} moves")

    print("Loading Pokémon...")
    pokemon = load_pokemon(moves)

    print(f"Loaded {len(pokemon)} Pokémon")

    print("Loading encounters...")
    encounters = load_encounters()

    print(f"Loaded {len(encounters)} encounter locations")

    output = {
        "pokemon": pokemon,
        "moves": moves,
        "encounters": encounters
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)

    print(f"Wrote compiled data to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()