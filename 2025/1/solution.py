
# Advent of Code 2025 - Day 1

def solve_part_one(input):
    return None

def solve_part_two(input):
    current_pos = 50
    num_zeros = 0
    
    for turn in input:
        direction = turn[0]
        clicks = turn[1:]
        
        for i in range(int(clicks)):
            if direction == "L":
                if current_pos == 0:
                    current_pos = 99
                else:
                    current_pos -= 1
                    
                if current_pos == 0:
                    num_zeros += 1
                    
            elif direction == "R":
                if current_pos == 99:
                    current_pos = 0
                else:
                    current_pos += 1
                    
                if current_pos == 0:
                    num_zeros += 1
                    
    return num_zeros

# def fetch_input():
#     with open(f"2025_1_input.txt", "r") as file:
#         return file.read()
    
# solve_part_two(fetch_input().splitlines())
