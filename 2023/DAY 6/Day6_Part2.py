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
T = int(time[1].replace(" ", ""))

distance = data[1].split(":")
D = int(distance[1].replace(" ", ""))

Total = 1


ways = MinMaxHoldingTime(T, D)

print(T, D, "->", ways)

Total *= ways

print("Total:", Total)