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

def get_vector(direction):
    if direction == Direction.NORTH:
        return 0, -1
    if direction == Direction.EAST:
        return 1, 0
    if direction == Direction.SOUTH:
        return 0, 1
    if direction == Direction.WEST:
        return -1, 0

def in_map(room_map, next_pos_y, next_pos_x):
    if (next_pos_y >= 0 and next_pos_y < len(room_map)) and (next_pos_x >= 0 and next_pos_x < len(room_map[0])):
        return True

    return False

def parse_input(input):
    room_map = []
    guard_x = -1
    guard_y = -1

    for y, line in enumerate(input):
        line_map = []
        for x, char in enumerate(line):
            if char == '^':
                guard_x = x
                guard_y = y
                line_map.append('.')
            else:
                line_map.append(char)
        room_map.append(line_map)
    
    return room_map, guard_x, guard_y

def solve_part_one(input):
    room_map, guard_x, guard_y = parse_input(input)
    direction = Direction.NORTH
    visited_coords = set()
    visited_coords.add((guard_x, guard_y))
    in_room = True

    while in_room:
        dx, dy = get_vector(direction)
        next_pos_x, next_pos_y = guard_x + dx, guard_y + dy
        if in_map(room_map, next_pos_y, next_pos_x):
            next_pos_cell = room_map[next_pos_y][next_pos_x]
            if next_pos_cell == '#':
                direction = turn_right(direction)
                continue
            else:
                guard_x = next_pos_x
                guard_y = next_pos_y
                visited_coords.add((guard_x, guard_y))
        else:
            in_room = False

    return len(visited_coords)

def solve_part_two(input):
    loops = 0
    room_map, guard_x, guard_y = parse_input(input)
    orig_guard_x, orig_guard_y = guard_x, guard_y
    direction = Direction.NORTH
    visited_coords = set()
    visited_coords.add((guard_x, guard_y))
    in_room = True

    while in_room:
        dx, dy = get_vector(direction)
        next_pos_x, next_pos_y = guard_x + dx, guard_y + dy
        if in_map(room_map, next_pos_y, next_pos_x):
            next_pos_cell = room_map[next_pos_y][next_pos_x]
            if next_pos_cell == '#':
                direction = turn_right(direction)
                continue
            else:
                guard_x = next_pos_x
                guard_y = next_pos_y
                visited_coords.add((guard_x, guard_y))
        else:
            in_room = False

    # Now that we have the traveled path, lets add obstacles and see if we get in a loop
    for coords in visited_coords:
        new_obstacle_x = coords[0]
        new_obstacle_y = coords[1]
        room_map[new_obstacle_y][new_obstacle_x] = '#'
        
        # Reset state
        direction = Direction.NORTH
        guard_x, guard_y = orig_guard_x, orig_guard_y
        in_room = True

        # Loop conditions: If we end up at these coords, in this direction, we are in a loop
        state_set = set()
        state_set.add((guard_x, guard_y, direction))
        
        while in_room:
            dx, dy = get_vector(direction)
            next_pos_x, next_pos_y = guard_x + dx, guard_y + dy
            
            if in_map(room_map, next_pos_y, next_pos_x):
                next_pos_cell = room_map[next_pos_y][next_pos_x]
                if next_pos_cell == '#':
                    direction = turn_right(direction)
                    continue
                else:
                    guard_x = next_pos_x
                    guard_y = next_pos_y
                    state = (guard_x, guard_y, direction)
                    
                    if state in state_set:
                        loops += 1
                        break
                    else:
                        state_set.add(state)
            else:
                in_room = False

        room_map[new_obstacle_y][new_obstacle_x] = '.'

    return loops
