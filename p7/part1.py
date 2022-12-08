# Advent of Code 2022 

from anytree import Node, RenderTree, PostOrderIter
from pprint import pprint

def main(input: list) -> None:

    # Let's use trees!
    fs = Node('/', size=0)
    this_node = fs

    # Let's call every 1 command and its 0+ outputs an interaction
    interaction = []
    cmd_out = []
    collect_output = False

    # Iterate over all of the input commands and responses
    for line in input:
        # Command or output?
        cmd = is_cmd(line)
        if cmd:
            # New command+output. This means we have everything and can 
            # clear out the interaction for the next one
            # EXCEPTION! Last command of the list (because they won't be another cmd)
            #            Sloppily deal with this at the end. Don't judge me - I'm working fast!
            if interaction:
                # Update the tree ... done by reference (yuck)
                this_node = exec_cmd(fs, this_node, interaction)

            # Tree is updated, wipe this stuff out
            interaction = []
            cmd_out = []
            collect_output=False

            # Start new interaction with this command and look for output
            interaction.append(cmd)
            interaction.append([])
            collect_output = True
        
        else:
            # This is output from the command. Save it
            if collect_output:
                interaction[1].append(line)


    # Handle the last one because it wasn't triggered. No subsequent command
    if interaction:
        this_node = exec_cmd(fs, this_node, interaction)

    # Tree stucture built, but need to tally up directory sizes
    fs = update_dir_sizes(fs)


    # Okay, tree is in final state!!! Show it...
    for pre, fill, node in RenderTree(fs):
        # print("%s%s" % (pre, node.name))
        print(f'{pre} {node.name} {node.size}')

    # Report the solution
    # In both parts we need to track the sizes of all directories meeting
    #     a certain criterium
    # Part 1: Add them all up if they are less than 100,000
    # Part 2: Set a high theshold to see all of them, then manually
    #         review to get the smallest dir that's big enough to 
    #         free up the needed amount of space
    filtered_sizes = dir_node_listing(fs, 100000)

    # Part 2 stuff ...
    space_total = 70000000
    space_needed = 30000000
    current_free = space_total - fs.size
    print(f'{space_total}\tTotal space on disk is')
    print(f'{space_needed}\tSpace needed')
    print(f'{fs.size}\tCurrently used')
    print(f'{current_free}\tUnused space')
    print('-------------------------')
    print(f'{space_needed - current_free}\tAmount to free up')
    print(f'All dirs available:')
    print(sorted(filtered_sizes))

    # Manually reviewed list of filtered sizes to determine that 2050735 is the smallest
    # dir that is just big enough to free up space.



    return None

def update_dir_sizes(root: Node) -> Node:
    # Leaves update only their parents
    for l in PostOrderIter(root):
        if l.is_leaf:
            l.parent.size += l.size
    # Parents update only their parents
    for l in PostOrderIter(root):
        if not l.is_leaf:
            # print(f'{l.name} is NOT a leaf. Adding its size {l.size} to its parent {l.parent.name} of size {l.parent.size} = {l.parent.size + l.size}')
            try:
                l.parent.size += l.size
            except AttributeError as e:
                print(f'Could not add size to parent size for {l.parent} or {l}')
            # print(f'New size of {l.parent.name} is {l.parent.size}')
    # Do root separately because something is goofy above
    root.size = 0
    for l in root.leaves:
        root.size += l.size

    return root

def dir_node_listing(root: Node, sum_filter: int = 0) -> None:
    filtered_sizes = []

    for d in root.descendants:
        if not d.is_leaf:
            print(f'Directory {d.name} has size {d.size}')
            if d.size <= sum_filter:
                # if len(d.siblings) > 0:
                filtered_sizes.append(d.size)
    # Don't forget the root
    print(f'Directory {root.name} has size {root.size}')
    if root.size <= sum_filter:
        filtered_sizes.append(root.size)

    print(f'Sum of all directories LTE {sum_filter} is {sum(filtered_sizes)}')

    return filtered_sizes

def exec_cmd(tree: Node, this_node: Node, interaction: list) -> Node:
    # tree:        whole tree
    # this_node:   where exec_cmd is being called from
    # interaction: cmd + its output
    oper, output = interaction
    cmd, args = oper

    if cmd == 'ls':
        contents = parse_listing(output)
        for d in contents['directories']:
            _ = Node(d, parent=this_node, size=0)
        for f in contents['files']:
            _ = Node(f[1], parent=this_node, size=int(f[0]))
        return this_node
    elif cmd == 'cd':
        path = args[0]
        if path == '..':
            return this_node.parent
        elif path == '/':
            return this_node.root
        else:
            return get_child_node(this_node, path)

def get_child_node(this_node: Node, child_name: str) -> Node:
    for c in this_node.children:
        if c.name == child_name:
            return c
    return None

def parse_listing(output: list) -> list:
    # Example: ['dir a', '14848514 b.txt', '8504156 c.dat', 'dir d']
    objects = {
        'directories': [],
        'files': []
    }
    for object in output:
        parts = object.split()
        if parts[0] == 'dir':
            objects['directories'].append(parts[1])
        else:
            objects['files'].append(parts)
    return objects

def is_cmd(line: str) -> list:
    parts = line.split()
    if parts[0] == '$':
        oper = parts[1]
        args = parts[2:]
        return [oper, args]
    else:
        return None


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
    problem_input = read_input('./input/part1_test.txt', False)
    main(problem_input)
    