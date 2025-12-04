
# Advent of Code 2025 - Day 4

def in_bounds_2d(x: int, y: int, width: int, height: int) -> bool:
    """
    Check if a particular coord is within the bounds of a 2D list

    Args:
        x (int): x coord
        y (int): y coord
        width (int): width of 2D list
        height (int): height of 2D list

    Returns:
        bool: The result of the check.

    Raises:
        None
    """

    return 0 <= x < width and 0 <= y < height

def parse_input(input):
    room_map = []
    paper_rolls = set()

    for x, row in enumerate(input):
        room_map.append([])
        for y, col in enumerate(row):
            if col == '@':
                paper_rolls.add((x, y))
            room_map[x].append(col)

    return room_map, paper_rolls

def count_neighbor_rolls(room_map, coords):
    neighbors = 0
    width = len(room_map[0])
    height = len(room_map)
    x, y = coords[0], coords[1]

    # North
    dx, dy = 0, -1
    if in_bounds_2d(x + dx, y + dy, width, height) and room_map[x + dx][y + dy] == '@':
        neighbors += 1

    # NorthEast
    dx, dy = 1, -1
    if in_bounds_2d(x + dx, y + dy, width, height) and room_map[x + dx][y + dy] == '@':
        neighbors += 1

    # East
    dx, dy = 1, 0
    if in_bounds_2d(x + dx, y + dy, width, height) and room_map[x + dx][y + dy] == '@':
        neighbors += 1

    # SouthEast
    dx, dy = 1, 1
    if in_bounds_2d(x + dx, y + dy, width, height) and room_map[x + dx][y + dy] == '@':
        neighbors += 1

    # South
    dx, dy = 0, 1 
    if in_bounds_2d(x + dx, y + dy, width, height) and room_map[x + dx][y + dy] == '@':
        neighbors += 1

    # SouthWest
    dx, dy = -1, 1 
    if in_bounds_2d(x + dx, y + dy, width, height) and room_map[x + dx][y + dy] == '@':
        neighbors += 1

    # West
    dx, dy = -1, 0
    if in_bounds_2d(x + dx, y + dy, width, height) and room_map[x + dx][y + dy] == '@':
        neighbors += 1

    # NorthWest
    dx, dy = -1, -1
    if in_bounds_2d(x + dx, y + dy, width, height) and room_map[x + dx][y + dy] == '@':
        neighbors += 1

    return neighbors

def solve_part_one(input):
    room_map, paper_rolls = parse_input(input)
    total_movable_paper_rolls = 0

    for paper_roll in paper_rolls:
        neighbor_count = count_neighbor_rolls(room_map, (paper_roll[0], paper_roll[1]))
        if neighbor_count < 4:
            total_movable_paper_rolls += 1

    return total_movable_paper_rolls

def remove_paper_rolls(room_map, paper_rolls):
    total_removed_this_run = 0

    for paper_roll in paper_rolls:
        neighbor_count = count_neighbor_rolls(room_map, (paper_roll[0], paper_roll[1]))
        if neighbor_count < 4:
            paper_roll_x = paper_roll[0]
            paper_roll_y = paper_roll[1]
            room_map[paper_roll_x][paper_roll_y] = '.'
            total_removed_this_run += 1

    return total_removed_this_run

def calculate_paper_rolls(room_map):
    paper_rolls = set()

    for x, row in enumerate(room_map):
        for y, col in enumerate(row):
            if col == '@':
                paper_rolls.add((x, y))

    return paper_rolls

def solve_part_two(input):
    room_map, _ = parse_input(input)
    total_movable_paper_rolls = 0

    while True:
        paper_rolls = calculate_paper_rolls(room_map)
        removed_paper_rolls = remove_paper_rolls(room_map, paper_rolls)
        if removed_paper_rolls == 0:
            break

        total_movable_paper_rolls += removed_paper_rolls

    return total_movable_paper_rolls
