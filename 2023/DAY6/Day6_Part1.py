import math

with open("DAY6/Day6_Input.txt", "r") as file:
    data = file.read().splitlines()


def MinMaxHoldingTime(T, D):

    Min = (T - math.sqrt(T**2 - 4 * D)) / 2
    Max = (T + math.sqrt(T**2 - 4 * D)) / 2

    # We need STRICTLY greater distance than D
    Min = math.floor(Min) + 1
    Max = math.ceil(Max) - 1

    return Max - Min + 1


# ----- MAIN -----

time = data[0].split(":")
T = list(map(int, time[1].split()))

distance = data[1].split(":")
D = list(map(int, distance[1].split()))

Total = 1

for i in range(len(D)):
    ways = MinMaxHoldingTime(T[i], D[i])

    print(T[i], D[i], "->", ways)

    Total *= ways

print("Total:", Total)