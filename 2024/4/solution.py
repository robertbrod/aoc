# Advent of Code 2024 - Day 4

part_one_target_string = "MAS"

def in_bounds(matrix, row, col):
    if row < 0 or row >= len(matrix):
        return False
    
    if col < 0 or col >= len(matrix[row]):
        return False
    
    return True

def north(matrix, row, col):
    next_letter_row = row - 1
    next_letter_col = col

    for i in range(3):
        if in_bounds(matrix, next_letter_row, next_letter_col) == False:
            return False
        
        if matrix[next_letter_row][next_letter_col] != part_one_target_string[i]:
            return False
        
        next_letter_row -= 1
        
    return True

def part_one_northeast(matrix, row, col):
    next_letter_row = row - 1
    next_letter_col = col + 1

    for i in range(3):
        if in_bounds(matrix, next_letter_row, next_letter_col) == False:
            return False
        
        if matrix[next_letter_row][next_letter_col] != part_one_target_string[i]:
            return False
        
        next_letter_row -= 1
        next_letter_col += 1
        
    return True

def part_two_northeast(matrix, row, col):
    next_letter_row = row - 1
    next_letter_col = col + 1

    if in_bounds(matrix, next_letter_row, next_letter_col) == False:
        return None
    
    return matrix[next_letter_row][next_letter_col]

def east(matrix, row, col):
    next_letter_row = row
    next_letter_col = col + 1

    for i in range(3):
        if in_bounds(matrix, next_letter_row, next_letter_col) == False:
            return False
        
        if matrix[next_letter_row][next_letter_col] != part_one_target_string[i]:
            return False
        
        next_letter_col += 1
        
    return True

def part_one_southeast(matrix, row, col):
    next_letter_row = row + 1
    next_letter_col = col + 1

    for i in range(3):
        if in_bounds(matrix, next_letter_row, next_letter_col) == False:
            return False
        
        if matrix[next_letter_row][next_letter_col] != part_one_target_string[i]:
            return False
        
        next_letter_row += 1
        next_letter_col += 1
        
    return True

def part_two_southeast(matrix, row, col):
    next_letter_row = row + 1
    next_letter_col = col + 1

    if in_bounds(matrix, next_letter_row, next_letter_col) == False:
        return None
    
    return matrix[next_letter_row][next_letter_col]

def south(matrix, row, col):
    next_letter_row = row + 1
    next_letter_col = col

    for i in range(3):
        if in_bounds(matrix, next_letter_row, next_letter_col) == False:
            return False
        
        if matrix[next_letter_row][next_letter_col] != part_one_target_string[i]:
            return False
        
        next_letter_row += 1
        
    return True

def part_one_southwest(matrix, row, col):
    next_letter_row = row + 1
    next_letter_col = col - 1

    for i in range(3):
        if in_bounds(matrix, next_letter_row, next_letter_col) == False:
            return False
        
        if matrix[next_letter_row][next_letter_col] != part_one_target_string[i]:
            return False
        
        next_letter_row += 1
        next_letter_col -= 1
        
    return True

def part_two_southwest(matrix, row, col):
    next_letter_row = row + 1
    next_letter_col = col - 1

    if in_bounds(matrix, next_letter_row, next_letter_col) == False:
        return None
    
    return matrix[next_letter_row][next_letter_col]

def west(matrix, row, col):
    next_letter_row = row
    next_letter_col = col - 1

    for i in range(3):
        if in_bounds(matrix, next_letter_row, next_letter_col) == False:
            return False
        
        if matrix[next_letter_row][next_letter_col] != part_one_target_string[i]:
            return False
        
        next_letter_col -= 1
        
    return True

def part_one_northwest(matrix, row, col):
    next_letter_row = row - 1
    next_letter_col = col - 1

    for i in range(3):
        if in_bounds(matrix, next_letter_row, next_letter_col) == False:
            return False
        
        if matrix[next_letter_row][next_letter_col] != part_one_target_string[i]:
            return False
        
        next_letter_row -= 1
        next_letter_col -= 1
        
    return True

def part_two_northwest(matrix, row, col):
    next_letter_row = row - 1
    next_letter_col = col - 1

    if in_bounds(matrix, next_letter_row, next_letter_col) == False:
        return None
    
    return matrix[next_letter_row][next_letter_col]

def check_northwest_to_southeast(matrix, row, col):
    northwest = part_two_northwest(matrix, row, col)
    if northwest == None or northwest not in ['M', 'S']:
        return False
    
    southeast = part_two_southeast(matrix, row, col)
    if southeast == None or southeast not in ['M', 'S']:
        return False
    
    if northwest == southeast:
        return False
    
    return True

def check_northeast_to_southwest(matrix, row, col):
    northeast = part_two_northeast(matrix, row, col)
    if northeast == None or northeast not in ['M', 'S']:
        return False
    
    southwest = part_two_southwest(matrix, row, col)
    if southwest == None or southwest not in ['M', 'S']:
        return False
    
    if northeast == southwest:
        return False
    
    return True

def solve_part_one(input):
    total_matches = 0
    matrix = []

    # Read input into a 2D array (matrix)
    for line in input:
        matrix.append(list(line))

    # Iterate over the matrix row by row looking for 'X's
    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            # If we find an 'X'. look in each cardinal direction for a word match
            if col == 'X':
                if north(matrix, row_index, col_index) == True:
                    total_matches += 1

                if part_one_northeast(matrix, row_index, col_index) == True:
                    total_matches += 1

                if east(matrix, row_index, col_index) == True:
                    total_matches += 1

                if part_one_southeast(matrix, row_index, col_index) == True:
                    total_matches += 1

                if south(matrix, row_index, col_index) == True:
                    total_matches += 1

                if part_one_southwest(matrix, row_index, col_index) == True:
                    total_matches += 1

                if west(matrix, row_index, col_index) == True:
                    total_matches += 1

                if part_one_northwest(matrix, row_index, col_index) == True:
                    total_matches += 1

    return total_matches

def solve_part_two(input):
    total_matches = 0
    matrix = []

    # Read input into a 2D array (matrix)
    for line in input:
        matrix.append(list(line))

    # Iterate over the matrix row by row looking for 'A's
    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            if col == 'A':
                if check_northwest_to_southeast(matrix, row_index, col_index) == True and check_northeast_to_southwest(matrix, row_index, col_index) == True:
                    total_matches += 1

    return total_matches
