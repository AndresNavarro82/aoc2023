
hands = []
cardOrder = "AKQJT98765432"

# returns a number (less is higher hand) 
def handResult(hand):
    counts = { key : 0 for key in cardOrder}

    for card in hand:
        counts[card] += 1

    res = None
    cvalues = list(counts.values())
    if 5 in cvalues:
        res = 0 # flush
    elif 4 in cvalues:
        res = 1 # poker
    elif 3 in cvalues:
        if 2 in cvalues: 
            res = 2 # full house
        else:
            res = 3 # three of a kind
    elif 2 in cvalues:
        if cvalues.count(2) == 2:
            res = 4 # two pairs
        else:
            res = 5 # one pair
    else:
        res = 6 # high card
    
    return res

# this includes the value of the hand, plus
# the value of each card, the hand itself and the bid
def totalHandResult(hand_bid):
    hand, bid = hand_bid
    hv = handResult(hand)
    cardValues = map(lambda x:cardOrder.index(x),hand)
    res = [hv]
    res.extend(list(cardValues))
    res.append(hand)
    res.append(bid)
    return res

with open("07.txt") as file:
    for line in file:
        hand, bid = line.split()
        hands.append((hand,int(bid)))

results = list(map(totalHandResult, hands))
print(f"unordered: {results}")
results = sorted(results)
print(f"ordered: {results}")

total = 0
for i, r in enumerate(results):
    i = len(results)-i # 1 based rank, from lowest to highest
    bid = r[-1] # last value is the bid
    total += i*bid
print(total)
    

