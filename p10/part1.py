# Advent of Code 2022 

import time
from pprint import pprint

def main(input: list) -> None:
    instructions = [d.split() for d in input]

    reg = 1
    cycle = last_cycle = 1
    cycle_hist = {1: [0, 0]}

    signal_strengths = []

    print(f'Cycle\tOp\tArg\tSig Str\tReg\n===============================')
    print(f'{cycle}\tINIT\tINIT\t0\t0')

    for idx, instruction in enumerate(instructions):
        op = instruction[0]
        arg = int(instruction[1]) if len(instruction) == 2 else None
        ss = '.'

        if op == 'noop':
            cycle += 1
        else:
            reg += arg
            cycle += 2

        signal_strength = cycle * reg
        cycle_hist[cycle] = [reg, signal_strength]

        if cycle == 20 or (cycle-20)%40 == 0:
            signal_strengths.append(signal_strength)

        print(f'{cycle}\t{op}\t{arg}\t{ss}\t{reg}')


        while last_cycle != cycle-1:
            last_reg = cycle_hist[last_cycle][0]
            last_cycle += 1
            interpolated_signal_strength = last_reg * last_cycle
            cycle_hist[last_cycle] = [reg, interpolated_signal_strength]

            if last_cycle == 20 or (last_cycle-20)%40 == 0:
                signal_strengths.append(interpolated_signal_strength)

        last_cycle = cycle


    print(f'The sum of the {len(signal_strengths)} is {sum(signal_strengths)}')

    return None

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
    start_time = time.time()

    # Get input
    problem_input = read_input('./input/part1.txt', False)
    
    input_time = time.time()

    # Solve
    main(problem_input)

    end_time = time.time()
    
    # Report out execution time
    print('\n\n---------- Script Performance ------')
    print("Get Input", (input_time - start_time) * 10**3, "ms")
    print("Solve", (end_time - input_time) * 10**3, "ms")
    print("------------------------------------")
    print("Total Time", (end_time - start_time) * 10**3, "ms")
    print('\n\n')
    