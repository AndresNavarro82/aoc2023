sum = 0

# this has the number of copies, winners and numbers
# of each card
lines = []

def countWinners(winners, numbers):
    count = 0
    for n in numbers:
        if n in winners:
            count += 1
    return count

with open("04.txt") as file:
    for line in file:
        _,line = line.split(":")
        winners, numbers = line.split("|")
        winners = winners.split()
        numbers = numbers.split()
        # one copy of each card
        lines.append((1, winners, numbers))

for i in range(len(lines)):
    rep, winners, numbers = lines[i]
    # count each copy of this card
    sum += rep
    count = countWinners(winners, numbers)
    # repeat the same for each copy of this card
    # update count for the next count cards
    # this just skips if zero
    # (dont add pass the number of original cards)
    for j in range(i+1, min(len(lines), i+1+count)):
        r,w,n = lines[j]
        lines[j] = (r+rep,w,n)
print(sum)
