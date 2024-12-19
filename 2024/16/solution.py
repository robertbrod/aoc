# Advent of Code 2024 - Day 16

import heapq
import util

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

def dfs_all_paths(maze, current, end, visited, path, all_paths):
    x, y = current

    # Base case
    if current == end:
        all_paths.append(path.copy()[::-1])
        return
    
    visited.add(current)

    for direction in DIRECTIONS:
        nx, ny = x + direction[0], y + direction[1]

        if util.in_bounds_2d(nx, ny, len(maze[0]), len(maze)) and maze[ny][nx] != '#' and (nx, ny) not in visited:
            path.append((nx, ny))
            dfs_all_paths(maze, (nx, ny), end, visited, path, all_paths)
            path.pop()

    visited.remove(current)

def compute_cost(path):
    cost = 0
    
    for i in range(1, len(path)):
        current_node = path[i - 1]
        next_node = path[i]
        
        rotation_cost = compute_rotation_cost(current_node[1], next_node[1])
        cost += rotation_cost + 1
        
    return cost

def compute_direction(direction, node_direction):
    dx, dy = direction
    nx, ny = node_direction

    if nx < dx:
        return (-1, 0)
    elif nx > dx:
        return (1, 0)
    elif ny < dy:
        return (0, -1)
    else:
        return (0, 1)

def prune_paths(all_paths):
    score_dic = {}

    for path in all_paths:
        score = 0 
        last_direction = (1, 0)
        last_point = path[0]
        for pi, point in enumerate(path):
            if point == path[0]:
                continue
            node_direction = compute_direction(last_point, point)
            if node_direction != last_direction:
                score += 1000
            score += 1
            last_direction = node_direction
            last_point = point

        if score in score_dic:
            score_dic[score].append(path)
        else: 
            score_dic[score] = [path]

    smallest_score = min(score_dic.keys())
    
    return score_dic[smallest_score]

def solve_part_one(input):
    start, end, maze = parse_input(input)
    path = astar(maze, start, end)
    return compute_cost(path)

def solve_part_two(input):
    start, end, maze = parse_input(input)
    all_paths = []
    dfs_all_paths(maze, start, end, set(), [start], all_paths)
    pruned_paths = prune_paths(all_paths)
    tiles = set()
    for path in pruned_paths:
        for point in path:
            tiles.add(point)
    total_tiles = len(tiles)
    return total_tiles
