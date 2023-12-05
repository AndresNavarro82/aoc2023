sum = 0
with open("01.txt", "r") as file:
    for line in file:
        numbers = list(filter(lambda c : c.isdigit(), line))
        number = int(numbers[0]+numbers[-1])
        sum += number
print(sum)    
