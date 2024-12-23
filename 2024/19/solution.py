# Advent of Code 2024 - Day 19

import functools

def parse_input(input):
    towels, desired_patterns = [], []
    
    for index, line in enumerate(input):
        if index == 0:
            towels = line.replace(" ", "")
        elif line:
            desired_patterns.append(line)       
            
    return towels, desired_patterns 

def get_potential_next_designs(towels, target):
    potential_next_designs = []
    for towel in towels.split(','):
        substring_length = len(towel)
        if target[:substring_length] == towel:
            potential_next_designs.append(towel)
            
    return potential_next_designs

@functools.cache
def is_pattern_possible(towels, desired_pattern, index, current_pattern):
    if index == len(desired_pattern):
        return current_pattern == desired_pattern
    
    potential_next_designs = get_potential_next_designs(towels, desired_pattern[index:])
    for design in potential_next_designs:
        if is_pattern_possible(towels, desired_pattern, index + len(design), current_pattern + design):
            return True
        
    return False

def solve_part_one(input):
    towels, desired_patterns = parse_input(input)
    
    possible_designs = 0
    for desired_pattern in desired_patterns:
        if is_pattern_possible(towels, desired_pattern, 0, ""):
            possible_designs += 1
            
    return possible_designs

def solve_part_two(input):
    return None
