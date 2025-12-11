
# Advent of Code 2025 - Day 10

import itertools

class MachineManual:
    def __init__(self, target_light_state, button_masks, joltage_requirements):
        self.target_light_state = target_light_state
        self.button_masks = button_masks
        self.joltage_requirements = joltage_requirements

def fetch_input():
    with open(f"2025_10_input.txt", "r") as file:
        return file.readlines()

def parse_input(input, use_sample_input = False):
    sample_input = []
    sample_input.append("[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}")
    sample_input.append("[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}")
    sample_input.append("[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}")

    manuals = []

    if use_sample_input:
        for line in sample_input:
            button_masks = []
            joltage_requirements = None

            for data in line.split():
                # parsing light diagram
                if data.startswith('['):
                    data = data.replace('[', '')
                    data = data.replace(']', '')
                    light_diagram = [x for x in data]
                    light_diagram.reverse()
                    target_light_state = 0
                    for power, x in enumerate(light_diagram):
                        if x == '#':
                            target_light_state ^= (2 ** power)

                # parsing wiring schematic
                elif data.startswith('('):
                    data = data.replace('(', '')
                    data = data.replace(')', '')
                    button_ints = [int(x) for x in data.split(',')]
                    button_bits = 0
                    size = len(light_diagram) - 1
                    for button_int in button_ints:
                        button_bits ^= (2 ** (size - button_int))
                    button_masks.append(button_bits)

                # parsing joltage requirements
                elif data.startswith('{'):
                    data = data.replace('{', '')
                    data = data.replace('}', '')
                    joltage_requirements = [int(x) for x in data.split(',')]

            manuals.append(MachineManual(target_light_state, button_masks, joltage_requirements))
    
    else:
        for line in input:
            button_masks = []
            joltage_requirements = None

            for data in line.split():
                # parsing light diagram
                if data.startswith('['):
                    data = data.replace('[', '')
                    data = data.replace(']', '')
                    light_diagram = [x for x in data]
                    light_diagram.reverse()
                    target_light_state = 0
                    for power, x in enumerate(light_diagram):
                        if x == '#':
                            target_light_state ^= (2 ** power)

                # parsing wiring schematic
                elif data.startswith('('):
                    data = data.replace('(', '')
                    data = data.replace(')', '')
                    button_ints = [int(x) for x in data.split(',')]
                    button_bits = 0
                    size = len(light_diagram) - 1
                    for button_int in button_ints:
                        button_bits ^= (2 ** (size - button_int))
                    button_masks.append(button_bits)

                # parsing joltage requirements
                elif data.startswith('{'):
                    data = data.replace('{', '')
                    data = data.replace('}', '')
                    joltage_requirements = [int(x) for x in data.split(',')]

            manuals.append(MachineManual(target_light_state, button_masks, joltage_requirements))
        
    return manuals

def solve_part_one(input):
    manuals = parse_input(input, False)
    total_button_presses = 0

    num_manuals = len(manuals)
    for m_index, manual in enumerate(manuals):
        print(f"Processing manual {m_index} of {num_manuals}...")
        target_light_state = manual.target_light_state
        button_masks = manual.button_masks
        min_button_presses = float('inf')      
        
        permutations = itertools.permutations(button_masks)
        
        for p_index, permutation in enumerate(permutations):
            print(f"Processing permutation {p_index}...")
            visited = set()
            light_state = 0
            visited.add(light_state)
            button_presses = None
            for mask in permutation:
                light_state ^= mask
                if light_state == target_light_state:
                    if not button_presses:
                        button_presses = 1
                    else:
                        button_presses += 1
                    if button_presses != None and button_presses < min_button_presses:
                        min_button_presses = button_presses
                        
                    break
                elif light_state in visited:
                    break
                else:
                    visited.add(light_state)
                    if not button_presses:
                        button_presses = 1
                    else:
                        button_presses += 1
                    
                    if button_presses > min_button_presses:
                        break
            
        total_button_presses += min_button_presses
        print(f"Added {min_button_presses} button presses to our total. New total is {total_button_presses}...")

    return total_button_presses

def solve_part_two(input):
    return None