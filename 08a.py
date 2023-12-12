
nodes = {}

with open("08.txt") as file:
    # first line are the instructions
    instructions = file.readline().strip()
    file.readline() # discard empty line
    # next lines are the nodes
    for line in file:
        node, options = line.split('=')
        node = node.strip()
        left, right = options.split(',')
        # clean parens and spaces
        left = left.strip()[1:]
        right = right.strip()[:-1]
        nodes[node] = {'L': left, 'R': right}

#print(f'instructions {instructions}')
#print(f'nodes: {nodes}')

node = 'AAA'
steps = 0
while(node != 'ZZZ'):
    for i in instructions:
        # follow instruction to next node
        node = nodes[node][i]
        steps += 1
        print('.', end='')
        if node == 'ZZZ':
            # early exit
            print("Early exit")
            break
    else:
        print('another loop...')


print("finally...")
print(steps)