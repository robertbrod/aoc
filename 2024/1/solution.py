# Advent of Code 2024 - Day 1

def solve_part_one(input):
    left_list = []
    right_list = []
    
    for line in input:
        parts = line.split("   ")
        left_list.append(parts[0])
        right_list.append(parts[1])
        
    left_list.sort()
    right_list.sort()
    
    total_diff = 0
    
    for index, loc_id in enumerate(left_list):
        total_diff += abs(int(left_list[index]) - int(right_list[index]))
        
    return total_diff

def solve_part_two(input):
    left_list = []
    right_list = []
    
    for line in input:
        parts = line.split("   ")
        left_list.append(parts[0])
        right_list.append(parts[1])
        
    hash_map = {}
    
    for loc_id in right_list:
        if loc_id in hash_map:
            hash_map[loc_id] = hash_map.get(loc_id, 0) + 1
        else:
            hash_map[loc_id] = 1
            
    total_similarity_score = 0        
    
    for loc_id in left_list:
        if loc_id in hash_map:
            total_similarity_score += int(loc_id) * int(hash_map.get(loc_id))
    
    return total_similarity_score