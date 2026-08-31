with open("2025/DAY 4/Day4_Input.txt", "r") as file:
    data = [list(line) for line in file.read().splitlines()]


def checkAround(i, j, data):
    count = 0

    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:

            if di == 0 and dj == 0:
                continue

            ni = i + di
            nj = j + dj

            if (
                0 <= ni < len(data)
                and 0 <= nj < len(data[ni])
                and (data[ni][nj] == '@' or data[ni][nj] == 'X')
            ):
                count += 1

    return count < 4


# ----- MAIN -----

total = 0
c = 1

while c > 0:
    c = 0

    for i in range(len(data)):
        for j in range(len(data[i])):

            if data[i][j] == '@' and checkAround(i, j, data):
                data[i][j] = 'X'
                c += 1

    total += c

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'X':
                data[i][j] = '.'


print(total)