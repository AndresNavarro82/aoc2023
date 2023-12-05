sum = 0
# exclude zero, as per the instructions
digits = {  "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9" }
# but include it here, to do as in the last exercise
for d in range(10):
    dstr = str(d)
    digits[dstr] = dstr
# print(digits)

def findAllFirstAndLastPositions(line):
    positions = map(lambda dstr : (dstr, line.find(dstr), line.rfind(dstr)), 
                    digits.keys())
    # eliminate all that don't appear (don't have first nor last position)
    return list(filter(lambda t : t[1] != -1, positions))

def findFirstAndLast(line):
    positions = findAllFirstAndLastPositions(line)
    #print("new line: ")
    #print(line)
    #print("positions: ")
    #print(positions)
    min = positions[0][1]
    max = positions[0][2]
    first = last = positions[0][0]
    
    for dstr, fpos, lpos in positions[1:]:
        if fpos < min:
            min = fpos
            first = dstr
        if lpos > max:
            max = lpos
            last = dstr

    #print(f"first:  {first}, last:  {last}")
    return (first, last)    

with open("01.txt", "r") as file:
    for line in file:
        first, last = findFirstAndLast(line)
        numberstr = digits[first] + digits[last]
        #print(numberstr)
        sum += int(numberstr)
print(sum)    
