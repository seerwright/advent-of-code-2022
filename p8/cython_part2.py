import part2


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
    part2.main(problem_input)
    
