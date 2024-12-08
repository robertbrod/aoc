# Advent of Code 2024 - Day 8

import util

def parse_input(input):
    frequency_map = {}
    for row_index, row in enumerate(input):
        for col_index, char in enumerate(row):
            if char != '.':
                if frequency_map.get(char) == None:
                    frequency_map[char] = [(row_index, col_index)]
                else:
                    frequency_map[char].append((row_index, col_index))

    return frequency_map, len(input[0]), len(input) 

def solve_part_one(input):
    antinodes = set()

    frequency_map, width, height = parse_input(input)

    for frequency in frequency_map:
        coords = frequency_map[frequency]
        for index in range(len(coords)):
            coord = coords[index]
            filtered_coords = coords[:index] + coords[index + 1:]
            for filtered_coord in filtered_coords:
                dx = filtered_coord[0] - coord[0]
                dy = filtered_coord[1] - coord[1]
                antinode_one = (filtered_coord[0] + dx, filtered_coord[1] + dy)
                antinode_two = (coord[0] + (-1 * dx), coord[1] + (-1 * dy))
                if util.in_bounds(antinode_one[0], antinode_one[1], width, height):
                    antinodes.add(antinode_one)
                if util.in_bounds(antinode_two[0], antinode_two[1], width, height):
                    antinodes.add(antinode_two)

    return len(antinodes)

def solve_part_two(input):
    antinodes = set()

    frequency_map, width, height = parse_input(input)

    for frequency in frequency_map:
        coords = frequency_map[frequency]
        for index in range(len(coords)):
            coord = coords[index]
            antinodes.add(coord)
            filtered_coords = coords[:index] + coords[index + 1:]
            for filtered_coord in filtered_coords:
                dx = filtered_coord[0] - coord[0]
                dy = filtered_coord[1] - coord[1]
                antinode_x, antinode_y = filtered_coord[0] + dx, filtered_coord[1] + dy
                while util.in_bounds(antinode_x, antinode_y, width, height):
                    antinodes.add((antinode_x, antinode_y))
                    antinode_x, antinode_y = antinode_x + dx, antinode_y + dy

                dx *= -1
                dy *= -1
                antinode_x, antinode_y = coord[0] + dx, coord[1] + dy
                while util.in_bounds(antinode_x, antinode_y, width, height):
                    antinodes.add((antinode_x, antinode_y))
                    antinode_x, antinode_y = antinode_x + dx, antinode_y + dy

    return len(antinodes)
