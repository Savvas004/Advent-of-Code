with open("2025/DAY 1/Day1_Input.txt", "r") as file:
    data = file.read().splitlines()

CurrentPoint = 50
Counter = 0

for line in data:
    move = line[0]
    num = int(line[1:])

    if move == 'R':
        CurrentPoint = (CurrentPoint + num) % 100
    elif move == 'L':
        CurrentPoint = (CurrentPoint - num) % 100

    if CurrentPoint == 0:
        Counter += 1

print(Counter)