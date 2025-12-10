
# Advent of Code 2025 - Day 9

from shapely import Point
from shapely import Polygon

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
    polygon = Polygon(points)
    max_area = 0

    for i in range(0, len(points)):
        for j in range(0, len(points)):
            corner1 = points[i]
            corner1_x = corner1.x
            corner1_y = corner1.y

            corner2 = points[j]
            corner2_x = corner2.x
            corner2_y = corner2.y

            w = abs(corner1_x - corner2_x) + 1
            h = abs(corner1_y - corner2_y) + 1

            minx = min(corner1_x, corner2_x)
            maxx = max(corner1_x, corner2_x)
            miny = min(corner1_y, corner2_y)
            maxy = max(corner1_y, corner2_y)

            rect = Polygon.from_bounds(minx, miny, maxx, maxy)

            if polygon.contains(rect):
                max_area = max(max_area, w * h)

    print(int(max_area))

def parse_input(input, use_sample_input=False):
    sample_input = []
    sample_input.append("7,1")
    sample_input.append("11,1")
    sample_input.append("11,7")
    sample_input.append("9,7")
    sample_input.append("9,5")
    sample_input.append("2,5")
    sample_input.append("2,3")
    sample_input.append("7,3")

    points = []

    if use_sample_input:
        for line in sample_input:
            x, y = line.strip().split(',')
            points.append(Point(int(x), int(y)))
    else:
        for line in input:
            x, y = line.strip().split(',')
            points.append(Point(int(x), int(y)))

    return points

def fetch_input():
    with open(f"2025_9_input.txt", "r") as file:
        return file.readlines()
    
# solve_part_one(fetch_input())
solve_part_two(fetch_input())
