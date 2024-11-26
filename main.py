import aoc_gateway
import yearly_helper
from datetime import datetime
import os

# ---------- CONSTANTS ----------

YEAR = 2023
DAY = 1
PART = 1

# ---------- Yearly helpers ----------

if not os.path.exists(f"{datetime.now().year}/"):
    yearly_helper.create_input_dirs(YEAR)
else:
    print("Skipping yearly helper for creating directories; it should already exist!")

# ---------- Puzzle input ----------

try:
    # Fetch input data from Advent of Code website
    data = aoc_gateway.fetch_input(YEAR, DAY)

    # Cache input data
    with open(f"{YEAR}/{DAY}/{YEAR}_{DAY}_input.txt", "w") as file:
        file.write(data)
except Exception as error:
    print(error)

puzzle_input = 

