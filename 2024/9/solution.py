# Advent of Code 2024 - Day 9

def parse_disk_map(disk_map):
    blocks = []

    # Alternate between reading files and free space
    reading_free_space = False

    file_id = 0

    for digit in disk_map:
        if not reading_free_space:
            # Read file size
            file_size = digit
            blocks.extend(file_size * [file_id])
            file_id += 1
        else:
            # Read free space
            free_space_size = digit
            blocks.extend(free_space_size * [-1])

        # Flip the flag
        reading_free_space = not reading_free_space

    return blocks

def sort_blocks(blocks):
    # Initialize free space pointer
    free_space_pointer = 0
    while blocks[free_space_pointer] != -1:
        free_space_pointer += 1

    # Initialize block pointer
    file_index_pointer = len(blocks) - 1
    index_dx = -1
    while blocks[file_index_pointer] == -1:
        file_index_pointer += index_dx

    file_data = blocks[file_index_pointer]

    dx_swapped = False

    # Main loop: continues as long as we are in bounds with both pointers
    while (0 <= file_index_pointer < len(blocks)) and free_space_pointer < len(blocks):
        # Exit condition
        if free_space_pointer >= file_index_pointer:
            break

        while free_space_pointer < len(blocks) and blocks[free_space_pointer] == -1 and file_data != -1:
            # Swap the file data and the free space
            blocks[free_space_pointer] = file_data
            blocks[file_index_pointer] = -1

            # Move the pointers
            free_space_pointer += 1
            file_index_pointer += index_dx

            file_data = blocks[file_index_pointer]

        # Lets find another free space
        while free_space_pointer < len(blocks) and blocks[free_space_pointer] != -1:
            free_space_pointer += 1

        # Do we need to move our index pointer?
        if file_data == -1:
            while (0 <= file_index_pointer <= len(blocks)) and file_data == -1:
                file_index_pointer += index_dx
                file_data = blocks[file_index_pointer]
        
def compute_checksum(blocks):
    checksum = 0

    index = 0
    while index < len(blocks) and blocks[index] != -1:
        checksum += (blocks[index] * index)
        index += 1

    return checksum

def solve_part_one(input):
    disk_map = [int(digit) for digit in input[0]]
    blocks = parse_disk_map(disk_map)
    sort_blocks(blocks)
    return compute_checksum(blocks)

def solve_part_two(input):
    return 0
