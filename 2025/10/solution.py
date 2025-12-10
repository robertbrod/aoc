
# Advent of Code 2025 - Day 10

class MachineManual:
    def __init__(self, target_light_state, button_masks, joltage_requirements):
        self.target_light_state = target_light_state
        self.button_masks = button_masks
        self.joltage_requirements = joltage_requirements

def fetch_sample_input():
    input = []
    input.append("[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}")
    input.append("[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}")
    input.append("[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}")

    return input

def fetch_input():
    with open(f"2025_10_input.txt", "r") as file:
        return file.readlines()

def parse_input(input):
    manuals = []

    for line in input:
        button_masks = []
        joltage_requirements = None

        for data in line.split():
            # parsing light diagram
            if data.startswith('['):
                data = data.replace('[', '')
                data = data.replace(']', '')
                light_diagram = [x for x in data]
                print(light_diagram)
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
    manuals = parse_input(input)

    for manual in manuals:
        print(manual.target_light_state)
        print(manual.button_masks)

    return None

def solve_part_two(input):
    return None

# solve_part_one(fetch_input())
solve_part_one(fetch_sample_input())
# solve_part_two(fetch_input())
# solve_part_two(fetch_input())