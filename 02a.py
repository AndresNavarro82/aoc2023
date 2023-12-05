# Total: 12 red cubes, 13 green cubes, and 14 blue cubes

totals = { "red": 12, "green": 13, "blue": 14}

def split_subreveal(subreveal):
    return tuple(map(lambda x: x.strip(), subreveal.split()))

def split_reveal(reveal):
    return list(map(split_subreveal, reveal.split(",")))

def is_game_possible(reveals):
    for reveal in reveals:    
        for numberstr, color in reveal:
            number = int(numberstr)
            if (number > totals[color]):
                return False
    return True

  
with open("02.txt", "r") as file:
    sum = 0
    for line in file:
        # each line is a game that contains the id and reveals
        game, reveals = line.split(":")
        # skip the word "Game" and take the number
        game = int(game.split()[1])
        reveals = list(map(split_reveal, reveals.split(";")))
        if is_game_possible(reveals):
            sum += game
        #print(f"game: {game}")
        #print(reveals)
    print(sum)