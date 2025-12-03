# Advent of Code 2024 - Day 23

def get_connections(input):
    connections = {}
    
    for line in input:
        connection = line.split('-')
        left = connection[0]
        right = connection[1]
        
        if left in connections:
            connections[left].append(right)
        else:
            connections[left] = [right]
            
        if right in connections:
            connections[right].append(left)
        else:
            connections[right] = [left]
        
    return connections

def get_groups(connections):
    groups = []
    
    for start_node in connections:
        connected_nodes = connections[start_node]
        for connected_node in connected_nodes:
            sub_connections = connections[connected_node]
            for sub_connection in sub_connections:
                if start_node in connections[sub_connection]:
                    group = set((start_node, connected_node, sub_connection))
                    if group not in groups:
                        groups.append(group)          
       
    return groups 

def solve_part_one(input):
    connections = get_connections(input)
    groups = get_groups(connections)
    
    groups_with_t_count = 0
    for group in groups:
        for node in group:
            if node[0] == 't':
                groups_with_t_count += 1
                break
    
    return groups_with_t_count

def bron_kerbosch(current_clique, potential_nodes, processed_nodes, adjacency_list):
    if not potential_nodes and not processed_nodes:
        yield current_clique
        
    while potential_nodes:
        v = potential_nodes.pop()
        yield from bron_kerbosch(
            current_clique.union({v}), 
            potential_nodes.intersection(adjacency_list[v]), 
            processed_nodes.intersection(adjacency_list[v]), 
            adjacency_list
        )
        processed_nodes.add(v)

def solve_part_two(input):
    adjacency_list = get_connections(input)
    all_cliques = list(bron_kerbosch(set(), set(adjacency_list.keys()), set(), adjacency_list))
    largest_clique = sorted(max(all_cliques, key = len))
    password = ",".join(largest_clique)
    return password
