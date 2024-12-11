# Advent of Code 2024 - Day 11

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

def solve_part_two(input):
    
    return None
