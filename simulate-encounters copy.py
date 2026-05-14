#!/usr/bin/env python3

"""
Pokemon Platinum Decomp Encounter Simulator
===========================================

Simulates Hardcore Nuzlocke first encounters across a sequence of maps.

Rules implemented:
- Encounter locations are processed in order.
- Encounter methods are attempted in a configurable priority order.
- Already caught Pokemon species are excluded from future encounters.
- If an encounter method has no valid species left, the next method is tried.
- SPECIES_NONE entries are ignored.
- Swarms/day/night/radar/version-exclusive encounters are ignored.
- Uses the exact slot probabilities from Platinum's encounter code.

Outputs:
- How often each Pokemon was obtained across all simulations.
- Per-location encounter statistics.
- Catch percentages.

Usage:
    python encounter_sim.py

Adjust the CONFIG section below.
"""

import json
import random
from pathlib import Path
from collections import Counter, defaultdict

# ============================================================
# CONFIG
# ============================================================

# Folder containing encounter JSON files
ENCOUNTER_DIR = Path("res/field/encounters")

# Ordered list of encounter files to process
LOCATION_FILES = [
    "encounters_route_201.json",
    "encounters_lake_verity_low_water.json",
    # "encounters_lake_verity.json",
    "encounters_route_202.json",
    "encounters_route_203.json",
    "encounters_twinleaf_town.json",
    "encounters_oreburgh_gate_1f.json",
    # "encounters_oreburgh_gate_b1f.json",
    "encounters_route_207.json",
    "encounters_oreburgh_mine_b1f.json",
    # "encounters_oreburgh_mine_b2f.json",

    ########### ROARK ###########
    "encounters_route_204_south.json",
    "encounters_ravaged_path.json",
    # "encounters_route_204_north.json",
    "encounters_valley_windworks_outside.json",
    "encounters_route_205_south.json",
    "encounters_eterna_forest.json",
    # "encounters_route_205_north.json",
    "encounters_route_211_west.json",
    "encounters_mt_coronet_1f_north_room_1.json",
    # "encounters_route_211_east.json",

    ########### GARDENIA ###########
    "encounters_old_chateau_back_east_room.json",
    # "encounters_old_chateau_back_middle_east_room.json",
    # "encounters_old_chateau_back_middle_room.json",
    # "encounters_old_chateau_back_middle_west_room.json",
    # "encounters_old_chateau_back_west_room.json",
    # "encounters_old_chateau_corridor.json",
    # "encounters_old_chateau_dining_area.json",
    # "encounters_old_chateau.json",
    # "encounters_old_chateau_side_rooms.json",
    "encounters_route_206.json",
    "encounters_wayward_cave_1f.json",
    # "encounters_wayward_cave_b1f.json"
    "encounters_route_208.json",

    ########### FANTINA ###########
    "encounters_route_209.json",
    "encounters_route_209_lost_tower_1f.json",
    # "encounters_route_209_lost_tower_2f.json",
    # "encounters_route_209_lost_tower_3f.json",
    # "encounters_route_209_lost_tower_4f.json",
    # "encounters_route_209_lost_tower_5f.json",
    "encounters_route_210_south.json",
    "encounters_route_215.json",

    ########### MAYLENE ###########
    "encounters_route_214.json",
    "encounters_maniac_tunnel.json",
    # "encounters_ruin_maniac_cave_long.json",
    # "encounters_ruin_maniac_cave_short.json",
    "encounters_valor_lakefront.json",
    "encounters_route_213.json",
    "encounters_great_marsh_1.json", # I think?
    # "encounters_great_marsh_2.json",
    # "encounters_great_marsh_3.json",
    # "encounters_great_marsh_4.json",
    # "encounters_great_marsh_5.json",
    # "encounters_great_marsh_6.json",
    # "encounters_great_marsh_lookout.json",
    "encounters_route_212_south.json",
    # "encounters_route_212_north.json",
    "encounters_trophy_garden.json",

    ########### WAKE ###########
    # "encounters_route_210_north.json",
    "encounters_fuego_ironworks_outside.json",
    "encounters_route_219.json",
    "encounters_route_220.json",
    "encounters_route_221.json",
    "encounters_route_218.json",
    "encounters_iron_island_1f.json",
    # "encounters_iron_island_b1f_left_room.json",
    # "encounters_iron_island_b1f_right_room.json",
    # "encounters_iron_island_b2f_left_room.json",
    # "encounters_iron_island_b2f_right_room.json",
    # "encounters_iron_island_b3f.json",
    # "encounters_iron_island.json",

    ########### BYRON ###########
    "encounters_lake_valor.json",
    "encounters_route_216.json",
    "encounters_route_217.json",
    "encounters_acuity_lakefront.json",

    ########### CANDICE ###########
    "encounters_lake_acuity.json",
    "encounters_sendoff_spring.json",
    "encounters_route_222.json",
    "encounters_route_223.json",

    ########### VOLKNER ###########
    "encounters_route_224.json",
    "encounters_victory_road_1f.json",
    # "encounters_victory_road_1f_room_1.json",
    # "encounters_victory_road_1f_room_2.json",
    # "encounters_victory_road_1f_room_3.json",
    # "encounters_victory_road_2f.json",
    # "encounters_victory_road_b1f.json",

    ########### POSTGAME ###########
    # "encounters_route_225.json",
    # "encounters_route_226.json",
    # "encounters_route_227.json",
    # "encounters_route_228.json",
    # "encounters_route_229.json",
    # "encounters_route_230.json",

    ##### not sure about timing, but for now irrelevant #####
    # "encounters_mt_coronet_1f_north_room_2.json",
    # "encounters_mt_coronet_1f_south.json",
    # "encounters_mt_coronet_1f_tunnel_room.json",
    # "encounters_mt_coronet_2f.json",
    # "encounters_mt_coronet_3f.json",
    # "encounters_mt_coronet_4f_room_3.json",
    # "encounters_mt_coronet_4f_rooms_1_and_2.json",
    # "encounters_mt_coronet_5f.json",
    # "encounters_mt_coronet_6f.json",
    # "encounters_mt_coronet_b1f.json",
    # "encounters_mt_coronet_outside_north.json",
    # "encounters_mt_coronet_outside_south.json",
]

