with open("DAY7/Day7_Input.txt", "r") as file:
    data = file.read().splitlines()


strength = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}


def checkHand(cards):

    counts = {}

    # Count how many times each card appears
    for card in cards:
        if card in counts:
            counts[card] += 1
        else:
            counts[card] = 1

    values = list(counts.values())

    if 5 in values:
        return 7   # Five of a kind

    elif 4 in values:
        return 6   # Four of a kind

    elif 3 in values and 2 in values:
        return 5   # Full house

    elif 3 in values:
        return 4   # Three of a kind

    elif values.count(2) == 2:
        return 3   # Two pair

    elif 2 in values:
        return 2   # One pair

    else:
        return 1   # High card


hands = []


for line in data:

    game = line.split()

    cards = game[0]
    bid = int(game[1])

    hand_type = checkHand(cards)

    hands.append([cards, bid, hand_type])


def sortKey(hand):

    cards = hand[0]
    hand_type = hand[2]

    card_values = []

    for card in cards:
        card_values.append(strength[card])

    return (
        hand_type,
        card_values[0],
        card_values[1],
        card_values[2],
        card_values[3],
        card_values[4]
    )


# Weakest hand first
hands.sort(key=sortKey)


total = 0

for i in range(len(hands)):

    rank = i + 1
    bid = hands[i][1]

    total += rank * bid

    print(
        rank,
        hands[i][0],
        hands[i][1],
        hands[i][2]
    )


print("Total:", total)