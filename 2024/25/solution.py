# Advent of Code 2024 - Day 25

def parse_input(input):
    schematics = []
    
    # build out the 2d arrays
    next_schematic = []
    for line in input:
        if line:
            next_schematic.append(line)
        else:
            schematics.append(next_schematic)
            next_schematic = []
    
    schematics.append(next_schematic)
    
    # sort them into keys and locks
    keys = []
    locks = []
    for schematic in schematics:
        # it's a lock
        if schematic[0] == '#####' and schematic[6] == '.....':
            locks.append(schematic)
        # it's a key
        elif schematic[0] == '.....' and schematic[6] == '#####':
            keys.append(schematic)
            
    # convert them into height maps
    key_maps = []
    
    for key in keys:
        heights = []
        height = 0
        
        for x in range(0, len(key[0])):
            for y in range(len(key) - 2, -1, -1):
                if key[y][x] == '#' and y == 0:
                    heights.append(height)
                    height = 0
                elif key[y][x] == '#':
                    height += 1
                else:
                    heights.append(height)
                    height = 0
                    break
        key_maps.append(heights)
        
    lock_maps = []
    for lock in locks:
        heights = []
        height = 0
        
        for x in range(0, len(lock[0])):
            for y in range(1, len(lock)):
                if lock[y][x] == '#' and y == len(lock) - 1:
                    heights.append(height)
                    height = 0
                elif lock[y][x] == '#':
                    height += 1
                else:
                    heights.append(height)
                    height = 0
                    break
        lock_maps.append(heights)
    
    return key_maps, lock_maps

def solve_part_one(input):
    key_maps, lock_maps = parse_input(input)
    
    pairs_that_fit = set()
    
    for lock_index, lock in enumerate(lock_maps):
        for key_index, key in enumerate(key_maps):
            fits = True
            for i in range(0, 5):
                if lock[i] + key[i] > 5:
                    fits = False
                    break
            if fits:
                pairs_that_fit.add((lock_index, key_index))

    return len(pairs_that_fit)
