# Advent of Code 2024 - Day 17

def parse_input(input):
    registers = {}
    program = None
    
    for i, line in enumerate(input):
        if i == 0:
            registers['A'] = int(line.split(':')[1])
        elif i == 1:
            registers['B'] = int(line.split(':')[1])
        elif i == 2:
            registers['C'] = int(line.split(':')[1])
        elif i == 4:
            program = list(map(int, line.split(':')[1].strip().split(',')))
        
    return registers, program

def solve_part_one(input):
    registers, program = parse_input(input)
    
    return None

def solve_part_two(input):
    return None
