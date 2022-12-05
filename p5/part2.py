# Advent of Code 2022 

from copy import deepcopy


def main(input: list) -> None:
    # Input format
    #   Example
    #       [D]    
    #       [N] [C]    
    #   [Z] [M] [P]
    #    1   2   3 

    #   move 1 from 2 to 1  //Interpret as move 1 crate from stack 2 to stack 1 (one at a time)
    #   move 3 from 1 to 3
    #   move 2 from 2 to 1
    #   move 1 from 1 to 2
    #       

    # Objective
    #   Determine which crate which be on top of each stack

    parsed_input_data = parse_initial_stack(input)
    initial_stack, instructions = parsed_input_data['initial_stack'], parsed_input_data['instructions']

    new_stack = initial_stack
    for instruction in instructions:
        print(new_stack)
        new_stack = do_move(new_stack, instruction)
        print(instruction)
        print(new_stack)
        print('------------------------------')

    top_crates = []
    for stack in new_stack:
        top_crates.append(stack[-1])

    print(f"Top crates are {''.join(top_crates)}")
    return None


def do_move(stack_state: list, instruction: list) -> list:
    # Input:  current stack state and instruction to execute
    # Return: new stack state
    crates_to_move = instruction[0]
    from_crate = instruction[1]
    to_crate = instruction[2]

    s = deepcopy(stack_state)

    s[to_crate-1].extend(s[from_crate-1][-crates_to_move:])
    s[from_crate-1] = s[from_crate-1][:-crates_to_move]

    return s

def parse_initial_stack(input_data: list) -> dict:
    # Return a dict with lists for both the stack and instructions
    separator_row = input_data.index('')
    
    # Stack
    initial_stack_rows = input_data[:separator_row]
    stack_as_list = format_stack(initial_stack_rows)
    # Rotate so we can pop and push
    stack_as_list = rotate_stack(stack_as_list)

    # Insttructions
    instruction_rows = input_data[separator_row+1:]
    instructions = format_instructions(instruction_rows)

    return {'initial_stack': stack_as_list, 'instructions': instructions}

def format_instructions(unformatted_instructions: list) -> list:
    # Input:  move 1 from 2 to 1
    # Return: ['1', '2', '1']
    instructions = []
    for row in unformatted_instructions:
        pieces = row.split()
        instructions.append([int(pieces[1]), int(pieces[3]), int(pieces[5])])
    return instructions


def rotate_stack(stack: list) -> list:
    rot_stack = zip(*reversed(stack))
    rot_stack = [list(crates) for crates in rot_stack]

    clean_stack = []
    for stack in rot_stack:
        clean_stack.append([x for x in stack if x != ' '])

    return clean_stack

def format_stack(unformatted_stack: list) -> list:
    # Input
    #   ['    [D]    ', '[N] [C]    ', '[Z] [M] [P]', ' 1   2   3 ']
    # Return
    #   [[' ', 'D', ' '], ['N', 'C', ' '], ['Z', 'M', 'P'], ['1', '2', '3']]

    stack_ids = unformatted_stack[-1].split()
    num_stacks = max([int(i) for i in stack_ids])
    data_cols = get_stack_data_map(num_stacks)
    
    stacks_as_list = []
    for row in unformatted_stack:
        this_row = []
        for data_col in data_cols:
            this_row.append(row[data_col])
        stacks_as_list.append(this_row)

    return stacks_as_list[:-1]

def get_stack_data_map(num_stacks) -> list:
    # ' 1   2   3 '
    # '0123456789...
    # We need to know index positions of the numbers: 1, 5, 9  
    data_cols = [i for i in range(1, num_stacks*4 ,4)]
    return data_cols[:num_stacks]

def read_input(filename: str, split_ws: bool = True) -> list:
    # Split on whitespace by default, otherwise return whole string
    with open(filename) as f:
        file_as_list = []

        content = f.readlines()
        for line in content:
            if split_ws:
                file_as_list.append(line.split())
            else:
                file_as_list.append(line.strip('\n'))

        return file_as_list

if __name__ == "__main__":
    problem_input = read_input('./input/part1.txt', False)
    main(problem_input)

