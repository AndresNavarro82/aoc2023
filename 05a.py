seeds = []

# seed -> ... maps ... -> location
# parallel lists, names for debugging
mapsNames = []
maps = []

def translate(map, number):
    for dst,src,rng in map:
        if src <= number < src+rng:
            return dst+(number-src)
    # if not in any range, its the same number
    return number

def getLocation(seed):
    # the location is the result of translating
    # for every map
    number = seed
    #print("translate")
    #print(number)
    for name, map in zip(mapsNames, maps):
        number = translate(map, number)
        #print(f"map {name}: {number}")
    return number

with open("05.txt") as file:
    line = file.readline()
    seeds = line.split(':')[-1].split()
    seeds = list(map(int, seeds))
    file.readline() # discard empty line

    for line in file:
        line = line.strip()
        if ':' in line:
            name = line.split()[0]
            mapsNames.append(name)
            maps.append([])
        elif line != '':
            dst,src,rng = line.split()
            maps[-1].append((int(dst),int(src),int(rng)))

minLocation = getLocation(seeds[0])
for seed in seeds:
     l = getLocation(seed)
     if l < minLocation:
         minLocation = l
print(minLocation)