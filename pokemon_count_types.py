import csv
from collections import defaultdict

INPUT_CSV = "pokemon.csv"

type_counts = defaultdict(int)

with open(INPUT_CSV, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        t1 = row["type1"]
        t2 = row["type2"]

        # Use a set to avoid counting mono-types twice
        unique_types = {t1, t2}

        for t in unique_types:
            if t:  # ignore empty just in case
                type_counts[t] += 1

# Print results sorted alphabetically
for t in sorted(type_counts):
    print(f"{t}, {type_counts[t]}"), {t2}