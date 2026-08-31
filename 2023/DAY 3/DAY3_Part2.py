with open("DAY3/DAY3_Input.txt", "r") as file:
    data = [list(line) for line in file.read().splitlines()]

numebers = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}


def getNum(i, j, data):

    # Move to first digit
    while j > 0 and data[i][j - 1] in numebers:
        j -= 1

    start = j
    num = 0

    # Read full number
    while j < len(data[i]) and data[i][j] in numebers:
        num = num * 10 + int(data[i][j])
        j += 1

    return num, start


def checkAround(i, j, data):

    numbers = []
    positions = []

    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:

            if di == 0 and dj == 0:
                continue

            ni = i + di
            nj = j + dj

            # Boundary check
            if (
                0 <= ni < len(data)
                and 0 <= nj < len(data[ni])
                and data[ni][nj] in numebers
            ):

                number, start = getNum(ni, nj, data)

                position = (ni, start)

                # Don't add same number twice
                if position not in positions:
                    positions.append(position)
                    numbers.append(number)

    return numbers


# ----- MAIN -----

total = 0

for i in range(len(data)):
    for j in range(len(data[i])):

        if data[i][j] == '*':

            numbers = checkAround(i, j, data)

            print("Found * at:", i, j)
            print("Numbers:", numbers)

            if len(numbers) == 2:
                total += numbers[0] * numbers[1]


print("Final total:", total)