# Advent of Code 2024 - Day 18

import heapq
import util

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Node:
    def __init__(self, x, y, g, h):
        self.x = x
        self.y = y
        self.g = g # Cost from start to this node
        self.h = h # Heuristic (estimated cost to goal)
        self.f = g + h # Total cost
        self.parent = None
        
    def __lt__(self, other):
        return self.f < other.f
    
def parse_input(input):
    points = []
    
    for line in input:
        data = line.split(',')
        points.append((int(data[0]), int(data[1])))
        
    return points

def generate_grid(length, width, data, num_data):
    grid = []
    for _ in range(width):
        grid.append(['.'] * length)
        
    for i in range(num_data):
        x, y = data[i]
        grid[y][x] = '#'

    return grid

def reconstruct_path(node):
    path = []
    while node:
        path.append([(node.x, node.y)])
        node = node.parent
    return path[::-1]

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, end):
    open_list = []
    closed_list = set()
    g_values = {}
    
    start_node = Node(start[0], start[1], 0, heuristic(start, end)) 
    g_values[(start[0], start[1])] = 0
    
    # Priority queue (min-heap)
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current = heapq.heappop(open_list)
        
        if (current.x, current.y) == end:
            return reconstruct_path(current)
        
        closed_list.add((current.x, current.y))
        
        for direction in DIRECTIONS:
            nx, ny = current.x + direction[0], current.y + direction[1]
            
            if not util.in_bounds_2d(nx, ny, len(grid[0]), len(grid)) or grid[ny][nx] == '#':
                continue
            
            move_cost = 1
            g = current.g + move_cost
            
            if (nx, ny) in closed_list or g >= g_values.get((nx, ny), float('inf')):
                continue
            
            g_values[(nx, ny)] = g
            h = heuristic((nx, ny), end)
            neighbor = Node(nx, ny, g, h)
            neighbor.parent = current
            
            heapq.heappush(open_list, neighbor)
            
    return None

def print_grid(grid):
    for row in grid:
        print("".join(row))
    
def solve_part_one(input):
    data = parse_input(input)
    grid = generate_grid(71, 71, data, 1024)
    path = astar(grid, (0, 0), (70, 70))
    return len(path) - 1

def solve_part_two(input):
    data = parse_input(input)
    
    for i in range(1, 2426):
        grid = generate_grid(71, 71, data, 1024 + i)
        if not astar(grid, (0, 0), (70, 70)):
            bad_memory_coord = data[1024 + i - 1]
            print(bad_memory_coord)
            print(f"{bad_memory_coord[0]},{bad_memory_coord[1]}")
            return f"{bad_memory_coord[0]},{bad_memory_coord[1]}"
