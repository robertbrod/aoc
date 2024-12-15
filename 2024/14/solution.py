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
    for robot in robots:
5        x_init, y_init = robot.position
        x_velocity, y_velocity = robot.velocity

        x_final = (x_init + x_velocity * seconds)
        y_final = (y_init + y_velocity * seconds)

        x_final %= width
        y_final %= height

        print(f"Final adjusted position: ({x_final}, {y_final})")
    pass

def solve_part_one(input):
    robots = parse_input(input)

    quadrants = {
        "north-west": 0,
        "north-east": 0,
        "south-west": 0,
        "south-east": 0
    }

    move_robots(robots, quadrants, 100, 11, 7)

    # Compute and return safety factor
    return None

def solve_part_two(input):
    return None
