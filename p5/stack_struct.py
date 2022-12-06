# Advent of Code 2022 

from copy import deepcopy
import numpy as np


def main(input: list) -> None:
    # Part 1 of 2: Stack stuff
    stack_raw_data = input[:input.index('')]
    stack_ids = [i for i in stack_raw_data[-1]]
    stack_id_positions = [i for i,x in enumerate(stack_ids) if x != ' ']

    # Capture the stack with named stack IDs for us humans
    stack_struct_vert = {}
    for col in stack_id_positions:
        stack_struct_vert[col] = None
        this_stack = []
        
        for row in stack_raw_data[:-1]:
            this_stack.append(row[col])

        stack_struct_vert[col] = this_stack

    # Get just the crates as lists
    stack = []
    for k in sorted(stack_struct_vert.keys()):
        stack.append(stack_struct_vert[k])

    # Use numpy to flip array so left is bottom
    stack = np.array(stack)
    stack = stack[:,::-1]
    stack = stack.tolist()
    stack = [[item for item in substack if item != ' '] for substack in stack]

    # Part 2 of 2: Instruction stuff
    instructions = []
    instructions_raw_data = input[input.index('')+1:]
    for row in instructions_raw_data:
        pieces = row.split()
        instructions.append([int(pieces[1]), int(pieces[3]), int(pieces[5])])

    # Do all the moves
    for instruction in instructions:
        stack = do_move(stack, instruction)

    # Print out the answer / all top crates
    top_crates = ''.join([column[-1] for column in stack])
    print(top_crates)
    
    return None

def do_move(stack_state: list, instruction: list) -> list:
    crates_to_move = instruction[0]
    from_crate = instruction[1]
    to_crate = instruction[2]

    s = deepcopy(stack_state)
    for i in range(crates_to_move):
        crate = s[from_crate-1].pop()
        s[to_crate-1].append(crate)

    return s

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
    problem_input = read_input('./input/part1_test.txt', False)
    main(problem_input)

