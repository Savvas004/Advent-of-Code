with open("2025/DAY 4/Day4_Input.txt", "r") as file:
    data = [list(line) for line in file.read().splitlines()]


def checkAround(i, j, data):
    count = 0

    for di in [-1,0,1]:
        for dj in [-1,0,1]:

            if di == 0 and dj == 0:
                continue

            ni = i + di
            nj = j + dj

            if(
                0 <= ni < len(data)
                and 0 <= nj < len(data[ni])
                and data[ni][nj] == '@'
            ):
                count += 1

    return count < 4

# ----- MAIN -----

c = 0

for i in range(len(data)):
    for j in range(len(data[i])):

        if data[i][j] == '@' and checkAround(i, j, data):
            c += 1
print(c)