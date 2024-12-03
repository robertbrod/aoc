# Advent of Code 2024 - Day 3

import re

def solve_part_one(input):
    total = 0

    for line in input:
        valid_instructions = find_matches(line)
        for instruction in valid_instructions:
            multiplicand = int(instruction[0])
            multiplier = int(instruction[1])
            total += (multiplicand * multiplier)

    return total

def solve_part_two(input):
    total = 0
    enabled = True

    for line in input:
        valid_instructions = find_matches(line, 2)
        for instruction in valid_instructions:
            filtered_instruction = list(filter(None, instruction))

            if filtered_instruction[0] == "do()":
                enabled = True
            elif filtered_instruction[0] == "don't()":
                enabled = False
            elif (enabled == True):
                multiplicand = int(filtered_instruction[0])
                multiplier = int(filtered_instruction[1])
                total += (multiplicand * multiplier)

    return total

def find_matches(input_text, part = 1):
    part_one_regex = r"mul\((\d+),(\d+)\)"
    part_two_regex = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"

    return re.findall(part_one_regex, input_text) if part == 1 else re.findall(part_two_regex, input_text)