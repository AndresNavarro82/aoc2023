seeds = []

# seed -> ... maps ... -> location
# parallel lists, names for debugging
mapsNames = []
maps = []

def translateRange(map, start, count):
    #print("translate Range")
    #print(map)
    srcIntervals = [(start, count)]
    dstIntervals = []
    while len(srcIntervals) > 0:
        start,count = srcIntervals.pop()
        if count == 0: # skip empty intervals
            continue
        end = start+count-1
        #print(f"start: {start}, count: {count}, end: {end}")
        for dst,src,cnt in map:
            lastSrc = src+cnt-1
            #print(f"dst: {dst}, src: {src}, cnt: {cnt}, lastSrc: {lastSrc}")
            # first if no intersection keep looking

            if end < src or start > lastSrc:
                # no intersection, keep looking
                #print("no intersection")
                continue
            else:
                # how many are left before and after
                # this map
                #print("intersection")
                countLeft = src-start
                if countLeft > 0:
                    srcIntervals.append((start, countLeft))
                    count -= countLeft
                    start = src
                countRight = end - lastSrc
                if countRight > 0:
                    srcIntervals.append((lastSrc+1, countRight))
                    count -= countRight
                    end = lastSrc
                # the remaining is inside the map
                dstIntervals.append((dst+(start-src),count))
                break
        else: # on normal exits the interval
              # should be added as is
              # if not in any range, its the same number
            dstIntervals.append((start, count))
    #print("res:")
    #print(dstIntervals)
    return dstIntervals

def getLocationRanges(start, count):
    intervals = [(start, count)]
    #print()
    #print(f"intervals (seed)")
    #print(intervals)
    for name, map in zip(mapsNames, maps):
        newIntervals = []
        for start, count in intervals: 
            t = translateRange(map, start, count)
            newIntervals.extend(t)
        intervals = newIntervals
        #print()
        #print(f"intervals ({name})")
        #print(intervals)
    return intervals


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

#debug by levels
#max = 1
#mapsNames = mapsNames[:1]
#maps = maps[:1]

minLocation = getLocation(seeds[0])
# now the seed list is a list of start, len ranges of seeds
for i in range(0, len(seeds), 2):
    start = seeds[i]
    count = seeds[i+1]
    end = start + count - 1
    intervals = getLocationRanges(start, count)
    for l,_ in intervals:
        if l < minLocation:
            minLocation = l
    #for seed in range(start, end):
    #     print()
    #     print(f"seed: {seed}")
    #     l = getLocation(seed)
    #     if l < minLocation:
    #         minLocation = l
print(minLocation)