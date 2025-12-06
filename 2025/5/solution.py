
# Advent of Code 2025 - Day 5

def parse_input(input):
    ranges = []
    ids = []
    parsing_ranges = True
    
    for line in input:
        if parsing_ranges:
            if line == '':
                parsing_ranges = False
            else:
                start, end = line.split('-')
                ranges.append((int(start), int(end)))
        else:
            ids.append(int(line))
                
    return ranges, ids

def solve_part_one(input):
    fresh_product_id_ranges, product_ids = parse_input(input)
    
    fresh_products = 0
    
    for product_id in product_ids:
        found = False
        for product_id_range in fresh_product_id_ranges:
            min = product_id_range[0]
            max = product_id_range[1]
            
            if product_id >= min and product_id <= max:
                found = True
                break
        
        if found:
            fresh_products += 1
    
    return fresh_products

def solve_part_two(input):
    fresh_product_id_ranges, _ = parse_input(input)
    
    fresh_products = 0
    
    return fresh_products
