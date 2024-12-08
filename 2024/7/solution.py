# Advent of Code 2024 - Day 7

def parse_input(input):
    rows = []
    for line in input:
        target, nums = line.split(":")
        rows.append([int(target), list(map(int, nums.split()))])

    return rows

def backtrack(index, current_value, target, nums):
    # Base case: Have we used all the numbers?
    if index == len(nums):
        return current_value == target
    
    num = nums[index]

    # Addition
    if backtrack(index + 1, current_value + num, target, nums):
        return True

    # Multiplication
    if backtrack(index + 1, current_value * num, target, nums):
        return True

    return False

def concatenate_nums(nums, index):
    num_1 = nums[index]
    num_2 = nums[index + 1]
    del nums[index]
    del nums[index]
    nums.insert(index, int(str(num_1) + str(num_2)))

def backtrack_two(index, current_value, target, nums):
    # Base case: Have we used all the numbers?
    if index == len(nums):
        return current_value == target
    
    num = nums[index]

    # Addition
    if backtrack_two(index + 1, current_value + num, target, nums):
        return True

    # Multiplication
    if backtrack_two(index + 1, current_value * num, target, nums):
        return True
    
    # Concatenation
    if backtrack_two(index + 1, int(str(current_value) + str(num)), target, nums):
        return True

    return False

def solve_part_one(input):
    total_calibration = 0

    data = parse_input(input)
    for data_set in data:
        target = data_set[0]
        nums = data_set[1]
        if backtrack(1, nums[0], target, nums):
            total_calibration += target

    return total_calibration

def solve_part_two(input):
    total_calibration = 0

    data = parse_input(input)
    for data_set in data:
        target = data_set[0]
        nums = data_set[1]
        if backtrack_two(1, nums[0], target, nums):
            total_calibration += target
            
    return total_calibration
