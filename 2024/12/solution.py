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

def solve_part_two(input):
    total_price = 0
    garden = parse_input(input)
    garden_width = len(garden[0])
    garden_height = len(garden)
    
    visited = set()
    regions = []
    for x in range(len(garden[0])):
        for y in range(len(garden)):
            if (x, y) not in visited:
                region = []
                flood_fill_two(garden, x, y, garden[y][x], visited, region)
                regions.append((garden[y][x], region))
                
    for region in regions:
        region_label = region[0]
        coords = region[1]
        area = len(coords)
        corners = 0
        
        for coord in coords:
            north_neighbor = (coord[0], coord[1] - 1)
            north_east_neighbor = (coord[0] + 1, coord[1] - 1)
            east_neighbor = (coord[0] + 1, coord[1])
            south_east_neighbor = (coord[0] + 1, coord[1] + 1)
            south_neighbor = (coord[0], coord[1] + 1)
            south_west_neighbor = (coord[0] - 1, coord[1] + 1)
            west_neighbor = (coord[0] - 1, coord[1])
            north_west_neighbor = (coord[0] - 1, coord[1] - 1)
            
            # opposing neighbors 1 (north->south)
            if util.in_bounds_2d(north_neighbor[0], north_neighbor[1], garden_width, garden_height) and util.in_bounds_2d(south_neighbor[0], south_neighbor[1], garden_width, garden_height) and garden[north_neighbor[1]][north_neighbor[0]] != region_label and garden[south_neighbor[1]][south_neighbor[0]] != region_label:
                continue
            # opposing neighbors 2 (east->west)
            elif util.in_bounds_2d(east_neighbor[0], east_neighbor[1], garden_width, garden_height) and util.in_bounds_2d(east_neighbor[0], east_neighbor[1], garden_width, garden_height) and garden[east_neighbor[1]][east_neighbor[0]] != region_label and garden[west_neighbor[1]][west_neighbor[0]] != region_label:
                continue
            
        total_price += (area * corners)

    return total_price
