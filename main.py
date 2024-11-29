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

response = None

try:
    # Fetch input data from Advent of Code website and cache on disk
    response = aoc_gateway.fetch_input(YEAR, DAY)
    util.cache_input(response, YEAR, DAY)
except Exception as error:
    print(error)
    
try:
    # Dynamically fetch the appropriate solution module
    module_name = f"{YEAR}.{DAY}.solution"
    solution_module = importlib.import_module(module_name)
except ModuleNotFoundError:
    print(f"Solution for {YEAR} day {DAY} not found")

input_data_str = util.fetch_input(YEAR, DAY)
input_data = input_data_str.splitlines()
part_one_result = solution_module.solve_part_one(input_data)
# part_two_result = solution_module.solve_part_two(input_data)

print(part_one_result)