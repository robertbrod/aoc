# Advent of Code 2024 - Day 24

def parse_input(input):
    wires = {}
    gates = []
    for line in input:
        if line:
            # We are parsing wire inputs
            if ':' in line:
                data = line.replace(' ', '').split(':')
                wires[data[0]] = int(data[1])
            # We are parsing gates
            else:
                data = line.replace(' ', '').split('->')
                if 'AND' in data[0]:
                    output = data[1]
                    data = data[0].split('AND')
                    gates.append(('AND', data[0], data[1], output)) # (gate, input wire, input wire, output wire)
                elif 'XOR' in data[0]:
                    output = data[1]
                    data = data[0].split(('XOR'))
                    gates.append(('XOR', data[0], data[1], output)) # (gate, input wire, input wire, output wire)
                elif 'OR' in data[0]:
                    output = data[1]
                    data = data[0].split(('OR'))
                    gates.append(('OR', data[0], data[1], output)) # (gate, input wire, input wire, output wire)
                    
    return wires, gates

def and_operation(num1, num2):
    return num1 & num2

def xor_operation(num1, num2):
    return num1 ^ num2

def or_operation(num1, num2):
    return num1 | num2

def get_output(wires, gates):
    outputs = []
    
    operation_map = {
        'AND': and_operation,
        'XOR': xor_operation,
        'OR': or_operation
    }
    
    gates_to_process = gates[:]
    
    while gates_to_process:
        gates_without_signals = []
        for gate in gates_to_process:
            # check if inputs are received
            if gate[1] in wires and gate[2] in wires:
                operation = gate[0]
                input_one = wires[gate[1]] # input wire 1
                input_two = wires[gate[2]] # input wire 2
                output_wire = gate[3]
                
                output = operation_map[operation](input_one, input_two)
                if 'z' in output_wire:
                    outputs.append((output_wire, output))
                else:
                    wires[output_wire] = output
            else:
                gates_without_signals.append(gate)
        
        gates_to_process = gates_without_signals
            
    return outputs

def compute_decimal_output(outputs):
    decimal_value = 0
    
    for power, output_wire in enumerate(outputs):
        value = output_wire[1]
        if value == 1:
            decimal_value += pow(2, power)
            
    return decimal_value

def solve_part_one(input):
    wires, gates = parse_input(input)
    outputs = sorted(get_output(wires, gates))
    decimal_output = compute_decimal_output(outputs)
    
    return decimal_output

def solve_part_two(input):
    return None
