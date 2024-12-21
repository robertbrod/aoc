# Advent of Code 2024 - Day 16

import heapq
import util
from copy import deepcopy

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
EXPECTED_SCORE = 75416

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
    
def check_reversed_direction(new_direction, prev_direction):
    prev_direction_index = DIRECTIONS.index(prev_direction)
    new_direction_index = DIRECTIONS.index(new_direction)

    return (prev_direction_index + 2) % 4 != new_direction_index

def parse_input(input):
    maze = []
    start = None
    end = None
    
    for y, row in enumerate(input):
        maze_row = []
        for x, col in enumerate(row):
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

def dijkstra(maze, start, end):
    expected_score = 75416
    unvisited_nodes = set()
    heap = []
    node = Node(start[0], start[1], DIRECTIONS[3], 0, [(start)])
    
    
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

def dijkstra(maze, start, end):
    open_list = []

    heapq.heappush(open_list, (0, start, (1, 0), [start]))
    costs = [[float('inf')] * len(row) for row in maze]

    costs[start[1]][start[0]] = 0
    
    visited = set()
    paths = []

    while open_list:
        cost, pos, direction, path = heapq.heappop(open_list)
        visited.add((pos, direction))

        if pos == end and cost <= costs[pos[1]][pos[0]]:
            paths.extend(path)
        
        for dx, dy in DIRECTIONS:
            nx = pos[0] + dx
            ny = pos[1] + dy
            n_pos = (nx, ny)

            if not util.in_bounds_2d(nx, ny, len(maze[0]), len(maze)) or maze[ny][nx] == '#':
                continue

            new_cost = cost + 1
            if (dx, dy) != direction:
                new_cost += 1000

            if costs[ny][nx] + 1000 < new_cost or new_cost > 75416:
                continue

            if (dx, dy) != direction:
                costs[ny][nx] = min(costs[ny][nx], cost + 1001)
                path_turn = deepcopy(path)
                path_turn.append(n_pos)
                heapq.heappush(open_list, (cost + 1001, n_pos, (dx, dy), path_turn))
            elif (dx, dy) == direction:
                costs[ny][nx] = min(costs[ny][nx], cost + 1)
                path_straight = deepcopy(path)
                path_straight.append(n_pos)
                heapq.heappush(open_list, (cost + 1, n_pos, (dx, dy), path_straight))

    return len(set(paths))

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
    start, end, maze = parse_input(input)
<<<<<<< HEAD
    paths = dijkstra(maze, start, end)
    return None
=======
    tile_count = dijkstra(maze, start, end)

    return tile_count
>>>>>>> baf30ea191c199e18959ba9b289e7a9bce6b78a9
