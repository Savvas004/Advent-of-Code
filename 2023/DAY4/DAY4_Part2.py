with open("DAY4/Day4_Input.txt", "r") as file:
    data = file.read().splitlines()

copies = [1] * len(data)
T_Points = 0
points = 0
count = 0

for line in data:
    parts = line.split(":")

    game = parts[1].split("|")

    W_Game = game[0].split()
    c_Game = game[1].split()

    for i in range(len(c_Game)):
        for j in range(len(W_Game)):
            if W_Game[j] == c_Game[i]:
                points += 1

    count += 1

    for k in range(count, count + points):
        # if k < len(copies):
            copies[k] += copies[count - 1]

    points = 0

for i in range(len(copies)):
    T_Points += copies[i]

print("Total cards: " + str(T_Points))