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

def sort_blocks_contiguous(blocks):
    # Initialize free space pointer
    free_space_pointer = 0
    while blocks[free_space_pointer] != -1:
        free_space_pointer += 1

    # Initialize block pointer
    file_index_pointer = len(blocks) - 1
    while blocks[file_index_pointer] == -1:
        file_index_pointer -= 1

    file_data = blocks[file_index_pointer]

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
            file_index_pointer -= 1

            file_data = blocks[file_index_pointer]

        # Lets find another free space
        while free_space_pointer < len(blocks) and blocks[free_space_pointer] != -1:
            free_space_pointer += 1

        # Do we need to move our index pointer?
        if file_data == -1:
            while (0 <= file_index_pointer <= len(blocks)) and file_data == -1:
                file_index_pointer -= 1
                file_data = blocks[file_index_pointer]

def sort_blocks_non_fragmenting(blocks):
    # Initialize free space pointer
    free_space_pointer = 0
    while blocks[free_space_pointer] != -1:
        free_space_pointer += 1

    # Initialize block pointer
    file_index_pointer = len(blocks) - 1
    while blocks[file_index_pointer] == -1:
        file_index_pointer -= 1

    orig_file_index_pointer = file_index_pointer

    # Main loop: continues as long as we are in bounds with both pointers
    while (0 <= file_index_pointer < len(blocks)) and free_space_pointer < len(blocks):
        # Compute the size of the available free space
        free_space_size = 1
        free_space_pointer_pair = free_space_pointer + 1
        while free_space_pointer_pair < len(blocks) and blocks[free_space_pointer_pair] == -1:
            free_space_size += 1
            free_space_pointer_pair += 1   

        # Now lets look for something that will fit
        while True:
            if blocks[file_index_pointer] == -1:
                file_index_pointer -= 1
                while blocks[file_index_pointer] == -1:
                    file_index_pointer -= 1
            file_size = 1
            file_index_pointer_pair = file_index_pointer - 1
            while blocks[file_index_pointer_pair] == blocks[file_index_pointer]:
                file_size += 1
                file_index_pointer_pair -= 1
            
            if file_size <= free_space_size or file_index_pointer < free_space_pointer:
                break
            else:
                # If we moved into free space, we need to find another file block
                file_index_pointer = file_index_pointer_pair
                while blocks[file_index_pointer] == -1:
                    file_index_pointer -= 1
        
        # Make the swap
        if file_size <= free_space_size:
            for i in range(file_size):
                blocks[free_space_pointer + i] = blocks[file_index_pointer - i]
                blocks[file_index_pointer - i] = -1

        # Find the next free space
        free_space_pointer = free_space_pointer + file_size
        while free_space_pointer < len(blocks) and blocks[free_space_pointer] != -1:
            free_space_pointer += 1

        file_index_pointer = orig_file_index_pointer
        
def sort_blocks_non_fragmenting(blocks):
    # Initialize free space pointer
    free_space_pointer = 0
    while blocks[free_space_pointer] != -1:
        free_space_pointer += 1
    first_free_space_index = free_space_pointer

    # Initialize block pointer
    file_index_pointer = len(blocks) - 1
    while blocks[file_index_pointer] == -1:
        file_index_pointer -= 1
        
    # Main loop: continues as long as we are in bounds with both pointers
    while (0 <= file_index_pointer < len(blocks)) and free_space_pointer < len(blocks):        
        # Compute the size of the next file
        while blocks[file_index_pointer] == -1:
            file_index_pointer -= 1
            
        file_id = blocks[file_index_pointer]
        file_size = 1
        file_index_pointer_pair = file_index_pointer - 1
        while blocks[file_index_pointer_pair] == file_id:
            file_size += 1
            file_index_pointer_pair -= 1
            
        # Now lets find the first avilable free space that can hold it
        while blocks[free_space_pointer] != -1:
            free_space_pointer += 1
            
        while free_space_pointer < len(blocks):
            free_space = 1
            free_space_pointer_pair = free_space_pointer + 1
            while free_space_pointer_pair < len(blocks) and blocks[free_space_pointer_pair] == -1:
                free_space += 1
                free_space_pointer_pair += 1
            
            # Does the file fit in the available free space?
            if file_size <= free_space:
                break;
            else:
                free_space_pointer = free_space_pointer_pair
                while free_space_pointer < len(blocks) and blocks[free_space_pointer] != -1:
                    free_space_pointer += 1
                    
        # Make the swap!
        if file_size <= free_space and free_space_pointer < file_index_pointer:
            for i in range(file_size):
                blocks[free_space_pointer + i] = blocks[file_index_pointer - i]
                blocks[file_index_pointer - i] = -1
        else:
            file_index_pointer -= file_size

        # Reset the pointers
        free_space_pointer = first_free_space_index
                
        
def compute_checksum(blocks):
    checksum = 0

    index = 0
    while index < len(blocks):
        if blocks[index] != -1:
            checksum += (blocks[index] * index)
            
        index += 1

    return checksum

def solve_part_one(input):
    disk_map = [int(digit) for digit in input[0]]
    blocks = parse_disk_map(disk_map)
    sort_blocks_contiguous(blocks)
    return compute_checksum(blocks)

def solve_part_two(input):
    disk_map = [int(digit) for digit in input[0]]
    blocks = parse_disk_map(disk_map)
    sort_blocks_non_fragmenting(blocks)
    return compute_checksum(blocks)
