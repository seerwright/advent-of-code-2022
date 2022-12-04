# Advent of Code 2022 

def main(input: list) -> None:
    # Input format
    #   String of two comma-separated ranges
    #       Each range is an elf's assigned areas
    #       A range is complete, no gaps. Inclusive of the bookends
    #
    #   Example: "2-6,4-8" means one elf has 2,3,4,5,6 and the other has 4,5,6,7,8

    # Objective
    #   Count of pairs where one range overlaps the other range at all

    overlap_count = 0

    for pair in input:
        elf1, elf2 = pair[0].split(',')
        is_overlap = False

        if is_overlapped(elf1, elf2):
            is_overlap = True
        if is_overlapped(elf2, elf1):
            is_overlap=True

        if is_overlap:
            overlap_count += 1

    print(f'Number of pairs where one range is overlapped with the other is {overlap_count}')        

    return None

def is_overlapped(rng1: str, rng2: str) -> bool:
    begin1, end1 = rng1.split('-')
    begin2, end2 = rng2.split('-')

    # Does the begining value fall between the target begin/end?
    # or
    # Does the ending value fall between the target begin/end? 

    if (int(begin1) <= int(end2)) and (int(begin1) >= int(begin2)):
        return True
    elif (int(end1) <= int(end2)) and (int(end1) >= int(begin2)):
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

