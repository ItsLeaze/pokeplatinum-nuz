#!/usr/bin/env python3

"""
Print all level-up evolutions from the Pokemon data files.

Reads:
    res/pokemon/<pokemon>/data.json

Looks for evolutions of the form:
    [
        "EVO_LEVEL",
        <level>,
        "SPECIES_X"
    ]

Outputs:
    SPECIES_SNOVER 40 SPECIES_ABOMASNOW

Sorted by evolution level ascending.
"""

import json
from pathlib import Path

POKEMON_DIR = Path("res/pokemon")


def folder_to_species(folder_name):
    return f"SPECIES_{folder_name.upper()}"


def main():
    evolutions = []

    for pokemon_dir in POKEMON_DIR.iterdir():
        if not pokemon_dir.is_dir():
            continue

        data_file = pokemon_dir / "data.json"

        if not data_file.exists():
            continue

        source_species = folder_to_species(pokemon_dir.name)

        try:
            with open(data_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            evo_list = data.get("evolutions", [])

            for evo in evo_list:
                if len(evo) < 3:
                    continue

                evo_method = evo[0]

                # Only handle level evolutions
                if evo_method != "EVO_LEVEL":
                    continue

                level = evo[1]
                target_species = evo[2]

                evolutions.append((
                    level,
                    source_species,
                    target_species
                ))

        except Exception as e:
            print(f"[WARN] Failed reading {data_file}: {e}")

    # Sort by evolution level ascending
    evolutions.sort(key=lambda x: (x[0], x[1]))

    # Print result
    for level, source_species, target_species in evolutions:
        print(f"{source_species} {level} {target_species}")


if __name__ == "__main__":
    main()