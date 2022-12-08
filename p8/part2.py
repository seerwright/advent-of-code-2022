# Advent of Code 2022 

from copy import deepcopy
import numpy as np
import numpy.typing as npt
from pprint import pprint

def main(input: list) -> None:

    # Prep trees data
    trees = [[*x] for x in input]
    trees = np.array(trees)
    trees = trees.astype(int)

    width, height = trees.shape
    
    cmap = make_coordinate_map(width, height, 0)
    cmap_rot = make_coordinate_map(width, height, 3)


    scores = []

    # For each tree, calc the scenic score
    for w in range(width):
        for h in range(height):
            scores.append(get_scenic_score(trees, w, h, cmap, cmap_rot))

    print(f'Top scenic score is {max(scores)}')

    return None

def get_scenic_score(trees: npt.ArrayLike, w: int, h: int, cmap: list, cmap_rot: list) -> int:
    total_w, total_h = trees.shape


    coord = cmap[w][h]
    my_height = trees[w][h]

    l_vis = 0
    r_vis = 0
    u_vis = 0
    d_vis = 0

    this_row = trees[w,:]

    left_slice = this_row[:h]
    left_slice = np.flip(left_slice)
    l_vis = get_visibility(left_slice, my_height)

    right_slice = this_row[h+1:]
    r_vis = get_visibility(right_slice, my_height)
    

    new_w, new_h = None, None
    for cw in range(total_w):
        for ch in range(total_h):
            if cmap_rot[cw][ch] == coord:
                new_w, new_h = cw, ch
                break


        
    t_trees = np.rot90(trees)

    this_row = t_trees[new_w,:]


    left_slice = this_row[:new_h]
    left_slice = np.flip(left_slice)
    u_vis = get_visibility(left_slice, my_height)

    right_slice = this_row[new_h+1:]
    d_vis = get_visibility(right_slice, my_height)


    return l_vis * r_vis * u_vis * d_vis


def get_visibility(slice: npt.ArrayLike, h: int) -> int:
    s = list(slice)
    v = 0
    if s:    
        for e in s:
            if h > e:
                v += 1
            elif h <= e:
                v += 1
                break
            else:
                break
    else: 
        return 0

    return v

def make_coordinate_map(w: int, h: int, rot: int = 0) -> list:
    c = []
    for width in range(w):
        r = []
        for height in range(h):
            r.append(f'{str(width)}X{str(height)}')
        c.append(r)

    for _ in range(rot):
        c = list(zip(*reversed(c)))

    return c

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
    