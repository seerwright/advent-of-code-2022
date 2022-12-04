# Advent of Code 2022 

def main(input: list) -> None:
    # Input format
    #   Two characters
    #   Char 1 = [A | B | C]  // This is the opponent's action
    #   Char 2 = [X | Y | Z]  // The outcome you must effect
    #
    #   Example: [['A', 'X'], ['C', 'Z']]

    # Objective
    #   Get the total points for all RPS rounds in the input file

    match_points = get_match_points()
    match_outcomes = get_match_outcome_map()
    action_points_map = get_action_points_map()

    tournament_total = 0

    # Log what's going on
    print(f'a1\ta2\toutcome\ts_pts\tm_pts\tr_pts\tt_total')

    for round_actions in input:
        # What outcome do we need?
        opponent_action = round_actions[0]
        desired_outcome_code = round_actions[1]
        desired_outcome = match_outcomes[desired_outcome_code]

        # Which action should we take based on the action we need?
        outcomes_for_action = action_points_map[opponent_action]

        # Figure out the scoring
        selection_score = outcomes_for_action[desired_outcome]
        match_score = match_points[desired_outcome]
        round_score = selection_score + match_score
        tournament_total += round_score
        
        # Log each round
        print(f'{round_actions[0]}\t{round_actions[1]}\t{desired_outcome}\t{selection_score}\t{match_score}\t{round_score}\t{tournament_total}')
    
    print(f'\nTournament Total is {tournament_total}')

    return None


def get_action_points_map() -> dict:
    # For all combos of opponent's selection and 
    # desired outcome [lose | draw | win], return the
    # points associated with the action you must have taken
    # Notes:
    # 1 for Rock, 2 for Paper, and 3 for Scissors
    # A for Rock, B for Paper, and C for Scissors
    return {
        'A': {'lose': 3, 'draw': 1, 'win': 2},
        'B': {'lose': 1, 'draw': 2, 'win': 3},
        'C': {'lose': 2, 'draw': 3, 'win': 1}
    }

def get_match_points() -> dict:
    return {
        'lose': 0,
        'draw': 3,
        'win': 6
    }

def get_match_outcome_map() -> dict:
    return {
        'X': 'lose',
        'Y': 'draw',
        'Z': 'win'
    }

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