# Encounter method priority
# Methods are attempted in order until a valid encounter exists.
ENCOUNTER_METHOD_ORDER = [
    "land",
    "surf",
    "old_rod",
    "good_rod",
    "super_rod",
]

# Number of full game simulations
SIMULATION_COUNT = 10000

# ============================================================
# SLOT PROBABILITIES
# ============================================================

GROUND_SLOT_WEIGHTS = [
    20,  # slot 0
    20,  # slot 1
    10,  # slot 2
    10,  # slot 3
    10,  # slot 4
    10,  # slot 5
    5,   # slot 6
    5,   # slot 7
    4,   # slot 8
    4,   # slot 9
    1,   # slot 10
    1,   # slot 11
]

WATER_SLOT_WEIGHTS = [
    60,
    30,
    5,
    4,
    1,
]

OLD_ROD_WEIGHTS = [
    60,
    30,
    5,
    4,
    1,
]

GOOD_ROD_WEIGHTS = [
    40,
    40,
    15,
    4,
    1,
]

SUPER_ROD_WEIGHTS = [
    40,
    40,
    15,
    4,
    1,
]

# ============================================================
# ENCOUNTER TABLE MAPPING
# ============================================================

METHOD_INFO = {
    "land": {
        "table": "land_encounters",
        "weights": GROUND_SLOT_WEIGHTS,
    },
    "surf": {
        "table": "surf_encounters",
        "weights": WATER_SLOT_WEIGHTS,
    },
    "old_rod": {
        "table": "old_rod_encounters",
        "weights": OLD_ROD_WEIGHTS,
    },
    "good_rod": {
        "table": "good_rod_encounters",
        "weights": GOOD_ROD_WEIGHTS,
    },
    "super_rod": {
        "table": "super_rod_encounters",
        "weights": SUPER_ROD_WEIGHTS,
    },
}

# ============================================================
# HELPERS
# ============================================================

def weighted_choice(entries, weights):
    """
    entries: list of encounter dicts
    weights: corresponding slot weights
    """
    return random.choices(entries, weights=weights, k=1)[0]


def load_encounter_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_valid_encounters(encounter_data, method, caught_species):
    """
    Returns:
        (valid_entries, valid_weights)
    """

    info = METHOD_INFO[method]

    table_name = info["table"]
    weights = info["weights"]

    if table_name not in encounter_data:
        return [], []

    encounter_table = encounter_data[table_name]

    valid_entries = []
    valid_weights = []

    for i, entry in enumerate(encounter_table):
        if i >= len(weights):
            break

        species = entry["species"]

        if species == "SPECIES_NONE":
            continue

        if species in caught_species:
            continue

        valid_entries.append(entry)
        valid_weights.append(weights[i])

    return valid_entries, valid_weights


def simulate_location(encounter_data, caught_species):
    """
    Attempts encounter methods in configured order.

    Returns:
        encountered_species or None
    """

    for method in ENCOUNTER_METHOD_ORDER:
        valid_entries, valid_weights = get_valid_encounters(
            encounter_data,
            method,
            caught_species
        )

        if not valid_entries:
            continue

        chosen = weighted_choice(valid_entries, valid_weights)
        species = chosen["species"]

        caught_species.add(species)

        return species

    return None


# ============================================================
# MAIN SIMULATION
# ============================================================

def main():
    overall_species_counter = Counter()

    # Optional: per-location statistics
    per_location_counter = defaultdict(Counter)

    for sim in range(SIMULATION_COUNT):
        caught_species = set()

        for location_file in LOCATION_FILES:
            path = ENCOUNTER_DIR / location_file

            encounter_data = load_encounter_file(path)

            species = simulate_location(encounter_data, caught_species)

            if species is not None:
                overall_species_counter[species] += 1
                per_location_counter[location_file][species] += 1

    # ========================================================
    # OUTPUT
    # ========================================================

    print()
    print("===================================================")
    print(f"SIMULATIONS: {SIMULATION_COUNT}")
    print("===================================================")
    print()

    print("OVERALL ENCOUNTER COUNTS")
    print("------------------------")

    sorted_species = sorted(
        overall_species_counter.items(),
        key=lambda x: (-x[1], x[0])
    )

    for species, count in sorted_species:
        percentage = (
            count / SIMULATION_COUNT
        ) * 100

        print(
            f"{species:<30} "
            f"{count:>8} "
            f"({percentage:6.2f}%)"
        )

    print()
    print("===================================================")
    print("PER-LOCATION STATS")
    print("===================================================")

    for location_file in LOCATION_FILES:
        print()
        print(location_file)
        print("-" * len(location_file))

        location_total = sum(
            per_location_counter[location_file].values()
        )

        sorted_location_species = sorted(
            per_location_counter[location_file].items(),
            key=lambda x: (-x[1], x[0])
        )

        for species, count in sorted_location_species:
            percentage = (
                count / SIMULATION_COUNT
            ) * 100

            print(
                f"{species:<30} "
                f"{count:>8} "
                f"({percentage:6.2f}%)"
            )

        if location_total == 0:
            print("No valid encounters.")

    print()
    print("Done.")


if __name__ == "__main__":
    main()
