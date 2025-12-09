
# Advent of Code 2025 - Day 9

def solve_part_one(input):
    points = parse_input(input)
    max_area = 0
    for i in range(0, len(points)):
        for j in range(0, len(points)):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]

            dx += 1
            dy += 1

            if abs(dx * dy) > max_area:
                max_area = abs(dx * dy)

    print(max_area)

def solve_part_two(input):
    points = parse_input(input)
    max_area = 0

    for i in range(0, len(points)):
        ax = points[i][0]
        ay = points[i][1]
        for j in range(0, len(points)):
            bx = points[j][0]
            by = points[j][1]

            # if ax == bx and ay == by and i != j:
            #     print("Duplicate point found in list")

            dx = ax - bx
            dy = ay - by

            dx += 1
            dy += 1
            
            valid_point = True

            if abs(dx * dy) > max_area:
                for point in range(0, len(points)):
                    px = points[point][0]
                    py = points[point][1]

                    if (px == ax and py == ay) or (px == bx and py == by):
                        # print(f"skipping point ({px}, {py}).... a = ({ax}, {ay}); b = ({bx}, {by})")
                        continue
                    else:
                        if (px < ax and px > bx) or (px > ax and px < bx):
                            if (py < ay and py > by) or (py > ay and py < by):
                                # print(f"{px} is between {ax} and {bx}")
                                # print(f"{py} is between {ay} and {by}")
                                valid_point = False
                                break

                top_boundary_count = 1
                bottom_boundary_count = 1
                left_boundary_count = 1
                right_boundary_count = 1

                for point in range(0, len(points)):
                    px = points[point][0]
                    py = points[point][1]

                    if py == ay and ((px < ax and px > bx) or (px > ax and px < bx)):
                        top_boundary_count += 1
                    if py == by and ((px < ax and px > bx) or (px > ax and px < bx)):
                        bottom_boundary_count += 1
                    if px == ax and ((py < ay and py > by) or (py > ay and py < by)):
                        left_boundary_count += 1
                    if px == bx and ((py < ay and py > by) or (py > ay and py < by)):
                        right_boundary_count += 1

                if top_boundary_count < 2 or bottom_boundary_count < 2 or left_boundary_count < 2 or right_boundary_count < 2:
                    valid_point = False

                if valid_point:
                    max_area = abs(dx * dy)

    print(max_area)

def parse_input(input):
    points = []

    for line in input:
        x, y = line.strip().split(',')
        points.append((int(x), int(y)))

    return points

def fetch_input():
    with open(f"2025_9_input.txt", "r") as file:
        return file.readlines()
    
# solve_part_one(fetch_input())
solve_part_two(fetch_input())
