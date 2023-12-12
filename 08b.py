
from math import gcd


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

def allEndInZ(nodes):
    for n in nodes:
        if n[-1] != 'Z':
            return False
    return True

def endsInZ(n):
    return n[-1] == 'Z'

def findLoop(node):
    step = 0
    # save in (node, instruction) the step count
    previous = {(node,len(instructions)-1): 0}
    zs = []
    loopSize = None
    while loopSize == None:
        for c, i in enumerate(instructions):
            node = nodes[node][i]
            step = step+1
            if (node,c) in previous:
                # loop found
                prefix = previous[(node,c)]
                loopSize = step - prefix
                break
            previous[(node,c)] = step
            if (endsInZ(node)):
                zs.append(c)
#    print(f'prev: {previous}')
#    print(f'zs: {zs}')
#    print(f'Loop size: {loopSize}')
#    print(f'Loop prefix: {prefix}')
    return loopSize

def lcm(a, b):
    return a*b // gcd(a, b)

def lcmAll(numbers):
    x = numbers[0]
    for n in numbers[1:]:
        x = lcm(x, n)
    return x

# initial nodes are nodes that end in A
cnodes = list(filter(lambda x: x[-1]=='A',
                    nodes.keys()))
steps = 0
print(cnodes)
loops = list(map(findLoop, cnodes))
print(loops)

## Found out all loops end with a z after
## using all instructions, so I am not sure
## this is general enough but sure works
## for this case
print(lcmAll(loops))
