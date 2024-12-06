# Advent of Code 2024 - Day 6

from enum import Enum

class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

def turn_right(direction):
    if direction == Direction.NORTH:
        return Direction.EAST
    if direction == Direction.EAST:
        return Direction.SOUTH
    if direction == Direction.SOUTH:
        return Direction.WEST
    if direction == Direction.WEST:
        return Direction.NORTH

def parse_input(input):
    room_map = []
    guard_x = -1
    guard_y = -1

    for y, line in enumerate(input):
        line_map = []
        for x, char in enumerate(line):
            line_map.append(char)
            if char == '^':
                guard_x = x
                guard_y = y
        room_map.append(line_map)
    
    return room_map, guard_x, guard_y

def solve_part_one(input):
    room_map, guard_x, guard_y = parse_input(input)
    visited_coords = set()

def solve_part_two(input):
    return 0
