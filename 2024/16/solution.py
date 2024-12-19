# Advent of Code 2024 - Day 16

import heapq
import util
from collections import defaultdict, deque

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Node:
    def __init__(self, x, y, direction, g, h):
        self.x = x
        self.y = y
        self.direction = direction
        self.g = g # Cost from start to this node
        self.h = h # Heuristic (estimated cost to goal)
        self.f = g + h # Total cost
        self.parent = None
        
    def __lt__(self, other):
        return self.f < other.f

def parse_input(input):
    maze = []
    start = None
    end = None
    
    for x, row in enumerate(input):
        maze_row = []
        for y, col in enumerate(row):
            if col == 'S':
                start = (x, y)
                maze_row.append('.')
            elif col == 'E':
                end = (x, y)
                maze_row.append('.')
            else:
                maze_row.append(col)
        maze.append(maze_row)
            
    return start, end, maze
    
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def reconstruct_path(node):
    path = []
    while node:
        path.append([(node.x, node.y), node.direction])
        node = node.parent
    return path[::-1]

def compute_rotation_cost(current_direction, new_direction):
    if current_direction == new_direction:
        return 0
    return 1000
    
def astar(maze, start, end):
    open_list = []
    
    # Priority queue (min-heap)
    heapq.heappush(open_list, Node(start[0], start[1], (1, 0), 0, heuristic(start, end)))
    
    closed_list = set()
    
    while open_list:
        current = heapq.heappop(open_list)
        
        if (current.x, current.y) == end:
            return reconstruct_path(current)
        
        closed_list.add((current.x, current.y))
        
        for direction in DIRECTIONS:
            nx, ny = current.x + direction[0], current.y + direction[1]
            
            if not util.in_bounds_2d(nx, ny, len(maze[0]), len(maze)) or maze[ny][nx] == '#' or (nx, ny) in closed_list:
                continue
            
            rotation_cost = compute_rotation_cost(current.direction, direction)
            move_cost = 1
            
            g = current.g + move_cost + rotation_cost
            h = heuristic((nx, ny), end)
            neighbor = Node(nx, ny, direction, g, h)
            neighbor.parent = current
            
            heapq.heappush(open_list, neighbor)
            
    return None

def compute_cost(path):
    cost = 0
    
    for i in range(1, len(path)):
        current_node = path[i - 1]
        next_node = path[i]
        
        rotation_cost = compute_rotation_cost(current_node[1], next_node[1])
        cost += rotation_cost + 1
        
    return cost

def solve_part_one(input):
    start, end, maze = parse_input(input)
    path = astar(maze, start, end)
    return compute_cost(path)

def solve_part_two(input):
    return None
