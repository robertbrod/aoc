
# Advent of Code 2025 - Day 5

class FreshProductRange:
    def __init__(self, min, max):
        self.min = min
        self.max = max

def parse_input_part_two(input, use_sample=False):
    sample_input = []
    sample_input.append("3-5")
    sample_input.append("10-14")
    sample_input.append("16-20")
    sample_input.append("12-18")
    
    ranges = []
    
    if use_sample:
        for line in sample_input:
            if line == '':
                break
                
            start, end = line.split('-')
            ranges.append(FreshProductRange(int(start), int(end)))
    else:  
        for line in input:
            if line == '':
                break
            else:
                start, end = line.split('-')
                ranges.append(FreshProductRange(int(start), int(end))) 
                
    return ranges

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
    fresh_product_id_ranges = parse_input_part_two(input, False)
    
    while True:
        fresh_product_id_ranges.sort(key = lambda product_id_range: product_id_range.min)
        range_absorbed = False
        for index in range(0, len(fresh_product_id_ranges)):
            # check for overlap with the following range (min of next compared to max of current)
            if index + 1 < len(fresh_product_id_ranges) and (fresh_product_id_ranges[index + 1].min <= fresh_product_id_ranges[index].max or (fresh_product_id_ranges[index + 1].min - 1 == fresh_product_id_ranges[index].max)):
                fresh_product_id_ranges[index].max = max(fresh_product_id_ranges[index + 1].max, fresh_product_id_ranges[index].max)
                del fresh_product_id_ranges[index + 1]
                range_absorbed = True
                break
        
        if not range_absorbed:
            break
    
    fresh_products = 0
    
    for fresh_product_id_range in fresh_product_id_ranges:
        print(f"{fresh_product_id_range.min}-{fresh_product_id_range.max}")
        fresh_products += (fresh_product_id_range.max - fresh_product_id_range.min) + 1
    
    return fresh_products
