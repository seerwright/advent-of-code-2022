# Advent of Code 2022 

import numpy as np
import sys

def main(input: list) -> None:
    moves = [d.split() for d in input]
    moves = expand_move_list(moves)

    h = [0, 0]
    t = [0, 0]

    tail_visits = {fmt_key(t): 'Merry Christmas!'}

    for idx, m in enumerate(moves):

        # print(f'#{idx} BEFORE H move:\tm {m}\th {h}\tt {t}\tadjacent? {is_adj(h, t)}')
        h = do_move(m, h)
        is_a = is_adj(h, t)
        # print(f'#{idx} AFTER H move:\tm {m}\th {h}\tt {t}\tadjacent? {is_adj(h, t)}')
        if not is_a:
            t = move_t(t, h)
            if fmt_key(t) not in tail_visits:
                tail_visits[fmt_key(t)] = 'Merry Christmas!'
            dir, dst = m[0], int(m[1])
            # print(f'#{idx} AFTER T move:\tm {m}\th {h}\tt {t}\tadjacent? {is_adj(h, t)}')
        # print('------------------------------------------------')


    # print_board(15, h, t, tail_visits)  
    # print()
    print(f'Tail visited {len(tail_visits.keys())} locations.')

    return None

def print_board(size: int, h: list, t: list, visited: dict = None) -> None:
    offset = int(size/2)
    board = [['.'] * size for _ in range(size)]
    board[h[1]-offset][h[0]+offset] = 'H'
    board[t[1]-offset][t[0]+offset] = 'T'

    if visited:
        for v in visited.keys():
            vx, vy = v.split(',')
            board[int(vy)-offset][int(vx)+offset] = '#'
    pretty = [''.join(row) for row in board]
    print('\n'.join(pretty))


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
        if abs(hx-tx) > 1:
            new_tx = int((hx+tx)/2)
            new_ty = hy
        else:
            new_tx = hx
            new_ty = int((ty+hy)/2)
        return [new_tx, new_ty]
    else:
        # What am I forgetting?
        print('move_t does not have full coverage!!!')
        return None
        




    if abs(tx-hx) > abs(ty-hy):

        new_t = [tx + (hx - tx), ty]
    else:
        new_t = [tx, ty + (hy - ty)]

    # Check one more time because the above may not
    # have fixed it, but one more move definitely will
    if is_adj(h, new_t):
        return new_t
    else:
        print(f'Not adjacent between {h} and {new_t}')
        return move_t(new_t, h)

def is_adj(hc: list, tc: list) -> bool:
    d = ((hc[0] - tc[0])**2 + (hc[1] - tc[1])**2)**0.5
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
    problem_input = read_input('./input/part1.txt', False)
    main(problem_input)
    