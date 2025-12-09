
# Advent of Code 2025 - Day 8

import math

class JunctionBox:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def parse_input(input, use_sample_input = False):
    junction_boxes = []

    sample_input = []
    sample_input.append("162,817,812")
    sample_input.append("57,618,57")
    sample_input.append("906,360,560")
    sample_input.append("592,479,940")
    sample_input.append("352,342,300")
    sample_input.append("466,668,158")
    sample_input.append("542,29,236")
    sample_input.append("431,825,988")
    sample_input.append("739,650,466")
    sample_input.append("52,470,668")
    sample_input.append("216,146,977")
    sample_input.append("819,987,18")
    sample_input.append("117,168,530")
    sample_input.append("805,96,715")
    sample_input.append("346,949,466")
    sample_input.append("970,615,88")
    sample_input.append("941,993,340")
    sample_input.append("862,61,35")
    sample_input.append("984,92,344")
    sample_input.append("425,690,689")

    if use_sample_input:
        for line in sample_input:
            x, y, z = line.strip().split(',')
            junction_boxes.append(JunctionBox(int(x), int(y), int(z)))
    else:
        for line in input:
            x, y, z = line.strip().split(',')
            junction_boxes.append(JunctionBox(int(x), int(y), int(z)))

    return junction_boxes

def calc_distance(p, q):
    return math.sqrt(((p.x - q.x) ** 2) + ((p.y - q.y) ** 2) + ((p.z - q.z) ** 2))

def solve_part_one(input):
    junction_boxes = parse_input(input, True)

def solve_part_two(input):
    return None
