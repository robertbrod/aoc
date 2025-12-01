
# Advent of Code 2025 - Day 1

def solve_part_one(input):
    current_pos = 50
    number_of_times_at_0 = 0

    for turn in input:
        direction = turn[0]
        num = int(turn[1:])
        if (direction == "L"):
            current_pos = (current_pos - num) % 100
        else:
            current_pos = (current_pos + num) % 100

        if current_pos == 0:
            number_of_times_at_0 = number_of_times_at_0 + 1

    return number_of_times_at_0

def solve_part_two(input):
    current_pos = 50
    number_of_clicks_at_0 = 0

    for turn in input:
        direction = turn[0]
        num = int(turn[1:])
        if (direction == "L"):
            for _ in range(num):
                if current_pos == 0:
                    current_pos = 99
                else:
                    current_pos -= 1

                if current_pos == 0:
                    number_of_clicks_at_0 += 1
        else:
            for _ in range(num):
                if current_pos == 99:
                    current_pos = 0
                else:
                    current_pos -= 1

                current_pos += 1
                if current_pos == 0:
                    number_of_clicks_at_0 += 1

    return number_of_clicks_at_0

def fetch_input():
    with open(f"2025_1_input.txt", "r") as file:
        return file.read().splitlines()
    
#print(solve_part_one(fetch_input()))
print(solve_part_two(fetch_input()))
