
# Advent of Code 2015 - Day 2

# Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

def parse_input(input):        
    return [tuple(map(int, line.split('x'))) for line in input]

def solve_part_one(input):
    total_material = 0
    
    present_dimensions = parse_input(input)
    for present_dimension in present_dimensions:
        length = present_dimension[0]
        width = present_dimension[1]
        height = present_dimension[2]
        
        side_1 = (length * width)
        side_2 = (width * height)
        side_3 = (height * length)
        
        smallest_side = min(side_1, side_2, side_3)
        
        total_material += ((2 * side_1) + (2 * side_2) + (2 * side_3) + smallest_side)
        
    return total_material

def solve_part_two(input):
    total_material = 0
    
    present_dimensions = parse_input(input)
    for present_dimension in present_dimensions:
        length = present_dimension[0]
        width = present_dimension[1]
        height = present_dimension[2]
        
        side_1_perimeter = ((2 * height) + (2 * width))
        side_2_perimeter = ((2 * height) + (2 * length))
        side_3_perimeter = ((2 * length) + (2 * width))
        
        volume = length * width * height
        
        total_material += (min(side_1_perimeter, side_2_perimeter, side_3_perimeter) + volume)
        
    return total_material
