with open("2025/DAY1/Day1_Input.txt", "r") as file:
    data = file.read().splitlines()

CurrentPoint = 50
Counter = 0

for line in data:
    move = line[0]
    num = int(line[1:])

    if move == 'R':
        Counter += (CurrentPoint + num) // 100
        CurrentPoint = (CurrentPoint + num) % 100

    elif move == 'L':
        if CurrentPoint == 0:
            Counter += num // 100
        else:
            Counter += (num + 100 - CurrentPoint) // 100

        CurrentPoint = (CurrentPoint - num) % 100

print(Counter)