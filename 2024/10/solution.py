# Advent of Code 2024 - Day 10

import util
from collections import deque

def parse_input(input):
    topographic_map = [] 
    trailheads = set()

    for x, row in enumerate(input):
        topographic_map.append([])
        for y, char in enumerate(row):
            digit = int(char)
            if digit == 0:
                trailheads.add((x, y))
            topographic_map[x].append(digit)

    return topographic_map, trailheads

def fetch_neigbors(topographic_map, coords):
    neighbors = set()
    width = len(topographic_map[0])
    height = len(topographic_map)
    x, y = coords[0], coords[1]

    # Up
    dx, dy = 0, -1
    if util.in_bounds_2d(x + dx, y + dy, width, height):
        neighbors.add((x + dx, y + dy))

    # Down
    dx, dy = 0, 1 
    if util.in_bounds_2d(x + dx, y + dy, width, height):
        neighbors.add((x + dx, y + dy))

    # Left
    dx, dy = -1, 0
    if util.in_bounds_2d(x + dx, y + dy, width, height):
        neighbors.add((x + dx, y + dy))

    # Right
    dx, dy = 1, 0
    if util.in_bounds_2d(x + dx, y + dy, width, height):
        neighbors.add((x + dx, y + dy))

    return neighbors

def run_bfs_part1(topographic_map, trailhead):
    queue = deque([(trailhead[0], trailhead[1], 0)])
    visited = set()
    visited.add((trailhead[0], trailhead[1], 0))
    trailhead_endings = set()

    while queue:
        x, y, val = queue.popleft()

        if val == 9:
            trailhead_endings.add((x, y))
            continue

        neighbors = fetch_neigbors(topographic_map, (x, y))
        for neighbor in neighbors:
            if topographic_map[neighbor[0]][neighbor[1]] == val + 1:
                visited.add((neighbor[0], neighbor[1], val + 1))
                queue.append((neighbor[0], neighbor[1], val + 1))

    return len(trailhead_endings)

def run_bfs_part2(topographic_map, trailhead):
    trailhead_score = 0
    queue = deque([(trailhead[0], trailhead[1], 0)])
    visited = set()
    visited.add((trailhead[0], trailhead[1], 0))

    while queue:
        x, y, val = queue.popleft()

        if val == 9:
            trailhead_score += 1
            continue

        neighbors = fetch_neigbors(topographic_map, (x, y))
        for neighbor in neighbors:
            if topographic_map[neighbor[0]][neighbor[1]] == val + 1:
                visited.add((neighbor[0], neighbor[1], val + 1))
                queue.append((neighbor[0], neighbor[1], val + 1))

    return trailhead_score

def solve_part_one(input):
    total_trailhead_score = 0
    
    topographic_map, trailheads = parse_input(input)

    for trailhead in trailheads:
        total_trailhead_score += run_bfs_part1(topographic_map, trailhead)

    return total_trailhead_score

def solve_part_two(input):
    total_trailhead_score = 0
    
    topographic_map, trailheads = parse_input(input)

    for trailhead in trailheads:
        total_trailhead_score += run_bfs_part2(topographic_map, trailhead)

    return total_trailhead_score
