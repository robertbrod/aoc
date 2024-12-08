import os

scaffolding = """# Advent of Code {year} - Day {day}

def solve_part_one(input):
    return 0

def solve_part_two(input):
    return 0
"""

def create_input_dirs(year):
    print(f"Creating directories for AoC {year}!")
    
    for i in range(1, 26, 1):
        try:
            path = f"{year}/{i}"
            os.makedirs(path)
            
            with open(f"{year}/{i}/solution.py", "w") as file:
                file.write(scaffolding.format(year = year, day = i))
        except Exception as error:
            print(f"Skipping directory creation: {path}")
            
def cache_input(data, year, day):
    with open(f"{year}/{day}/{year}_{day}_input.txt", "w") as file:
        file.write(data)
        
def fetch_input(year, day):
    with open(f"{year}/{day}/{year}_{day}_input.txt", "r") as file:
        return file.read()
    
def fetch_sample_input(year, day):
    with open(f"{year}/{day}/sample_input.txt", "r") as file:
        return file.read()
    
def in_bounds(x, y, width, height):
    """
    Check if a particular coord is within the bounds of a 2D structure

    Args:
        x (int): X coord
        y (int): Y coord
        width (int): width of 2D structure
        height (int): height of 2D structure

    Returns:
        bool: The result of the check.

    Raises:
        None
    """

    return 0 <= x < width and 0 <= y < height