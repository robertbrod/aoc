# Advent of Code 2024 - Day 19

def parse_input(input):
    towels, desired_patterns = [], []
    
    for index, line in enumerate(input):
        if index == 0:
            towels = line.replace(" ", "").split(',')
        elif line:
            desired_patterns.append(line)       
            
    return towels, desired_patterns 

def solve_part_one(input):
    towels, desired_patterns = parse_input(input)
    
    return None

def solve_part_two(input):
    return None
