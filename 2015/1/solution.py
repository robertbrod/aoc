
# Advent of Code 2015 - Day 1

def solve_part_one(input):
    floor = 0
    directions = input[0]
    
    for direction in directions:
        if direction == '(':
            floor += 1
        elif direction == ')':
            floor -= 1
        
    return floor

def solve_part_two(input):
    floor = 0
    directions = input[0]
    
    for position, direction in enumerate(directions):
        if direction == '(':
            floor += 1
        elif direction == ')':
            floor -= 1
            
        if floor == -1:
            return position + 1