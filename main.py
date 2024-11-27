import aoc_gateway
import importlib
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

# ---------- Puzzle ----------

try:
    # Fetch input data from Advent of Code website and cache on disk
    data = aoc_gateway.fetch_input(YEAR, DAY)
    util.cache_input_data(data, YEAR, DAY)
    
    module_name = f"{YEAR}.{DAY}.solution"
    solution_module = importlib.import_module(module_name)

    part_one_result = solution_module.solve_part_one(data)
    part_two_result = solution_module.solve_part_two(data)
except ModuleNotFoundError:
    print(f"Solution for {YEAR} day {DAY} not found")
except Exception as error:
    print(error)