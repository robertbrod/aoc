# Advent of Code 2024 - Day 14

class Robot:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

def parse_input(input):
    robots = []

    for line in input:
        data = line.split()
        raw_position = data[0].split('=')[1].split(',')
        raw_velocity = data[1].split('=')[1].split(',')
        position = (int(raw_position[0]), int(raw_position[1]))
        velocity = (int(raw_velocity[0]), int(raw_velocity[1]))
        robot = Robot(position, velocity)
        robots.append(robot)

    return robots

def move_robots(robots, quadrants, seconds, width, height):
    mid_width = width // 2
    mid_height = height // 2
    
    for robot in robots:
        x, y = robot.position
        x_velocity, y_velocity = robot.velocity

        x = (x + x_velocity * seconds) % width
        y = (y + y_velocity * seconds) % height

        if x == mid_width or y == mid_height:
            continue
        
        # north-west
        elif x < mid_width and y < mid_height:
             quadrants["north-west"] += 1
        
        # north-east 
        elif x > mid_width and y < mid_height:
            quadrants["north-east"] += 1
            
        # south-west    
        elif x < mid_width and y > mid_height:
            quadrants["south-west"] += 1
            
        # south-east
        elif x > mid_width and y > mid_height:
            quadrants["south-east"] += 1
            
def move_and_print_robots(robots, matrix, width, height):
    density = 0
    
    for seconds in range(1, 99999):
        for robot in robots:
            x, y = robot.position
            x_velocity, y_velocity = robot.velocity

            x = (x + x_velocity) % width
            y = (y + y_velocity) % height
            
            matrix[y][x] = '#'
            
            robot.position = (x, y)
            
            if 35 < x < 70 and 35 < y < 70:
                density += 1
                
        if density > 100:
            with open("2024/14/bathroom_map.txt", "w") as file:
                for row in matrix:
                    file.write("".join(row) + "\n")
                file.write(f"Time elapsed: {seconds} seconds\n")
                    
        density = 0
        reset_matrix(matrix)
        
def reset_matrix(matrix):
    matrix.clear()
    matrix.extend([['.'] * 101 for _ in range(103)])

def solve_part_one(input):
    robots = parse_input(input)

    quadrants = {
        "north-west": 0,
        "north-east": 0,
        "south-west": 0,
        "south-east": 0
    }

    move_robots(robots, quadrants, 100, 101, 103)

    # Compute and return safety factor
    return quadrants["north-west"] * quadrants["north-east"] * quadrants["south-west"] * quadrants["south-east"]

def solve_part_two(input):
    robots = parse_input(input)
    matrix = [['.'] * 101 for _ in range(103)]
    move_and_print_robots(robots, matrix, 101, 103)

    return None
