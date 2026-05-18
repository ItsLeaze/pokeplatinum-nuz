#!/usr/bin/env python3

import json
from collections import defaultdict

# ============================================================================
# CONFIG
# ============================================================================

COMPILED_DATA_FILE = "compiled_battle_data.json"

# Optional type filter:
# None -> include all Pokémon
# Example: "TYPE_FIRE"
TYPE_FILTER = "TYPE_DARK"

ALWAYS_INCLUDE_POKEMON = {
    "turtwig",
    "chimchar",
    "piplup",
    "bulbasaur",
    "charmander",
    "squirtle",
    "chikorita",
    "cyndaquil",
    "totodile",
    "treecko",
    "mudkip",
    "torchic",
    
    "corphish"
}

LEVEL_CAPS = {
    "Roark": 16,
    "Gardenia": 25,
    "Fantina": 30,
    "Maylene": 38,
    "Wake": 44,
    "Byron": 50,
    "Candice": 60,
    "Volkner": 70,
    "E4": 80
}

# ============================================================================
# EXAMPLE GYM ENCOUNTER ROUTES
# Fill these with your actual hardcore nuzlocke routing later
# ============================================================================

GYM_ENCOUNTERS = {
    "Roark": [
        "starter",
        "encounters_route_201",
        "encounters_lake_verity_low_water",
        "encounters_lake_verity",
        "encounters_route_202",
        "jubilife_briefcase",
        "encounters_route_203",
        "encounters_twinleaf_town",
        "encounters_oreburgh_gate_1f",
        "encounters_oreburgh_gate_b1f",
        "oreburgh_gift",
        "encounters_route_207",
        "encounters_oreburgh_mine_b1f",
        "encounters_oreburgh_mine_b2f",
    ],

    "Gardenia": [
        "encounters_route_204_south",
        "encounters_ravaged_path",
        "encounters_route_204_north",
        "floaroma_briefcase",
        "honey_tree_common",
        "honey_tree_uncommon",
        "encounters_valley_windworks_outside",
        "encounters_route_205_south",
        "encounters_eterna_forest",
        "encounters_route_205_north",
        "encounters_route_211_west",
        "encounters_mt_coronet_1f_north_room_1",
        "encounters_route_211_east",
        "eterna_trade",
    ],

    "Fantina": [
        "encounters_old_chateau_back_east_room",
        # "encounters_old_chateau_back_middle_east_room",
        # "encounters_old_chateau_back_middle_room",
        # "encounters_old_chateau_back_middle_west_room",
        # "encounters_old_chateau_back_west_room",
        # "encounters_old_chateau_corridor",
        # "encounters_old_chateau_dining_area",
        # "encounters_old_chateau",
        # "encounters_old_chateau_side_rooms",
        "encounters_route_206",
        "eterna_gift",
        "fossils_1",
        "encounters_wayward_cave_1f",
        "encounters_wayward_cave_b1f",
        "encounters_route_208",
        "hearthome_gift",
    ],

    "Maylene": [
        "encounters_route_209",
        "encounters_route_209_lost_tower_1f",
        # "encounters_route_209_lost_tower_2f",
        # "encounters_route_209_lost_tower_3f",
        # "encounters_route_209_lost_tower_4f",
        # "encounters_route_209_lost_tower_5f",
        "encounters_route_210_south",
        "cafe_briefcase",
        "encounters_route_215",
        "veilstone_briefcase",
        "veilstone_gift",
    ],
    
    "Wake": [
        "encounters_route_214",
        "encounters_maniac_tunnel",
        "encounters_ruin_maniac_cave_long",
        "encounters_ruin_maniac_cave_short",
        "encounters_valor_lakefront",
        "encounters_route_213",
        "encounters_great_marsh_1", # I think?
        "encounters_great_marsh_2",
        "encounters_great_marsh_3",
        "encounters_great_marsh_4",
        "encounters_great_marsh_5",
        "encounters_great_marsh_6",
        # "encounters_great_marsh_lookout",
        "encounters_route_212_south",
        "encounters_route_212_north",
        "encounters_trophy_garden",
    ],

    "Byron": [
        "encounters_route_210_north",
        "encounters_fuego_ironworks_outside",
        "encounters_route_219",
        "encounters_route_220",
        "encounters_route_221",
        "encounters_route_218",
        "honey_tree_rare",
        "encounters_iron_island_1f",
        "encounters_iron_island_b1f_left_room",
        "encounters_iron_island_b1f_right_room",
        "encounters_iron_island_b2f_left_room",
        "encounters_iron_island_b2f_right_room",
        "encounters_iron_island_b3f",
        "encounters_iron_island",
        "iron_island_gift",
    ],

    "Candice": [
        "encounters_lake_valor",
        "encounters_route_216",
        "encounters_route_217",
        "encounters_acuity_lakefront",
        "snowpoint_trade",
    ],

    "Volkner": [
        "encounters_lake_acuity",
        "encounters_sendoff_spring",
        "encounters_route_222",
        "encounters_route_223",
    ],

    "E4": [
        "encounters_route_224",
        "encounters_victory_road_1f",
        "encounters_victory_road_1f_room_1",
        "encounters_victory_road_1f_room_2",
        "encounters_victory_road_1f_room_3",
        "encounters_victory_road_2f",
        "encounters_victory_road_b1f",
    ]
}

# ============================================================================
# HELPERS
# ============================================================================

