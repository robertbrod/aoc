
# Advent of Code 2025 - Day 8

import math

class JunctionBox:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"x: {self.x}; y: {self.y}; z: {self.z} "
    
    def __eq__(self, value):
        return self.x == value.x and self.y == value.y and self.z == value.z

class Connection:
    def __init__(self, a, b, distance):
        self.a = a
        self.b = b
        self.distance = distance

    def __str__(self):
        return f"{self.a} - {self.b}: distance: {self.distance}"

class Circuit:
    def __init__(self):
        self.junction_boxes = []

    def __str__(self):
        a = ""
        for box in self.junction_boxes:
            a += box.__str__()

        return a
    
    def __eq__(self, value):
        if len(self.junction_boxes) != len(value.junction_boxes):
            return False
        else:
            for i in range(0, len(self.junction_boxes)):
                if self.junction_boxes[i] != value.junction_boxes[i]:
                    return False

        return True

def parse_input(input, use_sample_input = False):
    junction_boxes = []

    sample_input = []
    sample_input.append("162,817,812")
    sample_input.append("57,618,57")
    sample_input.append("906,360,560")
    sample_input.append("592,479,940")
    sample_input.append("352,342,300")
    sample_input.append("466,668,158")
    sample_input.append("542,29,236")
    sample_input.append("431,825,988")
    sample_input.append("739,650,466")
    sample_input.append("52,470,668")
    sample_input.append("216,146,977")
    sample_input.append("819,987,18")
    sample_input.append("117,168,530")
    sample_input.append("805,96,715")
    sample_input.append("346,949,466")
    sample_input.append("970,615,88")
    sample_input.append("941,993,340")
    sample_input.append("862,61,35")
    sample_input.append("984,92,344")
    sample_input.append("425,690,689")

    if use_sample_input:
        for line in sample_input:
            x, y, z = line.strip().split(',')
            junction_boxes.append(JunctionBox(int(x), int(y), int(z)))
    else:
        for line in input:
            x, y, z = line.strip().split(',')
            junction_boxes.append(JunctionBox(int(x), int(y), int(z)))

    return junction_boxes

def calc_distance(p, q):
    return math.sqrt(((p.x - q.x) ** 2) + ((p.y - q.y) ** 2) + ((p.z - q.z) ** 2))

def fetch_input():
    with open(f"2025_8_input.txt", "r") as file:
        return file.readlines()
    
def merge_circuits(a, b):
    if len(a.junction_boxes) >= len(b.junction_boxes):
        for element in b.junction_boxes:
            if element not in a.junction_boxes:
                a.junction_boxes.append(element)
        b.junction_boxes.clear()
    else:
        for element in a.junction_boxes:
            if element not in b.junction_boxes:
                b.junction_boxes.append(element)
        a.junction_boxes.clear()

def solve_part_one(input):    
    junction_boxes = parse_input(input, True)
    connections = []

    for i in range(0, len(junction_boxes)):
        for j in range(i + 1, len(junction_boxes)):
            box1 = junction_boxes[i]
            box2 = junction_boxes[j]
            connections.append(Connection(box1, box2, calc_distance(box1, box2)))

    connections.sort(key = lambda connection: connection.distance)

    circuits = []
    
    for connection in connections:
        circuit_handled = False
        for left_circuit in circuits:
            if circuit_handled:
                break

            if connection.a in left_circuit.junction_boxes:
                print(f"Box {connection.a} appeared in circuit {left_circuit}")
                left_circuit.junction_boxes.append(connection.b)
                
                for right_circuit in circuits:
                    if connection.b in right_circuit.junction_boxes and left_circuit != right_circuit:
                        print(f"")
                        merge_circuits(left_circuit, right_circuit)
                        if (len(left_circuit.junction_boxes) <= len(right_circuit.junction_boxes)):
                            circuits.remove(left_circuit)
                        else:
                            circuits.remove(right_circuit)

                        circuit_handled = True
                        break
            elif connection.b in left_circuit.junction_boxes and left_circuit != right_circuit:
                left_circuit.junction_boxes.append(connection.a)
                for right_circuit in circuits:
                    if connection.a in right_circuit.junction_boxes:
                        merge_circuits(left_circuit, right_circuit)
                        if (len(left_circuit.junction_boxes) <= len(right_circuit.junction_boxes)):
                            circuits.remove(left_circuit)
                        else:
                            circuits.remove(right_circuit)

                        circuit_handled = True
                        break
        
        if not circuit_handled:
            new_circuit = Circuit()
            new_circuit.junction_boxes.append(connection.a)
            new_circuit.junction_boxes.append(connection.b)
            circuits.append(new_circuit)
            print(f"New circuit created! {new_circuit}")
    
    circuits.sort(key = lambda circuit: len(circuit.junction_boxes))

    print(f"printin circuits")
    for circuit in circuits:
        print(circuit)
    
    solution = 1
    for i in range(0, 3):
        solution *= len(circuits[i].junction_boxes)

    for circuit in circuits:
        print(circuit)

    print(solution)

def solve_part_two(input):
    return None

solve_part_one(fetch_input())
