# Advent of Code 2024 - Day 11

import functools

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def append(self, data):
        self.size += 1
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            
        current_node.next = new_node
        
def parse_input(input):
    linked_list = LinkedList()
    
    for digit in list(map(int, input[0].split())):
        linked_list.append(digit)
    
    return linked_list

def solve_part_one(input):
    linked_list = parse_input(input)
    num_blinks = 25
    
    for _ in range(num_blinks):
        current_node = linked_list.head
        while current_node:
            data_str = str(current_node.data)
            
            # Rule no. 1: If the the stone is engraved with the num 0, it is replace by a stone engraved with the num 1.
            if current_node.data == 0:
                current_node.data = 1
                
            # Rule no. 2: If the stone is engraved with a num with an even number of digits, it is replaced by two stones.
            # The left half of the digits on one stone, the right half of the digits on another. (Leading zeroes are not kept)
            elif len(data_str) % 2 == 0:
                left_half = int(data_str[:int(len(data_str) / 2)])
                right_half = int(data_str[int(len(data_str) / 2):])
                current_node.data = left_half
                
                # Create the new node and increment the size of linked list
                new_node = Node(right_half)
                linked_list.size += 1
                
                # Insert the new node into the linked list
                new_node.next = current_node.next
                current_node.next = new_node
                
                # We don't want to "process" this new node during this blink, so lets move our current node forward
                current_node = new_node
            
            # Rule no. 3: If none of the other rules apply, the stone is replaced by a new stone with the old number multiplied by 2024
            else:
                current_node.data *= 2024
            
            # Move to the next node
            current_node = current_node.next
    
    return linked_list.size

@functools.cache
def dfs(node, get_neighbors, depth):
    if depth == 0:
        return 1
    
    neighbors = get_neighbors(node)
    total_count = 0
    for neighbor in neighbors:
        total_count += dfs(neighbor, get_neighbors, depth - 1)
        
    return total_count

def get_neighbors(node):
    neighbors = []
    node_str = str(node)
    
    # Rule no. 1: If the the stone is engraved with the num 0, it is replace by a stone engraved with the num 1.
    if node == 0:
        neighbors.append(1)
        
    # Rule no. 2: If the stone is engraved with a num with an even number of digits, it is replaced by two stones.
    # The left half of the digits on one stone, the right half of the digits on another. (Leading zeroes are not kept)
    elif len(node_str) % 2 == 0:
        neighbors.extend([int(node_str[:int(len(node_str) / 2)]), int(node_str[int(len(node_str) / 2):])])
        
    # Rule no. 3: If none of the other rules apply, the stone is replaced by a new stone with the old number multiplied by 2024
    else:
        neighbors.append(node * 2024)
        
    return neighbors

def solve_part_two(input):    
    total_stones = 0
    stones = list(map(int, input[0].split()))
    
    for stone in stones:
        total_stones += dfs(stone, get_neighbors, 75)
    
    return total_stones
