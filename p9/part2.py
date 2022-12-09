# Advent of Code 2022 

import time

def main(input: list) -> None:
    moves = [d.split() for d in input]
    moves = expand_move_list(moves)

    # Rope with ten knots + adjacency pairs for convenience
    num_knots = 10
    rope = [[0, 0] for _ in range(num_knots)]
    adjacency_pairs = list(zip([i for i in range(num_knots)][:-1], [i for i in range(num_knots)][1:]))
    num_adj_pairs = len(adjacency_pairs)

    # Track these because that's the whole point of this exercise!
    tail_visits = {fmt_key(rope[0]): None}

    # Do all the moves
    for idx, m in enumerate(moves):

        # Move the head
        rope[0] = do_move(m, rope[0])

        # Move the body
        for knot_num, a in enumerate(adjacency_pairs):
            last_knot = True if (knot_num +1) == num_adj_pairs else False

            is_adjacent = is_adj(rope[a[0]], rope[a[1]])

            if not is_adjacent:
                rope[a[1]] = move_t(rope[a[1]], rope[a[0]])

            if last_knot:
                if fmt_key(rope[-1]) not in tail_visits:
                    tail_visits[fmt_key(rope[-1])] = None

    print(f'\n\nTail visited {len(tail_visits.keys())} locations.')
    return None

def print_board(size: int, rope: list, visited: dict = None) -> None:
    offset = int(size/2)
    board = [['.'] * size for _ in range(size)]

    if visited:
        for v in visited.keys():
            vx, vy = v.split(',')
            board[int(vy)-offset][int(vx)+offset] = '#'

    for idx, r in enumerate(rope):
        board[r[1]-offset][r[0]+offset] = str(idx)

    board.reverse()
    pretty = [''.join(row) for row in board]
    print('\n'.join(pretty))
    return None

def fmt_key(t: list) -> str:
    return ','.join(str(c) for c in t)

def move_t(t, h) -> list:
    tx, ty = t
    hx, hy = h
    new_t = None
    if hx == tx:
        # Same row, must be col move to the avg
        return [tx, int((ty+hy)/2)]
    elif hy == ty:
        # Opposite
        return [int((tx+hx)/2), ty]
    elif hx != tx and hy != ty:
        # Need to move in BOTH directions
        new_tx = new_ty = None

        if get_distance(t, h) < 2.8:
        # You will only encounter this on Part 1
            if abs(hx-tx) > 1:
                new_tx = int((hx+tx)/2)
                new_ty = hy
            else:
                new_tx = hx
                new_ty = int((ty+hy)/2)
        else:
        # This is possible on Part 2
            new_tx = int((hx+tx)/2)
            new_ty = int((ty+hy)/2)
        return [new_tx, new_ty]

    else:
        return None
        
def get_distance(p1: list, p2: list) -> float:
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def is_adj(hc: list, tc: list) -> bool:
    d = get_distance(hc, tc)
    # d == 1: horizontal or vertical offset
    # 1 < d < 1.415: one diag away
    # d > 1.415: far away
    # ONLY NEED TO MOVE if 'far away'
    if d < 1.415:   
       return True
    else:
        # Far away
        return False 

def expand_move_list(moves: list) -> list:
    e = []
    for m in moves:
        dir, dst = m[0], int(m[1])
        for _ in range(dst):
            e.append([dir, 1])
    return e

def do_move(m: list, h: list) -> list:
    dir, dst = m
    if dir == 'R':
        return [h[0]+dst, h[1]]
    elif dir == 'L':
        return [h[0]-dst, h[1]]
    elif dir == 'D':
        return [h[0], h[1]-dst]
    elif dir == 'U':
        return [h[0], h[1]+dst]
    else:
        return h

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
    