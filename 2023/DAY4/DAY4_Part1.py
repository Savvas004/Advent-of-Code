with open("DAY4/Day4_Input.txt", "r") as file:
    data = file.read().splitlines()

T_Points = 0
points = 0

for line in data:
    parts = line.split(":")
    print(parts[1])

    game=parts[1].split("|")

    W_Game = game[0].split()
    c_Game = game[1].split()

    for i in range(len(c_Game)):
        for j in range(len(W_Game)):
            if W_Game[j]==c_Game[i]:
                print(W_Game[j]+" " + c_Game[i])
                if points==0:
                    points+=1
                points*=2
    print("Round Points: " + str(points))
    T_Points+=points
    points=0

print("Total points: " + str(T_Points/2))
