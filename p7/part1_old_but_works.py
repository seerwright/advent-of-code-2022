# Advent of Code 2022 

from anytree import Node, RenderTree, PostOrderIter
from pprint import pprint

def main(input: list) -> None:

    fs = Node('/', size=0)
    # marc = Node("Marc", parent=udo)

    this_node = fs

    interaction = []
    cmd_out = []
    collect_output = False
    for line in input:

        cmd = is_cmd(line)
        if cmd:
            # New command+output, clear everything out for next interaction
            pprint(interaction)
            # pprint(this_node.name)
            # We have everything, build the next part of the tree
            if interaction:
                this_node = exec_cmd(fs, this_node, interaction)
                for pre, fill, node in RenderTree(fs):
                    print("%s%s" % (pre, node.name))


            interaction = []
            cmd_out = []
            collect_output=False

            # Start new interaction with this command and look for output
            interaction.append(cmd)
            interaction.append([])
            collect_output = True
        
        else:
            # This is output
            if collect_output:
                interaction[1].append(line)


    # Handle the last one because it wasn't triggered. No subsequent command
    # To-do: clean this up
    if interaction:
        this_node = exec_cmd(fs, this_node, interaction)

    # Sum sizes at directory nodes for everything below
    fs = update_dir_sizes(fs)
    dir_node_listing(fs, 100000)

    for pre, fill, node in RenderTree(fs):
        # print("%s%s" % (pre, node.name))
        print(f'{pre} {node.name} {node.size}')


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

    return None

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
    problem_input = read_input('./input/part1.txt', False)
    main(problem_input)
    