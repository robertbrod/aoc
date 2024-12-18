# Advent of Code 2024 - Day 15

def parse_input(input):
    warehouse_map = []
    movements = []
    robot_position = None
    possible_movements = ['<', '>', '^', 'v']
    
    for row_index, line in enumerate(input):
        if not line:
            continue
        
        if any(char in line for char in possible_movements):
            movements.extend(line)
        else:
            row = []
            robot_in_line = False
            for char in line:
                if char == '#':
                    row.extend(['#', '#'])
                elif char == 'O':
                    row.extend(['[', ']'])
                elif char == '.':
                    row.extend(['.', '.'])
                elif char == '@':
                    robot_in_line = True
                    row.extend(['@', '.'])
                    
                if robot_in_line:
                    robot_position = (row.index('@'), row_index)
                    
            warehouse_map.append(row)
    
    return warehouse_map, movements, robot_position

def solve_part_two(input):
    warehouse_map, movements, robot_position = parse_input(input)
    
    return None

# -----------------------------------------------------------------------#

def parse_input_1(input):
    warehouse_map = []
    movements = []
    robot_position = None
    
    for index, line in enumerate(input):
        if not line:
            continue
        
        elif line[0] == '#':
            if '@' in line:
                robot_position = (line.index('@'), index)
            
            warehouse_map.append([char for char in line])
        else:
            movements.extend(line)
        
    return warehouse_map, movements, robot_position

def fetch_neighbor_1(coord, movement, warehouse_map):
    x, y = coord
    
    if movement == '<':
        if x - 1 < 0:
            return None, None
        else:
            return (x - 1, y), warehouse_map[y][x - 1]
    elif movement == '>':
        if x + 1 >= len(warehouse_map[0]):
            return None, None
        else:
            return (x + 1, y), warehouse_map[y][x + 1]
    elif movement == '^':
        if y - 1 < 0:
            return None, None
        else:
            return (x, y - 1), warehouse_map[y - 1][x]
    elif movement == 'v':
        if y + 1 >= len(warehouse_map):
            return None, None
        else:
            return (x, y + 1), warehouse_map[y + 1][x]
        
def move_box_1(warehouse_map, robot_position, neighbor_coord, movement):
    can_move = True
    coord = neighbor_coord
    
    if movement == '<':
        # Check if we can move
        while can_move:
            next_pos_x, next_pos_y = coord[0] - 1, coord[1]
            if warehouse_map[next_pos_y][next_pos_x] == '#':
                can_move = False
            elif warehouse_map[next_pos_y][next_pos_x] == '.':
                coord = (next_pos_x, next_pos_y)
                break
            else:
                coord = (next_pos_x, next_pos_y)

        if can_move:
            # Make the move
            for index in range(0, abs(robot_position[0] - neighbor_coord[0])):
                warehouse_map[coord[1]][coord[0] + index] = 'O'
    elif movement == '>':
        # Check if we can move
        while can_move:
            next_pos_x, next_pos_y = coord[0] + 1, coord[1]
            if warehouse_map[next_pos_y][next_pos_x] == '#':
                can_move = False
            elif warehouse_map[next_pos_y][next_pos_x] == '.':
                coord = (next_pos_x, next_pos_y)
                break
            else:
                coord = (next_pos_x, next_pos_y)

        if can_move:
            # Make the move
            for index in range(0, abs(robot_position[0] - neighbor_coord[0])):
                warehouse_map[coord[1]][coord[0] - index] = 'O'

    elif movement == '^':
        # Check if we can move
        while can_move:
            next_pos_x, next_pos_y = coord[0], coord[1] - 1
            if warehouse_map[next_pos_y][next_pos_x] == '#':
                can_move = False
            elif warehouse_map[next_pos_y][next_pos_x] == '.':
                coord = (next_pos_x, next_pos_y)
                break
            else:
                coord = (next_pos_x, next_pos_y)

        if can_move:
            # Make the move
            for index in range(0, abs(robot_position[1] - neighbor_coord[1])):
                warehouse_map[coord[1] - index][coord[0]] = 'O'

    elif movement == 'v':
        # Check if we can move
        while can_move:
            next_pos_x, next_pos_y = coord[0], coord[1] + 1
            if warehouse_map[next_pos_y][next_pos_x] == '#':
                can_move = False
            elif warehouse_map[next_pos_y][next_pos_x] == '.':
                coord = (next_pos_x, next_pos_y)
                break
            else:
                coord = (next_pos_x, next_pos_y)

        if can_move:
            # Make the move
            for index in range(0, abs(robot_position[1] - neighbor_coord[1])):
                warehouse_map[coord[1] + index][coord[0]] = 'O'
                
    return can_move
        
