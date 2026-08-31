with open("2025/DAY 2/Day2_Input.txt", "r") as file:
    data = file.read().splitlines()

line = data[0].split(",")

total = 0

for i in range(len(line)):
    R = line[i].split("-")

    for j in range(int(R[0]), int(R[1]) + 1):
        StrJ = str(j)

        if len(StrJ) % 2 == 0:
            num1 = StrJ[:len(StrJ)//2]
            num2 = StrJ[len(StrJ)//2:]

            if num1 == num2:
                total += j

print(total)