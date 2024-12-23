# Advent of Code 2024 - Day 20

from collections import deque, defaultdict

def parse_input(input):
    race, start, end = [], None, None

    for y, row in enumerate(input):
        row_contents = []
        for x, col in enumerate(row):
            if col == 'S':
                row_contents.append('.')
                start = (x, y)
            elif col == 'E':
                row_contents.append('.')
                end = (x, y)
            else:
                row_contents.append(col)
        race.append(row_contents)

    return race, start, end

def solve_part_one(input):
    race, start, end = parse_input(input)
    queue = deque([(start, 0)])
    distances = {}
    while queue:
        pos, distance = queue.popleft()
        x, y = pos[0], pos[1]

        if (x, y) in distances:
            continue

        distances[(x, y)] = distance
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x + dx, y + dy
            if race[ny][nx] != '#' and (nx, ny) not in distances:
                queue.appendleft(((nx, ny), distance + 1))

    shortcuts = defaultdict(int)
    for y, row in enumerate(race):
        for x, col in enumerate(row):
            for nx, ny in [(x - 2, y), (x + 2, y), (x, y - 2), (x, y + 2), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1)]:
                if (x, y) not in distances or (nx, ny) not in distances:
                    continue

                time_saved = distances[(nx, ny)] - distances[(x, y)] - 2
                if time_saved >= 100:
                    shortcuts[time_saved] += 1

    return sum(shortcut for shortcut in shortcuts.values())

def solve_part_two(input):
    race, start, end = parse_input(input)
    queue = deque([(start, 0)])
    distances = {}
    while queue:
        pos, distance = queue.popleft()
        x, y = pos[0], pos[1]

        if (x, y) in distances:
            continue

        distances[(x, y)] = distance
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x + dx, y + dy
            if race[ny][nx] != '#' and (nx, ny) not in distances:
                queue.appendleft(((nx, ny), distance + 1))

    shortcuts = defaultdict(int)
    for y, row in enumerate(race):
        for x, col in enumerate(row):
            if (x, y) not in distances:
                continue

            for len_cheat in range(2, 21):
                for dy in range(len_cheat + 1):
                    dx = len_cheat - dy
                    for nx, ny in set([(x + dx, y + dy), (x - dx, y + dy), (x + dx, y - dy), (x - dx, y - dy)]):
                        if (nx, ny) not in distances:
                            continue

                        time_saved = distances[(nx, ny)] - distances[(x, y)] - len_cheat
                        if time_saved >= 100:
                            shortcuts[time_saved] += 1

    return sum(shortcut for shortcut in shortcuts.values())
