import aoc_gateway
import importlib
import util
import os
import config_manager

def create_dirs():
    year = config_manager.get_state("year")
    
    # If this year's directory exists, we likely ran this successfully already.
    if not os.path.exists(f"{year}/"):
        util.create_input_dirs(year)

def fetch_input():
    year = config_manager.get_state("year")
    day = config_manager.get_state("day")
    
    try:
        response = aoc_gateway.fetch_input(year, day)
        util.cache_input(response, year, day)
    except Exception as error:
        print(error)

def run_solution():
    year = config_manager.get_state("year")
    day = config_manager.get_state("day")
    part = config_manager.get_state("part")
    
    # Dynamically fetch the appropriate solution module
    try:
        module_name = f"{year}.{day}.solution"
        solution_module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        print(f"Solution for {year} day {day} not found")
    
    input_data = util.fetch_input(year, day).splitlines()
    
    if part == 1:
        result = solution_module.solve_part_one(input_data)
        response = aoc_gateway.submit_answer(year, day, part, result)
        print(response)
    elif part == 2:
        result = solution_module.solve_part_two(input_data)
        response = aoc_gateway.submit_answer(year, day, part, result)
        print(response)
        
def display_leaderboard():
    participants = aoc_gateway.fetch_leaderboard()
    for participant in participants:
        position_str = "N/A " if participant.position == None else str(participant.position) + ') '
        print(f"{position_str:<5} {participant.name:<25} {str(participant.stars) + '★':<5}")

def main():
    display_leaderboard = config_manager.get_state("display_leaderboard")
    if display_leaderboard:  
        display_leaderboard()
    
    # Create scaffolded directories and solution files
    create_dirs()
    
    # Fetch input data from Advent of Code website and cache data on disk
    fetch_input()
    
    # Run solution!
    run_solution()

if __name__ == "__main__":
    main()