# Advent of Code 2022 

def main(input: list) -> None:
    # Input format
    #   String of two comma-separated ranges
    #       Each range is an elf's assigned areas
    #       A range is complete, no gaps. Inclusive of the bookends
    #
    #   Example: "2-6,4-8" means one elf has 2,3,4,5,6 and the other has 4,5,6,7,8

    # Objective
    #   Count of pairs where one range is completely in the other

    insider_count = 0

    for pair in input:
        elf1, elf2 = pair[0].split(',')
        is_inside = False

        if is_inside_other(elf1, elf2):
            is_inside = True
        if is_inside_other(elf2, elf1):
            is_inside=True

        if is_inside:
            insider_count += 1

    print(f'Number of pairs where one range is fully inside the other is {insider_count}')        

    return None

def is_inside_other(rng1: str, rng2: str) -> bool:
    begin1, end1 = rng1.split('-')
    begin2, end2 = rng2.split('-')
    if (int(begin1) >= int(begin2)) and (int(end1) <= int(end2)):
        return True
    else:
        return False

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

