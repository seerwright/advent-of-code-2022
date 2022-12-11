# Advent of Code 2022 

import time

def main(input: list) -> None:
    instructions = [d.split() for d in input]

    # Scorekeeping
    reg = 1
    cycle = last_cycle = 1
    cycle_hist = {1: [1, 1]}

    # Build the values that occur at each cycle
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

        while last_cycle != cycle-1:
            last_reg = cycle_hist[last_cycle][0]
            last_cycle += 1
            interpolated_signal_strength = last_reg * last_cycle
            cycle_hist[last_cycle] = [reg, interpolated_signal_strength]

        last_cycle = cycle

    print(render(cycle_hist))

    return None

def render(cycle_hist: dict) -> None:
    # Really getting lazy with var names here...
    ch_keys = sorted(cycle_hist.keys())
    regvals = []
    for k in ch_keys:
        regvals.append(cycle_hist[k][0])

    # Eval of pixel location is at beginning of step, but my 
    # values are the final state of a cycle. Add another init state
    # to fix this. 
    regvals.insert(0, 1)

    # A screen is 6 rows
    screen = {r: [] for r in range(6)}

    # For every register value...
    for i in range(240):
        rownum = int(i/40)
        currpx = i%40

        regval = regvals[i]
        spritepx = [regval-1, regval, regval+1]
        if currpx in spritepx:
            screen[rownum].append('#')
        else:
            screen[rownum].append(' ')

    # Show the answer
    for printrow in range(6):
        print(''.join(screen[printrow]))

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
    