import os
from models import Participant
import json

scaffolding = """
# Advent of Code {year} - Day {day}

def solve_part_one(input):
    return 0

def solve_part_two(input):
    return 0
"""

def create_daily_dirs(year: str) -> None:
    """
    Creates daily directories for the AoC year. This includes a parent directory `year` along with daily directories containing a scaffolded `solution.py`
    
    Args:
        year (str): AoC year
        
    Returns:
        None
        
    Raises:
        None

    """
    print(f"Creating daily directories for AoC {year}!")
    
    for i in range(1, 26, 1):
        try:
            path = f"{year}/{i}"
            os.makedirs(path)
            
            with open(f"{year}/{i}/solution.py", "w") as file:
                file.write(scaffolding.format(year = year, day = i))
        except Exception as error:
            print(f"Skipping directory creation: {path} ({error})")
            
def cache_input(data: str, year: str, day: str) -> None:
    """
    Writes puzzle input data to disk. Saves to `year/day/year_day_input.txt`

    Args:
        data (str): response from AoC API request
        year (str): puzzle year
        day (str): puzzle day

    Returns:
        None

    Raises:
        Exception
            Encountered error while writing to disk
    """
    
    print(f"Attempting to cache puzzle input...")
    
    try:
        with open(f"{year}/{day}/{year}_{day}_input.txt", "w") as file:
            file.write(data)
        
        print(f"Successfully cached puzzle input.")
    except Exception as error:
        print(f"Failed to cache puzzle input: {error}")
        
def cache_leaderboard(data: list[Participant]) -> None:
    """
    Writes private leaderboard data to disk. Saves to `leaderboard.txt`

    Args:
        data (str): Parsed response from AoC API

    Returns:
        None

    Raises:
        Exception
            Encountered error while writing to disk
    """
    
    print(f"Attempting to cache private leaderboard data...")
    
    participant_data = [participant.to_json() for participant in data]
    
    try:
        with open("leaderboard.txt", "w") as file:
            json.dump(participant_data, file, indent = 4)
            
        print(f"Successfully cached private leaderboard data.")
    except Exception as error:
        print(f"Failed to cache puzzle input: {error}")
        
def fetch_input(year: str, day: str) -> str:
    """
    Reads puzzle input from file. File must exist at `year/day/year_day_input.txt`

    Args:
        year (str): puzzle year
        day (str): puzzle day

    Returns:
        str: The contents of the file

    Raises:
        FileNotFoundError
            File does not exist
    """
    
    print(f"Attempting to fetch cached puzzle input...")
    
    try:
        with open(f"{year}/{day}/{year}_{day}_input.txt", "r") as file:
            print(f"Successfully fetched cached puzzle input.")
            return file.read()
    except FileNotFoundError:
        print(f"{year}/{day}/{year}_{day}_input.txt not found.")
        
def fetch_leaderboard() -> list[Participant]:
    """
    Reads private leaderboard data from file. File must exist at `leaderboard.txt`

    Args:
        None

    Returns:
        list[Participant]: List of participant data

    Raises:
        FileNotFoundError
            File does not exist
        JSONDecodeError
            Fle contains malformed JSON data
    """
    
    print("Attempting to fetch cached private leaderboard data...")
    
    try:
        with open("leaderboard.txt", "r") as file:
            data = json.load(file)
            
        print("Successfully fetched cached private leaderboard data.")
        return [Participant.load(participant) for participant in data]
    except FileNotFoundError:
        print(f"leaderboard.txt not found. Returning an empty list.")
        return []
    except json.JSONDecodeError:
        print(f"leaderboard.txt contains invalid JSON. Returning an empty list.")
    
def fetch_sample_input(year: str, day: str) -> str:
    """
    Reads sample puzzle input from file. This typically is copy-pasted directly from AoC problem description. File must exist at `year/day/sample_input.txt`

    Args:
        year (str): puzzle year
        day (str): puzzle day

    Returns:
        str: The contents of the file

    Raises:
        None
    """
    
    print(f"Attempting to fetch sample puzzle input...")
    
    try:
        with open(f"{year}/{day}/sample_input.txt", "r") as file:
            print("Successfully fetched cached sample puzzle input.")
            return file.read()
    except Exception as error:
        print(f"Failed to fetch sample puzzle input: {error}")
    
def in_bounds_2d(x: int, y: int, width: int, height: int) -> bool:
    """
    Check if a particular coord is within the bounds of a 2D list

    Args:
        x (int): X coord
        y (int): Y coord
        width (int): width of 2D list
        height (int): height of 2D list

    Returns:
        bool: The result of the check.

    Raises:
        None
    """

    return 0 <= x < width and 0 <= y < height

def in_bounds(index: int, length: int) -> bool:
    """
    Check if a particular index is within the bounds of a list

    Args:
        index (int): index of list
        length (int): length of list

    Returns:
        bool: The result of the check.

    Raises:
        None
    """

    return 0 <= index <= length