def move_robot_1(warehouse_map, movements, robot_pos):
    robot_position = robot_pos
            
    for movement in movements:
        if movement == '<':
            neighbor_coord, neighbor = fetch_neighbor_1(robot_position, movement, warehouse_map)
            if neighbor == '#':
                continue
            # We ran into a box
            if neighbor == 'O':
                # Try to move box
                if move_box_1(warehouse_map, robot_position, neighbor_coord, movement):
                    # If we were able to move the box, move the robot
                    new_robot_pos = (robot_position[0] - 1, robot_position[1])
                    warehouse_map[robot_position[1]][robot_position[0]] = '.'
                    warehouse_map[new_robot_pos[1]][new_robot_pos[0]] = '@'
                    robot_position = new_robot_pos
            # Move the robot
            else:
                new_robot_pos = (robot_position[0] - 1, robot_position[1])
                warehouse_map[robot_position[1]][robot_position[0]] = '.'
                warehouse_map[new_robot_pos[1]][new_robot_pos[0]] = '@'
                robot_position = new_robot_pos

        elif movement == '>':
            neighbor_coord, neighbor = fetch_neighbor_1(robot_position, movement, warehouse_map)
            if neighbor == '#':
                continue
            # We ran into a box
            if neighbor == 'O':
                # Try to move box
                if move_box_1(warehouse_map, robot_position, neighbor_coord, movement):
                    # If we were able to move the box, move the robot
                    new_robot_pos = (robot_position[0] + 1, robot_position[1])
                    warehouse_map[robot_position[1]][robot_position[0]] = '.'
                    warehouse_map[new_robot_pos[1]][new_robot_pos[0]] = '@'
                    robot_position = new_robot_pos
            # Move the robot
            else:
                new_robot_pos = (robot_position[0] + 1, robot_position[1])
                warehouse_map[robot_position[1]][robot_position[0]] = '.'
                warehouse_map[new_robot_pos[1]][new_robot_pos[0]] = '@'
                robot_position = new_robot_pos

        elif movement == '^':
            neighbor_coord, neighbor = fetch_neighbor_1(robot_position, movement, warehouse_map)
            if neighbor == '#':
                continue
            # We ran into a box
            if neighbor == 'O':
                # Try to move box
                if move_box_1(warehouse_map, robot_position, neighbor_coord, movement):
                    # If we were able to move the box, move the robot
                    new_robot_pos = (robot_position[0], robot_position[1] - 1)
                    warehouse_map[robot_position[1]][robot_position[0]] = '.'
                    warehouse_map[new_robot_pos[1]][new_robot_pos[0]] = '@'
                    robot_position = new_robot_pos
            # Move the robot
            else:
                new_robot_pos = (robot_position[0], robot_position[1] - 1)
                warehouse_map[robot_position[1]][robot_position[0]] = '.'
                warehouse_map[new_robot_pos[1]][new_robot_pos[0]] = '@'
                robot_position = new_robot_pos

        elif movement == 'v':
            neighbor_coord, neighbor = fetch_neighbor_1(robot_position, movement, warehouse_map)
            if neighbor == '#':
                continue
            # We ran into a box
            if neighbor == 'O':
                # Try to move box
                if move_box_1(warehouse_map, robot_position, neighbor_coord, movement):
                    # If we were able to move the box, move the robot
                    new_robot_pos = (robot_position[0], robot_position[1] + 1)
                    warehouse_map[robot_position[1]][robot_position[0]] = '.'
                    warehouse_map[new_robot_pos[1]][new_robot_pos[0]] = '@'
                    robot_position = new_robot_pos
            # Move the robot
            else:
                new_robot_pos = (robot_position[0], robot_position[1] + 1)
                warehouse_map[robot_position[1]][robot_position[0]] = '.'
                warehouse_map[new_robot_pos[1]][new_robot_pos[0]] = '@'
                robot_position = new_robot_pos
                
def compute_gps_1(warehouse_map):
    sum_of_gps = 0
    
    for row_index, row in enumerate(warehouse_map):
        for col_index, col in enumerate(row):
            if col == 'O':
                sum_of_gps += ((100 * row_index) + col_index)
        
    return sum_of_gps

def solve_part_one(input):
    warehouse_map, movements, robot_position = parse_input_1(input)
    move_robot_1(warehouse_map, movements, robot_position)
    
    return compute_gps_1(warehouse_map)
