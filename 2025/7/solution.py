
# Advent of Code 2025 - Day 7

import functools

quantum_tachyon_manifold_diagram = None

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Splitter:
    def __init__(self, x, y):
        self.location = Location(x, y)
        
class Beam:
    def __init__(self, x, y):
        self.location = Location(x, y)

def parse_input(input, use_sample_input=False):
    sample_input = []
    sample_input.append('.......S.......')
    sample_input.append('...............')
    sample_input.append('.......^.......')
    sample_input.append('...............')
    sample_input.append('......^.^......')
    sample_input.append('...............')
    sample_input.append('.....^.^.^.....')
    sample_input.append('...............')
    sample_input.append('....^.^...^....')
    sample_input.append('...............')
    sample_input.append('...^.^...^.^...')
    sample_input.append('...............')
    sample_input.append('..^...^.....^..')
    sample_input.append('...............')
    sample_input.append('.^.^.^.^.^...^.')
    sample_input.append('...............')
    
    diagram = []
    start = None
    splitters = []
    
    if use_sample_input:
        for row, line in enumerate(sample_input):
            diagram.append([])
            for col, char in enumerate(line):
                diagram[row].append(char)
                
                if char == 'S':
                    start = Location(col, row)
                elif char == '^':
                    splitters.append(Splitter(col, row))
    else:
        for row, line in enumerate(input):
            diagram.append([])
            for col, char in enumerate(line):
                diagram[row].append(char)
                
                if char == 'S':
                    start = Location(col, row)
                elif char == '^':
                    splitters.append(Splitter(col, row))
            
    return diagram, start, splitters

def solve_part_one(input):
    diagram, start, splitters = parse_input(input, False)
    
    beams = set()
    beams.add(start.x)
    total_splits = 0
    
    for y in range(0, len(diagram) - 1):
        new_beams = set()
        for beam in beams:
            # does our beam run into a splitter?
            if diagram[y + 1][beam] == '^':
                # split it
                new_beams.add(beam - 1)
                new_beams.add(beam + 1)
                total_splits += 1
            else:
                # continue straight down
                new_beams.add(beam)
                
        # replace the beams set
        beams = new_beams  
    
    return total_splits
  
def get_timelines(beam, depth):
    if quantum_tachyon_manifold_diagram[depth + 1][beam] == '^':
        return [beam - 1, beam + 1]
    else:
        return [beam]

@functools.cache
def dfs(beam, get_timelines, depth):
    if depth == len(quantum_tachyon_manifold_diagram) - 1:
        return 1
    
    timelines = get_timelines(beam, depth)
    total_timelines = 0
    for timeline in timelines:
        total_timelines += dfs(timeline, get_timelines, depth + 1)
        
    return total_timelines

def solve_part_two(input):
    diagram, start, splitters = parse_input(input, False)
    
    global quantum_tachyon_manifold_diagram
    quantum_tachyon_manifold_diagram = diagram
    
    total_timelines = dfs(start.x, get_timelines, 0)
    
    return total_timelines 
