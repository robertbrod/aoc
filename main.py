import aoc_gateway
import util
import os

# ---------- CONSTANTS ----------

YEAR = 2023
DAY = 1
PART = 1

# ---------- Yearly helpers ----------

if not os.path.exists(f"{YEAR}/"):
    util.create_input_dirs(YEAR)
else:
    print("Skipping yearly helper for creating directories; it should already exist!")

# ---------- Puzzle input ----------

try:
    # Fetch input data from Advent of Code website and cache on disk
    data = aoc_gateway.fetch_input(YEAR, DAY)
    util.cache_input_data(data, YEAR, DAY)
except Exception as error:
    print(error)