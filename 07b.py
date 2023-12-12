
hands = []
# J is now the weaker card
cardOrder = "AKQT98765432J"

flush = 0
poker = 1
full = 2
three = 3
twopairs = 4
pair = 5
high = 6

# returns a number (less is higher hand) 
def handResult(hand):
    counts = { key : 0 for key in cardOrder}

    for card in hand:
        counts[card] += 1

    res = None
    cvalues = list(counts.values())
    js = counts["J"]
    if 5 in cvalues:
        res = flush
    elif 4 in cvalues:
        if js > 0:
            res = flush
        else:
            res = poker
    elif 3 in cvalues:
        if 2 in cvalues: 
            if js > 0:
                res = flush
            else:
                res = full
        else:
            if js > 0:
                res = poker
            else:
                res = three
    elif 2 in cvalues:
        if cvalues.count(2) == 2:
            if js == 2:
                res = poker
            elif js == 1:
                res = full
            else:
                res = twopairs
        else:
            if js > 0:
                res = three
            else:
                res = pair
    else:
        if js > 0:
            res = pair
        else:
            res = high
    
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

filtered = list(filter(lambda x: 'J' in x[6], results))
print(f"filtered: {filtered}")

total = 0
for i, r in enumerate(results):
    i = len(results)-i # 1 based rank, from lowest to highest
    bid = r[-1] # last value is the bid
    total += i*bid
print(total)



