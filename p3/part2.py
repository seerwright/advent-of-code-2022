# Advent of Code 2022 

def main(input: list) -> None:
    # Input format
    #   String
    #       Even number of chars
    #       First half is compartment 1 items, second half is compartment 2
    #
    #   Example: aBcDEa

    # Objective
    #   Find items that appear in both rucksacks, determine their priority, return sum(priorities)

    priorities = []

    for list_of_stuff in input:
        c1, c2 = get_compartment_items(list_of_stuff[0])
        common_item = get_common_item(c1, c2)
        item_priority = get_priority_of_item(common_item)
        priorities.append(item_priority)

    print(priorities)
    print(f'Sum of priorities is {sum(priorities)}')

    return None

def get_priority_of_item(item: str) -> int:
    # a -> 97 ---- should start at 1
    # A -> 65 ---- should start at 27
    
    ordval = ord(item)
    if ordval >= 97:
        return ordval - 96
    else:
        return ordval - 38


def get_common_item(c1: str, c2: str) -> str:
    for item in c1:
        if item in c2:
            return item

def get_compartment_items(list_of_stuff: str) -> list:
    num_items = len(list_of_stuff)
    half_num = int(num_items/2)
    c1 = list_of_stuff[:half_num]
    c2 = list_of_stuff[-half_num:]
    return c1, c2

def read_input(filename: str) -> list:

    with open(filename) as f:
        file_as_list = []

        content = f.readlines()
        for line in content:
            file_as_list.append(line.split())

        return file_as_list

if __name__ == "__main__":
    problem_input = read_input('./input/part1.txt')
    main(problem_input)

