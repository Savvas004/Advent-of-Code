with open("2025/DAY 3/Day3_Input.txt", "r") as file:
    data = file.read().splitlines()


total = 0

for line in data:
    num1 = -1
    num2 = -1
    for i in range(len(line)):
        if num1 == -1:
            num1 = int(line[i])
        elif num2 == -1:
            num2 = int(line[i])

        if num2 < int(line[i]) and num2 != -1:
            num2 = int(line[i])

        if num1 < num2 and i < len(line) - 1:
            num1 = num2
            num2 = -1
    # print(num1*10 + num2)
    total += num1*10 + num2

print(total)