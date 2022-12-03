# Advent of Code 2022 



def main(input: list) -> None:
    # Input format
    #   One integer or empty string per line
    #   If integer, it is part of a group of 1+ other integers
    #   If empty, you're about to start a new group
    #
    #   Example: [['6173'], [], ['7524'], ['5259'], ['1006'], ['8445']]

    # Objective
    #   Find out which elf (calorie group) is carrying the most (sum groups, get max)


    # Keep track of stuff
    calorie_totals = []
    this_calorie_total = 0

    # Total the groups
    for calorie in input:
        if calorie != []:
            this_calorie_total += int(calorie[0])
        else:
            calorie_totals.append(this_calorie_total)
            this_calorie_total = 0

    # Solve the problem
    print(f'\nThe elf with the most calories has {max(calorie_totals)} calories.')

    return None

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

