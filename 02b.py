# Total: 12 red cubes, 13 green cubes, and 14 blue cubes

def split_subreveal(subreveal):
    return tuple(map(lambda x: x.strip(), subreveal.split()))

def split_reveal(reveal):
    return list(map(split_subreveal, reveal.split(",")))

def get_max_of_each_color(reveals):
    max = {"red": 0, "green": 0, "blue": 0}
    for reveal in reveals:    
        for numberstr, color in reveal:
            number = int(numberstr)
            if (number > max[color]):
                max[color] = number
    return max

def get_power(max):
    return max["red"] * max["green"] * max["blue"]

  
with open("02.txt", "r") as file:
    sum = 0
    for line in file:
        # each line is a game that contains the id and reveals
        game, reveals = line.split(":")
        # skip the word "Game" and take the number
        game = int(game.split()[1])
        reveals = list(map(split_reveal, reveals.split(";")))
        power = get_power(get_max_of_each_color(reveals))
        #print(f"game: {game}, power: {power}")
        sum += power
    print(sum)