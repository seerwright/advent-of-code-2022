# Advent of Code 2022 

def main(input: list) -> None:
    # Input format
    #   Two characters
    #   Char 1 = [A | B | C]
    #   Char 1 = [X | Y | Z]
    #
    #   Example: [['A', 'X'], ['C', 'Z']]

    # Objective
    #   Get the total points for all RPS rounds in the input file

    winning_strategy = get_winning_strategy()
    match_points = get_match_points()

    tournament_total = 0

    print(f'a1\ta2\toutcome\ts_pts\tm_pts\tr_pts\tt_total')



    for round_actions in input:
        round_outcome, selection_score = is_winner(actions=round_actions, 
                                                   winning_strategy=winning_strategy)
        match_score = match_points[round_outcome]
        round_score = selection_score + match_score
        tournament_total += round_score
        print(f'{round_actions[0]}\t{round_actions[1]}\t{round_outcome}\t{selection_score}\t{match_score}\t{round_score}\t{tournament_total}')
    
    print(f'Tournament Total is {tournament_total}')

    return None


def get_match_points() -> dict:
    return {
        'lose': 0,
        'draw': 3,
        'win': 6
    }

def is_winner(actions: list, winning_strategy: dict) -> list:
    # Given two actions, opponent and player, return
    # is winner (str) and points for selection (int)
    opponent_action = actions[0]
    winning_response, winning_points = winning_strategy[opponent_action]
    actual_response = actions[1]
    actual_points = get_selection_point_map(actual_response)


    if get_selection_point_map(opponent_action) == get_selection_point_map(actual_response):
        return 'draw', actual_points
    elif actual_response == winning_response:
        return 'win', winning_points
    else:
        return 'lose', actual_points

def get_winning_strategy() -> dict:
    # This strategy tells you what you will return 
    # as a function of what the opponent does, plus 
    # you get the selection points.
    return {
        'A': ['Y', get_selection_point_map('Y')],
        'B': ['Z', get_selection_point_map('Z')],
        'C': ['X', get_selection_point_map('X')]
    }

def get_selection_point_map(action: str) -> int:
    score_map = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    return score_map[action]


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

