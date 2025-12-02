
# Advent of Code 2025 - Day 2
import math

class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def solve_part_one(input):
    id_ranges = []
    sum_of_invalid_ids = 0

    for series in input.split(','):
        data = series.split('-')
        id_ranges.append(Range(int(data[0]), int(data[1])))
        
    for id_range in id_ranges:
        for id in range(id_range.start, id_range.end + 1):
            str_id = str(id)
            if len(str_id) % 2 == 0:
                middle = len(str_id) // 2
                first_half = str_id[0:middle]
                second_half = str_id[middle:]
                if first_half == second_half:
                    sum_of_invalid_ids += id
            else:
                continue
            
    return sum_of_invalid_ids
            
def solve_part_two(input):
    id_ranges = []
    sum_of_invalid_ids = 0

    for series in input.split(','):
        data = series.split('-')
        id_ranges.append(Range(int(data[0]), int(data[1])))
        
    for id_range in id_ranges:
        for id in range(id_range.start, id_range.end + 1):
            str_id = str(id)
            len_of_word = len(str_id)
            square_root = math.sqrt(len_of_word)
            factors = set()
            for i in range(1, math.floor(square_root) + 1):
                factors.add(len_of_word // i)
                factors.add(i)
                
            valid_factors = {f for f in factors if f < len_of_word}
                
            for factor in valid_factors:
                chunked_string = chunk_string(str_id, factor)
                if len(set(chunked_string)) == 1:
                    sum_of_invalid_ids += id
                    break

    return sum_of_invalid_ids             
                
def chunk_string(text, length):
    return [text[i:i + length] for i in range(0, len(text), length)]
    

def fetch_input():
    with open(f"2025_2_input.txt", "r") as file:
        return file.read()
    
print(solve_part_two(fetch_input()))
