# Advent of Code 2024 - Day 5

def parse_input(input):
    in_updates = False
    rules = []
    updates = []

    for line in input:
        if line == "":
            in_updates = True
            continue

        if not in_updates:
            rules.append(line)
        else:
            updates.append(line)

    return rules, updates

def find_middle(pages):
    return int(pages[int(len(pages) / 2)])

def solve_part_one(input):
    total_sum = 0
    rules, updates = parse_input(input)

    # value : all the values it must be before
    rule_map = {}

    # Parse through rules
    for rule in rules:
        parsed_rule = rule.split("|")
        key, value = parsed_rule[0], parsed_rule[1]

        if key in rule_map:
            rule_map[key].append(value)
        else:
            rule_map[key] = [value]

    # Alright, lets read through the updates
    for update in updates:
        prev_nums = []
        pages = update.split(",")
        valid = True
        
        for page in pages:
            # all the values that must come AFTER it
            rules = rule_map[page]
            if set(prev_nums) & set(rules):
                valid = False
                break

            prev_nums.append(page)

        if valid:
            total_sum += find_middle(pages)

    return total_sum

def solve_part_two(input):
    total_sum = 0
    rules, updates = parse_input(input)

    # value : all the values it must be before
    rule_map = {}

    # Parse through rules
    for rule in rules:
        parsed_rule = rule.split("|")
        key, value = parsed_rule[0], parsed_rule[1]

        if key in rule_map:
            rule_map[key].append(value)
        else:
            rule_map[key] = [value]

    # Alright, lets read through the updates to find the invalid ones
    invalid_updates = []
    for update in updates:
        prev_nums = []
        pages = update.split(",")
        valid = True
        
        for page in pages:
            # all the values that must come AFTER it
            if page in rule_map:
                rules = rule_map[page]
            else:
                rules = []
                
            if set(prev_nums) & set(rules):
                valid = False
                invalid_updates.append(update)
                break

            prev_nums.append(page)

    # Finally, lets sort out the invalid updates and make them VALID!
    for update in invalid_updates:
        
        prev_nums = []
        pages = update.split(",")
        index = 0

        while index < len(pages):
            # all the values that must come AFTER it
            if pages[index] in rule_map:
                rules = rule_map[pages[index]]
            else:
                rules = []

            # Okay, we have an intersection. Let's look a little deeper...
            if set(prev_nums) & set(rules):
                for prev_nums_index, prev_num in enumerate(prev_nums):
                    if prev_num in rules:
                        dirty_rotten_rule_breaker = prev_nums[prev_nums_index]
                        index_of_offender = pages.index(dirty_rotten_rule_breaker)
                        current_num = pages[index]
                        
                        # Swap the offender and the current num
                        prev_nums[prev_nums_index] = current_num
                        pages[index] = dirty_rotten_rule_breaker
                        
                        # Put the original number back where the offender was
                        pages[index_of_offender] = current_num
                        
                        # Reset index back to 0 because we are a brute force FREAK
                        index = 0
                        prev_nums = []
                        break
            else:
                prev_nums.append(pages[index])
                index += 1

        total_sum += find_middle(pages)
                   
    return total_sum
