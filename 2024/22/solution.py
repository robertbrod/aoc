# Advent of Code 2024 - Day 22

def parse_input(input):
    return list(map(int, input))

def mix(value, secret_number):
    return value ^ secret_number

def prune(secret_number):
    return secret_number % 16777216

def get_next_secret_number(secret_number, depth):
    for i in range(depth):
        # step one
        secret_number = prune(mix(secret_number * 64, secret_number))

        # step two
        secret_number = prune(mix(secret_number // 32, secret_number))

        # step three
        secret_number = prune(mix(secret_number * 2048, secret_number))

    return secret_number

def get_price_changes(secret_number, depth):
    price_changes = []
    price_changes.append((secret_number % 10, None))
    last_price = secret_number % 10

    for i in range(depth - 1):
        # step one
        secret_number = prune(mix(secret_number * 64, secret_number))

        # step two
        secret_number = prune(mix(secret_number // 32, secret_number))

        # step three
        secret_number = prune(mix(secret_number * 2048, secret_number))

        # add the price change
        price_changes.append((secret_number % 10, (secret_number % 10) - last_price))
        last_price = secret_number % 10 

    return price_changes

def get_price_dict(price_changes):
    price_dict = {}

    for index, price_change in enumerate(price_changes):
        if index < 4:
            continue

        price = price_change[0]
        if price > 0:
            price_change_signal = ",".join(str(p[1]) for p in price_changes[index - 3: index + 1])
            if price_change_signal not in price_dict:
                price_dict[price_change_signal] = price

    return price_dict

def solve_part_one(input):
    secret_numbers = parse_input(input)
    sum_of_secret_numbers = 0

    for secret_number in secret_numbers:
        sum_of_secret_numbers += get_next_secret_number(secret_number, 2000)

    return sum_of_secret_numbers

def solve_part_two(input):
    secret_numbers = parse_input(input)
    price_change_signals = {}
    
    for secret_number in secret_numbers:
        price_changes = get_price_changes(secret_number, 2000)
        price_dict = get_price_dict(price_changes)
        for key in price_dict:
            if key in price_change_signals:
                price_change_signals[key] += price_dict[key]
            else:
                price_change_signals[key] = price_dict[key]

    max_num_bananas = 0
    for price_change_signal in price_change_signals.values():
        if price_change_signal > max_num_bananas:
            max_num_bananas = price_change_signal

    print(price_change_signals['-2,1,-1,3'])

    return None