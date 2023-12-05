sum = 0
with open("04.txt") as file:
    for line in file:
        _,line = line.split(":")
        winners, numbers = line.split("|")
        winners = winners.split()
        numbers = numbers.split()
        count = 0
        for n in numbers:
            if n in winners:
                count += 1
        if count > 0:
            sum += 2**(count-1)

print(sum)
