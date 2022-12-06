# Advent of Code 2022 


def main(input: list) -> None:

    # Set up our input string and define the number of chars we're looking for
    buffer = input[0]
    token_length = 14

    # Generate all the segments, basically offsets of 1 through the token length
    segments = generate_segments(buffer, token_length)
    tuples = zip(*segments)

    # Check all of them until we find a distinct one
    for index, q in enumerate(tuples):
        q = list(q)
        if len(q) == len(set(q)):
            print(f'{q} is distinct and is located at {index+token_length}')
            break

    return None

def generate_segments(input: str, n_segments: int) -> list:
    # Generate the segments. These will be zipped by the caller to create tuples
    segments = []
    for i in range(n_segments):
        segments.append(input[i:-(n_segments-i)])
    return segments

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
    