# Advent of Code 2024 - Day 13

class ClawMachineConfig:
    def __init__(self, a, b, prize):
        self.a = a
        self.b = b
        self.prize = prize

def parse_input(input):
    configurations = []
    ax, ay, bx, by, px, py = None, None, None, None, None, None
    
    counter = 0
    for line in input:
        # Button A: X+77, Y+52
        if counter == 0:
            data = line.split(':')
            data = data[1].strip()
            data = data.split(',')
            x_raw, y_raw = data[0].split('+'), data[1].split('+')
            ax, ay = int(x_raw[1]), int(y_raw[1])
            
            counter += 1
        # Button B: X+14, Y+32
        elif counter == 1:
            data = line.split(':')
            data = data[1].strip()
            data = data.split(',')
            x_raw, y_raw = data[0].split('+'), data[1].split('+')
            bx, by = int(x_raw[1]), int(y_raw[1])
            counter += 1
        # Prize: X=5233, Y=14652
        elif counter == 2:
            data = line.split(':')
            data = data[1].split(',')
            x_raw, y_raw = data[0].split('='), data[1].split('=')
            px, py = int(x_raw[1]), int(y_raw[1])
            config = ClawMachineConfig((ax, ay), (bx, by), (px, py))
            configurations.append(config)
            counter += 1
        # Empty line
        elif counter == 3:
            counter = 0 
            
    return configurations

def parse_input_2(input):
    configurations = []
    ax, ay, bx, by, px, py = None, None, None, None, None, None
    
    counter = 0
    for line in input:
        # Button A: X+77, Y+52
        if counter == 0:
            data = line.split(':')
            data = data[1].strip()
            data = data.split(',')
            x_raw, y_raw = data[0].split('+'), data[1].split('+')
            ax, ay = int(x_raw[1]), int(y_raw[1])
            
            counter += 1
        # Button B: X+14, Y+32
        elif counter == 1:
            data = line.split(':')
            data = data[1].strip()
            data = data.split(',')
            x_raw, y_raw = data[0].split('+'), data[1].split('+')
            bx, by = int(x_raw[1]), int(y_raw[1])
            counter += 1
        # Prize: X=5233, Y=14652
        elif counter == 2:
            data = line.split(':')
            data = data[1].split(',')
            x_raw, y_raw = data[0].split('='), data[1].split('=')
            px, py = int(x_raw[1]), int(y_raw[1])
            config = ClawMachineConfig((ax, ay), (bx, by), (px + 10000000000000, py + 10000000000000))
            configurations.append(config)
            counter += 1
        # Empty line
        elif counter == 3:
            counter = 0 
            
    return configurations

def compute_fewest_tokens(configuration):
    ax, ay = configuration.a
    bx, by = configuration.b
    px, py = configuration.prize
    
    a = ((px * by) - (py * bx)) // ((ax * by) - (ay * bx))
    b = ((ax * py) - (ay * px)) // ((ax * by) - (ay * bx))
    
    if ((a * ax) + (b * bx)) == px and ((a * ay) + (b * by)) == py:
        return ((3 * a) + b)
    else:
        return 0

def solve_part_one(input):
    tokens_spent = 0
    
    configurations = parse_input(input)
    for configuration in configurations:
        tokens_spent += compute_fewest_tokens(configuration)
        
    return tokens_spent

def solve_part_two(input):
    tokens_spent = 0
    
    configurations = parse_input_2(input)
    for configuration in configurations:
        tokens_spent += compute_fewest_tokens(configuration)
        
    return tokens_spent
