# Advent of Code 2024 - Day 2

def solve_part_one(input):
    total_safe = 0
    
    for line in input:
        parts = list(map(int, line.split()))
        pointer = 0
        last_num = -1
        is_increasing = None
        safe = True
        
        while pointer < len(parts) and safe == True:
            if last_num == -1:
                last_num = parts[pointer]
                pointer += 1
                continue
            elif parts[pointer] == last_num:
                safe = False
                continue
                
            if is_increasing == None:
                if abs(parts[pointer] - last_num > 3):
                    safe = False
                    break
                elif parts[pointer] > last_num:
                    is_increasing = True
                else:
                    is_increasing = False
                    
            if (parts[pointer] - last_num > 3 and is_increasing == True) or (parts[pointer] < last_num and is_increasing == True):
                safe = False
                break
            elif (parts[pointer] - last_num < -3 and is_increasing == False) or (parts[pointer] > last_num and is_increasing == False):
                safe = False
                break
            
            last_num = parts[pointer]
            pointer += 1
                
        if safe == True:
            total_safe += 1       
        
    return total_safe

def solve_part_two(input):
    total_safe = 0

    for line in input:
        parts = list(map(int, line.split()))
        mutable_parts = parts.copy()
        pointer = 0
        removed_pointer = 0
        last_num = -1
        is_increasing = None
        safe = True
        last_try = False

        while pointer < len(mutable_parts) and safe == True:
            if removed_pointer == len(parts):
                last_try = True

            if last_num == -1:
                last_num = mutable_parts[pointer]
                pointer += 1
                continue
            elif mutable_parts[pointer] == last_num:
                if last_try == True:
                    safe = False
                    break

                mutable_parts = parts.copy()
                del mutable_parts[removed_pointer]
                removed_pointer += 1
                pointer = 0
                is_increasing = None
                last_num = -1
                continue
                
            if is_increasing == None:
                if abs(mutable_parts[pointer] - last_num > 3):
                    if last_try == True:
                        safe = False
                        break

                    mutable_parts = parts.copy()
                    del mutable_parts[removed_pointer]
                    removed_pointer += 1
                    pointer = 0
                    is_increasing = None
                    last_num = -1
                    continue
                elif mutable_parts[pointer] > last_num:
                    is_increasing = True
                else:
                    is_increasing = False
                    
            if (mutable_parts[pointer] - last_num > 3 and is_increasing == True) or (mutable_parts[pointer] < last_num and is_increasing == True):
                if last_try == True:
                    safe = False
                    break

                mutable_parts = parts.copy()
                del mutable_parts[removed_pointer]
                removed_pointer += 1
                pointer = 0
                is_increasing = None
                last_num = -1
                continue
            elif (mutable_parts[pointer] - last_num < -3 and is_increasing == False) or (mutable_parts[pointer] > last_num and is_increasing == False):
                if last_try == True:
                    safe = False
                    break

                mutable_parts = parts.copy()
                del mutable_parts[removed_pointer]
                removed_pointer += 1
                pointer = 0
                is_increasing = None
                last_num = -1
                continue
            
            last_num = mutable_parts[pointer]
            pointer += 1
                
        if safe == True:
            total_safe += 1       
        
    return total_safe
