import re
# dictionary for symbols, keys are tuples 
# representing positions (0 based, from top-left)
# values are the symbols themselves
symbols = {}
# list for tuples of part numbers and positions 
# (tuples as above)
parts = []

gears = {}

def markAdjacentGearCandidates(number, position):
    row, col = position
    #print(f"n: {number}, pos: {position}")
    for r in (row-1, row, row+1):
        for c in range(col-1, col+len(number)+1):
            #print((r,c))
            if ((r, c) in gearCandidates):
                gearCandidates[(r, c)].append(int(number))

with open("03.txt", "r") as file:
    row = 0
    for line in file:
        # strip the \n first
        # splitting by dots may leave
        # symbols and numbers fused together
        comb_tokens = line.strip().split(".")
        col = 0
#        print(comb_tokens)
        for ct in comb_tokens:
            # this works even for empty strings
            while(ct != ''):
                if not ct[0].isdigit():
                    # symbol found
                    symbols[(row,col)] = ct[0]
                    col += 1
                    ct = ct[1:]
                else:
                    # starts with number, but there
                    # may be symbols in there
                    last = re.match(r'(\d)+', ct).span()[-1]
                    parts.append((ct[:last],(row,col)))
                    col += len(ct[:last])
                    ct = ct[last:]
            col += 1
        row += 1

gearCandidates = {key: [] 
         for key, val in symbols.items() 
         if val == '*'}

for number, pos in parts:
    markAdjacentGearCandidates(number, pos)

sum = 0
for s, parts in gearCandidates.items():
    # only a valid gear if it's adjacent to exactly
    # two part numbers
    if (len(parts) == 2):
        ratio = parts[0] * parts[1]
        sum += ratio

#print(parts)
#print(symbols)
print(sum)
