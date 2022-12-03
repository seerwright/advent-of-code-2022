# Advent of Code 2022 

def main(input: list) -> None:
    # Input format
    #   One integer or empty string per line
    #   If integer, it is part of a group of 1+ other integers
    #   If empty, you're about to start a new group
    #
    #   Example: [['6173'], [], ['7524'], ['5259'], ['1006'], ['8445']]

    # Objective
    #   Find out which three elves (calorie groups) are carrying the most (sum groups, get max, sort)
    #   Return the sum of the top three elves


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
    calorie_totals = sorted(calorie_totals)
    print(f'\nThe total of the top three elves is {sum(calorie_totals[-3:])}')

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

