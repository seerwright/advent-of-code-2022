# Advent of Code 2022 

def main(input: list) -> None:
    # Input format
    #   String
    #       Even number of chars
    #       First half is compartment 1 items, second half is compartment 2
    #
    #   Example: aBcDEa

    # Objective
    #   Get sum of priorities for single item common to each elven threesome

    # Keep track of a few things...
    priorities = []
    done = False
    elf_groups = int(len(input)/3)
    current_elf_group = 0

    # Handle in groups of three
    while not done:
        group_stuff = input[3*current_elf_group:3*current_elf_group+3]
        
        common_group_item = get_common_group_item(group_stuff)

        priority_of_item = get_priority_of_item(common_group_item)
        priorities.append(priority_of_item)

        current_elf_group += 1
        if current_elf_group >= elf_groups:
            done = True


    print(priorities)
    print(f'Sum of priorities of elven group items is {sum(priorities)}')

    return None

def get_priority_of_item(item: str) -> int:
    # a -> 97 ---- should start at 1
    # A -> 65 ---- should start at 27
    
    ordval = ord(item)
    if ordval >= 97:
        return ordval - 96
    else:
        return ordval - 38

def get_common_group_item(group_stuff: list) -> str:
    elf1, elf2, elf3 = group_stuff
    for item in elf1[0]:
        if item in elf2[0] and item in elf3[0]:
            return item

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

