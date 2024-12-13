# Advent of Code 2024 - Day 12

import util

def parse_input(input):
    return [list(line) for line in input]

def get_neighbors(coords):
    neighbors = set()
    x = coords[0]
    y = coords[1]
    
    # up
    dx, dy = 0, -1
    neighbors.add((x + dx, y + dy))
    
    # right
    dx, dy = 1, 0
    neighbors.add((x + dx, y + dy))
    
    # down
    dx, dy = 0, 1
    neighbors.add((x + dx, y + dy))
    
    # left
    dx, dy = -1, 0
    neighbors.add((x + dx, y + dy))
    
    return neighbors

def flood_fill_one(garden, x, y, plot, visited):
    if (util.in_bounds_2d(x, y, len(garden[0]), len(garden)) == False) or ((x, y) in visited) or garden[y][x] != plot:
        return 0, 0
    
    visited.add((x, y))
    
    area = 1
    perimeter = 0
    
    neighbors = get_neighbors((x, y))
    for neighbor in neighbors:
        neighbor_x, neighbor_y = neighbor[0], neighbor[1]
        # Proceed with flood fill
        if util.in_bounds_2d(neighbor_x, neighbor_y, len(garden[0]), len(garden)) and garden[neighbor_y][neighbor_x] == plot:
            neighbor_area, neighbor_perimeter = flood_fill_one(garden, neighbor_x, neighbor_y, plot, visited)
            area += neighbor_area
            perimeter += neighbor_perimeter
        # Increment the perimeter if we moved out of bounds or into another region
        else:
            perimeter += 1
            
    return area, perimeter
    
def solve_part_one(input):
    total_price = 0
    garden = parse_input(input)
    
    visited = set()
    for x in range(len(garden[0])):
        for y in range(len(garden)):
            if (x, y) not in visited:
                area, perimeter = flood_fill_one(garden, x, y, garden[y][x], visited)
                total_price += (area * perimeter)

    return total_price

def flood_fill_two(garden, x, y, plot, visited, region):
    if (util.in_bounds_2d(x, y, len(garden[0]), len(garden)) == False) or ((x, y) in visited) or garden[y][x] != plot:
        return 0, 0
    
    visited.add((x, y))
    region.append((x, y))
    
    neighbors = get_neighbors((x, y))
    for neighbor in neighbors:
        neighbor_x, neighbor_y = neighbor[0], neighbor[1]
        if util.in_bounds_2d(neighbor_x, neighbor_y, len(garden[0]), len(garden)) and garden[neighbor_y][neighbor_x] == plot:
            flood_fill_two(garden, neighbor_x, neighbor_y, plot, visited, region)
            
    return region

def is_neighbor(point, garden_map, label):
    x, y = point[0], point[1]

    if util.in_bounds_2d(x, y, len(garden_map[0]), len(garden_map)) and garden_map[y][x] == label:
        return True
    
    return False

def solve_part_two(input):
    total_price = 0
    garden = parse_input(input)
    
    visited = set()
    regions = []
    for x in range(len(garden[0])):
        for y in range(len(garden)):
            if (x, y) not in visited:
                region = []
                flood_fill_two(garden, x, y, garden[y][x], visited, region)
                regions.append((garden[y][x], region))
    
    for region in regions:
        label, points = region
        area = len(points)
        corners = 0
        for point in points:
            x = point[0]
            y = point[1]

            # northwest vertex
            if (is_neighbor((x - 1, y), garden, label) and is_neighbor((x, y - 1), garden, label) and not is_neighbor((x - 1, y - 1), garden, label)) or (not is_neighbor((x - 1, y), garden, label) and not is_neighbor((x, y - 1), garden, label)):
                corners += 1

            # northeast vertex
            if (is_neighbor((x + 1, y), garden, label) and is_neighbor((x, y - 1), garden, label) and not is_neighbor((x + 1, y - 1), garden, label)) or (not is_neighbor((x + 1, y), garden, label) and not is_neighbor((x, y - 1), garden, label)):
                corners += 1

            # southwest vertex
            if (is_neighbor((x - 1, y), garden, label) and is_neighbor((x, y + 1), garden, label) and not is_neighbor((x - 1, y + 1), garden, label)) or (not is_neighbor((x - 1, y), garden, label) and not is_neighbor((x, y + 1), garden, label)):
                corners += 1

            # southeast vertex
            if (is_neighbor((x + 1, y), garden, label) and is_neighbor((x, y + 1), garden, label) and not is_neighbor((x + 1, y + 1), garden, label)) or (not is_neighbor((x + 1, y), garden, label) and not is_neighbor((x, y + 1), garden, label)):
                corners += 1

        total_price += (area * corners)
        print(f"Plot {label}: Area = {area}, Sides = {corners}")
    
    return total_price
