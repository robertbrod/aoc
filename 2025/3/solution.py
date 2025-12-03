
# Advent of Code 2025 - Day 3

def solve_part_one(battery_banks):
    total_joltage = 0

    for bank in battery_banks:
        stripped_bank = bank.strip()
        batteries = [int(battery) for battery in stripped_bank]
        left_pointer = 0
        right_pointer = 1
        max_right = batteries[right_pointer]
        
        while right_pointer < len(batteries):
            left_battery = batteries[left_pointer]
            right_battery = batteries[right_pointer]

            if right_battery > left_battery and right_pointer + 1 < len(batteries):
                left_pointer = right_pointer
                right_pointer += 1
                max_right = batteries[right_pointer]
            else:
                max_right = max(max_right, right_battery)
                right_pointer += 1

        total_joltage += ((batteries[left_pointer] * 10) + max_right)

    return total_joltage

def solve_part_two(battery_banks):
    total_joltage = 0

    for bank in battery_banks:
        joltage = 0
        stripped_bank = bank.strip()
        batteries = [int(battery) for battery in stripped_bank]
        index = 0
        
        eligible_12s = batteries[index:len(batteries) - 11]
        max_12 = max(eligible_12s)
        index_of_max_12 = eligible_12s.index(max_12)
        joltage += max_12 * (10 ** 11)
        index += index_of_max_12 + 1
        # print(f"Eligible 12s: {eligible_12s}; Max 12: {max_12} - index {index_of_max_12}; joltage added {max_12 * (10 ** 11)}; next index {index}")

        eligible_11s = batteries[index:len(batteries) - 10]
        max_11 = max(eligible_11s)
        index_of_max_11 = eligible_11s.index(max_11)
        joltage += max_11 * (10 ** 10)
        index += index_of_max_11 + 1
        # print(f"Eligible 11s: {eligible_11s}; Max 11: {max_11} - index {index_of_max_11}; joltage added {max_11 * (10 ** 10)}; next index {index}")

        eligible_10s = batteries[index:len(batteries) - 9]
        max_10 = max(eligible_10s)
        index_of_max_10 = eligible_10s.index(max_10)
        joltage += max_10 * (10 ** 9)
        index += index_of_max_10 + 1
        # print(f"Eligible 10s: {eligible_10s}; Max 10: {max_10} - index {index_of_max_10}; joltage added {max_10 * (10 ** 9)}; next index {index}")

        eligible_9s = batteries[index:len(batteries) - 8]
        max_9 = max(eligible_9s)
        index_of_max_9 = eligible_9s.index(max_9)
        joltage += max_9 * (10 ** 8)
        index += index_of_max_9 + 1
        # print(f"Eligible 9s: {eligible_9s}; Max 9: {max_9} - index {index_of_max_9}; joltage added {max_9 * (10 ** 8)}; next index {index}")

        eligible_8s = batteries[index:len(batteries) - 7]
        max_8 = max(eligible_8s)
        index_of_max_8 = eligible_8s.index(max_8)
        joltage += max_8 * (10 ** 7)
        index += index_of_max_8 + 1
        # print(f"Eligible 8s: {eligible_8s}; Max 8: {max_8} - index {index_of_max_8}; joltage added {max_8 * (10 ** 7)}; next index {index}")

        eligible_7s = batteries[index:len(batteries) - 6]
        max_7 = max(eligible_7s)
        index_of_max_7 = eligible_7s.index(max_7)
        joltage += max_7 * (10 ** 6)
        index += index_of_max_7 + 1
        # print(f"Eligible 7s: {eligible_7s}; Max 7: {max_7} - index {index_of_max_7}; joltage added {max_7 * (10 ** 6)}; next index {index}")

        eligible_6s = batteries[index:len(batteries) - 5]
        max_6 = max(eligible_6s)
        index_of_max_6 = eligible_6s.index(max_6)
        joltage += max_6 * (10 ** 5)
        index += index_of_max_6 + 1
        # print(f"Eligible 6s: {eligible_6s}; Max 6: {max_6} - index {index_of_max_6}; joltage added {max_6 * (10 ** 5)}; next index {index}")

        eligible_5s = batteries[index:len(batteries) - 4]
        max_5 = max(eligible_5s)
        index_of_max_5 = eligible_5s.index(max_5)
        joltage += max_5 * (10 ** 4)
        index += index_of_max_5 + 1
        # print(f"Eligible 5s: {eligible_5s}; Max 5: {max_5} - index {index_of_max_5}; joltage added {max_5 * (10 ** 4)}; next index {index}")

        eligible_4s = batteries[index:len(batteries) - 3]
        max_4 = max(eligible_4s)
        index_of_max_4 = eligible_4s.index(max_4)
        joltage += max_4 * (10 ** 3)
        index += index_of_max_4 + 1
        # print(f"Eligible 4s: {eligible_4s}; Max 4: {max_4} - index {index_of_max_4}; joltage added {max_4 * (10 ** 3)}; next index {index}")

        eligible_3s = batteries[index:len(batteries) - 2]
        max_3 = max(eligible_3s)
        index_of_max_3 = eligible_3s.index(max_3)
        joltage += max_3 * (10 ** 2)
        index += index_of_max_3 + 1
        # print(f"Eligible 3s: {eligible_3s}; Max 3: {max_3} - index {index_of_max_3}; joltage added {max_3 * (10 ** 2)}; next index {index}")

        eligible_2s = batteries[index:len(batteries) - 1]
        max_2 = max(eligible_2s)
        index_of_max_2 = eligible_2s.index(max_2)
        joltage += max_2 * (10 ** 1)
        index += index_of_max_2 + 1
        # print(f"Eligible 2s: {eligible_2s}; Max 2: {max_2} - index {index_of_max_2}; joltage added {max_2 * (10 ** 1)}; next index {index}")

        eligible_1s = batteries[index:len(batteries)]
        max_1 = max(eligible_1s)
        index_of_max_1 = eligible_1s.index(max_1)
        joltage += max_1 * (10 ** 0)
        index += index_of_max_1 + 1
        # print(f"Eligible 1s: {eligible_1s}; Max 1: {max_1} - index {index_of_max_1}; joltage added {max_1 * (10 ** 0)}; next index {index}")

        total_joltage += joltage

    return total_joltage

def fetch_input():
    with open(f"2025_3_input.txt", "r") as file:
        return file.readlines()
    
# print(solve_part_one(fetch_input()))
print(solve_part_two(fetch_input()))
# print(solve_part_two(["234234234234278"]))