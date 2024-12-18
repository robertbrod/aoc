# Advent of Code 2024 - Day 17

def parse_input(input):
    registers = {}
    program = None
    
    for i, line in enumerate(input):
        if i == 0:
            registers['A'] = int(line.split(':')[1])
        elif i == 1:
            registers['B'] = int(line.split(':')[1])
        elif i == 2:
            registers['C'] = int(line.split(':')[1])
        elif i == 4:
            program = list(map(int, line.split(':')[1].strip().split(',')))
        
    return registers, program

def compute_operand(registers, combo_operand):
    operand = None

    if 0 <= combo_operand <= 3:
        operand = combo_operand
    elif combo_operand == 4:
        operand = registers['A']
    elif combo_operand == 5:
        operand = registers['B']
    elif combo_operand == 6:
        operand = registers['C'] 

    return operand

# opcode 0
def adv_instruction(registers, combo_operand):
    numerator = registers['A']
    denominator = pow(2, compute_operand(registers, combo_operand))

    registers['A'] = int(numerator / denominator)

# opcode 1
def bxl_instruction(registers, literal_operand):
    registers['B'] = registers['B'] ^ literal_operand

# opcode 2
def bst_instruction(registers, combo_operand):
    operand = compute_operand(registers, combo_operand)

    registers['B'] = operand % 8

# opcode 3
def jnz_instruction(registers, literal_operand):
    if registers['A'] == 0:
        return -1
    else:
        return literal_operand
    
# opcode 4
def bxc_instruction(registers, literal_operand):
    registers['B'] = registers['B'] ^ registers['C']

# opcode 5
def out_instruction(registers, combo_operand):
    operand = compute_operand(registers, combo_operand)

    return operand % 8

# opcode 6
def bdv_instruction(registers, combo_operand):
    numerator = registers['A']
    denominator = pow(2, compute_operand(registers, combo_operand))

    registers['B'] = int(numerator / denominator)

# opcode 7
def cdv_instruction(registers, combo_operand):    
    numerator = registers['A']
    denominator = denominator = pow(2, compute_operand(registers, combo_operand))

    registers['C'] = int(numerator / denominator)

def execute_program(registers, program):
    output = []

    program_counter = 0
    function_map = {
        0: adv_instruction, # store result of division in register A
        1: bxl_instruction, # store result of XOR in register B
        2: bst_instruction, # store result of % 8 in register B
        3: jnz_instruction, # return -1 if no jump needed, otherwise returns index of instruction to jump to
        4: bxc_instruction, # store result of XOR in register B
        5: out_instruction, # returns result of % 8
        6: bdv_instruction, # store result of division in register B
        7: cdv_instruction # store result of division in register C
    }

    while program_counter < len(program):
        opcode = program[program_counter]
        operand = program[program_counter + 1]
        func = function_map[opcode]

        if opcode != 3:
            result = func(registers, operand)
            if result != None:
                output.append(str(result))

            program_counter += 2

        else:
            result = func(registers, operand)
            if result == -1:
                program_counter += 2
            else:
                program_counter = result

    return output

def solve_part_one(input):
    registers, program = parse_input(input)
    output = execute_program(registers, program)
    output_str = ",".join(output)
    
    return output_str

def solve_part_two(input):
    return None
