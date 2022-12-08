# Advent of Code 2022 

from copy import deepcopy
import numpy as np
import numpy.typing as npt
from pprint import pprint
import sys

def main(input: list) -> None:

    # Prep trees data
    trees = [[*x] for x in input]
    trees = np.array(trees)
    trees = trees.astype(int)
    width, height = trees.shape

    cmap = get_cmap_with_rotated_coordinates(width, height)

    # Keep track of scenic scores
    scores = []

    # For each tree, calc the scenic score
    for w in range(width):
        for h in range(height):
            scores.append(get_scenic_score(trees, w, h, cmap))
    
    print(f'Top scenic score is {max(scores)}')

    return None


def get_cmap_with_rotated_coordinates(width: int, height: int) -> dict:
    # Coordinate map and rotated positions
    cmap = make_coordinate_map(width, height, 0)
    cmap_rot = make_coordinate_map(width, height, 1)
    
    # Lazy...
    def convert_split(a):
        return int(a[0]), int(a[1])
    
    # Convert to dictionary for O(1) lookups!
    cmap = {coord: [convert_split(coord.split('X'))] for sublist in cmap for coord in sublist}
    
    # For each item in the rotated map, get it's new x,y for the prev coord
    for row_num, row in enumerate(cmap_rot):
        for col_num, col in enumerate(row):
            x, y = row_num, col_num
            coord_id = col
            cmap[f'{x}X{y}'].append(convert_split(col.split('X')))

    # cmap_rot = {coord: convert_split(coord.split('X')) for sublist in cmap_rot for coord in sublist}
    return cmap


def get_scenic_score(trees: npt.ArrayLike, w: int, h: int, cmap: list) -> int:
    coord = f'{w}X{h}'
    my_height = trees[w][h]

    l_vis = r_vis = u_vis = d_vis = 0

    # Part 1 of 2: Look left and right first
    this_row = trees[w,:]

    left_slice = this_row[:h]
    left_slice = np.flip(left_slice)
    l_vis = get_visibility(left_slice, my_height)

    right_slice = this_row[h+1:]
    r_vis = get_visibility(right_slice, my_height)
    
    # Part 2 of 2: Rotate the map, then look left and right again
    new_w, new_h = cmap[coord][1]
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
    # A little goofy, but ...
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
    