def load_data():
    with open(COMPILED_DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_best_ability_power(move):
    """
    Uses the strongest possible ability result.
    """

    effective_power = move.get("effective_power", {})

    if not effective_power:
        return 0

    return max(effective_power.values())


def evolve_pokemon_if_possible(species, level, pokemon_db):
    results = set()

    def recurse(current_species):

        pokemon = pokemon_db.get(current_species)

        if not pokemon:
            results.add(current_species)
            return

        valid_evolutions = []

        for evo in pokemon.get("evolutions", []):

            evo_level = evo.get("level", 100)

            if level >= evo_level:
                valid_evolutions.append(evo["target"])

        if not valid_evolutions:
            results.add(current_species)
            return

        for evolved_species in valid_evolutions:
            recurse(evolved_species)

    recurse(species)

    return sorted(results)


def get_available_moves(pokemon, level):
    """
    Returns all level-up moves available at the given level,
    deduplicated so each move appears only once.

    If a move is learned multiple times, we keep the earliest (lowest level) entry.
    """

    best_by_move = {}

    for move in pokemon.get("moves", []):

        if move["level"] > level:
            continue

        move_name = move["move"]

        if (
            move_name not in best_by_move
            or move["level"] < best_by_move[move_name]["level"]
        ):
            best_by_move[move_name] = move

    return list(best_by_move.values())


def get_top_moves(pokemon, level, top_n=2):
    available_moves = get_available_moves(pokemon, level)

    ranked = sorted(
        available_moves,
        key=get_best_ability_power,
        reverse=True
    )

    if not ranked:
        return []

    strongest_power = get_best_ability_power(ranked[0])
    minimum_power = strongest_power / 2

    filtered = [
        move
        for move in ranked
        if get_best_ability_power(move) >= minimum_power
    ]

    return filtered[:top_n]


def safe_int(value, default=0):
    if value is None:
        return default
    return int(value)


# ============================================================================
# MAIN ANALYSIS
# ============================================================================

def main():

    data = load_data()

    pokemon_db = data["pokemon"]
    encounters_db = data["encounters"]

    unlocked_locations = []

    for gym_name, new_locations in GYM_ENCOUNTERS.items():

        level_cap = LEVEL_CAPS[gym_name]

        evolved_always_include = set()
        for species in ALWAYS_INCLUDE_POKEMON:
            evolved_always_include.update(
                evolve_pokemon_if_possible(
                    species,
                    level_cap,
                    pokemon_db
                )
            )

        # Add newly unlocked locations
        unlocked_locations.extend(new_locations)

        print()
        print("=" * 80)
        print(f"{gym_name.upper()} ENCOUNTERS (Level Cap {level_cap})")
        print("=" * 80)

        delayed_good_rod_encounters = set()
        delayed_surf_encounters = set()
        delayed_super_rod_encounters = set()
        obtainable = set()

        # ------------------------------------------------------------------
        # Gather encounters from ALL unlocked locations
        # ------------------------------------------------------------------
        for location in unlocked_locations:
            
            if location not in encounters_db:
                continue

            encounter_data = encounters_db[location]

            for category in ["land", "surf", "old_rod", "good_rod", "super_rod"]:
                for encounter in encounter_data.get(category, []):
                    evolved_species_list = evolve_pokemon_if_possible(
                        encounter["species"],
                        level_cap,
                        pokemon_db
                    )

                    if category == "good_rod" and level_cap <= 30:
                        delayed_good_rod_encounters.update(evolved_species_list)
                    if category == "surf" and level_cap <= 44:
                        delayed_surf_encounters.update(evolved_species_list)
                    if category == "super_rod" and level_cap <= 80:
                        delayed_super_rod_encounters.update(evolved_species_list)
                    else:
                        obtainable.update(evolved_species_list)

        if level_cap > 30:
            obtainable = obtainable.union(delayed_good_rod_encounters)
        if level_cap > 44:
            obtainable = obtainable.union(delayed_surf_encounters)
        if level_cap > 80:
            obtainable = obtainable.union(delayed_super_rod_encounters)

        rankings = []

        # ------------------------------------------------------------------
        # Analyze Pokémon
        # ------------------------------------------------------------------

        for species in sorted(obtainable):
            pokemon = pokemon_db.get(species)

            if not pokemon:
                continue

            # --------------------------------------------------------------
            # Type filter
            # --------------------------------------------------------------

            if TYPE_FILTER is not None:
                matches_type = TYPE_FILTER in pokemon.get("types", [])
                always_include = species in evolved_always_include

                if not matches_type and not always_include:
                    continue

            top_moves = get_top_moves(
                pokemon,
                level_cap,
                top_n= 2 if level_cap < 20 else (3 if level_cap < 80 else 4)
            )

            for move in top_moves:
                best_ability = None

                for ability, power in move.get("effective_power", {}).items():

                    if best_ability is None or power > safe_int(best_ability["power"]):
                        best_ability = {
                            "pokemon": species,
                            "level": level_cap,
                            "move": move["move"],
                            "ability_used": ability,
                            "power": power,
                            "accuracy": move["accuracy"],
                            "type": move["type"],
                            "class": move["class"]
                        }

                rankings.append(best_ability)

        # ------------------------------------------------------------------
        # Print rankings
        # ------------------------------------------------------------------

        rankings.sort(
            key=lambda x: x["power"],
            reverse=True
        )

        for i, entry in enumerate(rankings, start=1):

            print(
                f"{i:3}. "
                f"{entry['pokemon']:15} "
                f"Lv{entry['level']:2} | "
                f"{entry['move']:20} | "
                f"Power {entry['power']:7.2f} | "
                f"Acc {entry['accuracy']:3}"
            )


if __name__ == "__main__":
    main()