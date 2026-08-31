with open("DAY4/Day4_Input.txt", "r") as file:
    data = file.read().splitlines()


copies = [1] * len(data)

TotalCards = 0
points = 0

for line in data:
    
    parts = line.split(":")
    # print(parts[1])
    cardNumber = parts[0].split()
    card_index = int(cardNumber[1])-1

    for NumOfCopies in range(copies[card_index]):

        game=parts[1].split("|")

        W_Game = game[0].split()
        c_Game = game[1].split()

        for i in range(len(c_Game)):
            for j in range(len(W_Game)):
                if W_Game[j]==c_Game[i]:
                    points+=1

        for k in range(1, points + 1):
            if card_index + k < len(copies):
                copies[card_index + k] += copies[card_index]

        points = 0


for i in range (len(copies)):
    TotalCards+=copies[i]

print("Total points: " + str(TotalCards))
