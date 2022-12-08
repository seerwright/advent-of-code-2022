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
    trees = trees.tolist()

    # Keep track of trees seen
    trees_seen = {}

    # Look at trees across rows, rotate, repeat
    trees_seen = rotate_and_scan(trees, 0, trees_seen)
    print('\n ---------- ROTATE 1 ! -------------')
    trees_seen = rotate_and_scan(trees, 1, trees_seen)
    print('\n ---------- ROTATE 2 ! -------------')
    trees_seen = rotate_and_scan(trees, 2, trees_seen)
    print('\n ---------- ROTATE 3 ! -------------')
    trees_seen = rotate_and_scan(trees, 3, trees_seen)
    
    # Let's see all the trees
    pprint(trees_seen)

    # Print the answer
    print(f'There are {len(trees_seen.keys())} trees visible.')

    return None

def rotate_and_scan(trees: npt.ArrayLike, rot: int = 0, trees_seen: dict = {}) -> dict:

    width, height = len(trees[0]), len(trees)
    # Same size matrix, but this one contains coords
    cmap = make_coordinate_map(width, height, rot)

    # Probably not necessary now since the zip makes a copy
    t = deepcopy(trees)

    # Rotate the trees data
    for _ in range(rot):
        t = list(zip(*reversed(t)))

    # Tally up the visible trees
    for w in range(width):
        tallest_tree = -1
        for h in range(height):
            print(f'Value at [w, h] [cmap[w, h]] is {t[w][h]}')
            this_height = t[w][h]
            if this_height > tallest_tree:
                if cmap[w][h] not in trees_seen:
                    trees_seen[cmap[w][h]] = f'Set a new record in this lane with {this_height}'
                tallest_tree = this_height
    return trees_seen

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
    