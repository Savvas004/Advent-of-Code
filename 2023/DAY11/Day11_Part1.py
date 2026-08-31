with open("DAY11/Day11_Input.txt", "r") as file:
    data = file.read().splitlines()

grid = [list(line) for line in data]

array = [[], []]
total = 0


def ShiftRight(pos):
    for row in grid:
        row.insert(pos, ".")


def ShiftDown(pos):
    grid.insert(pos, ["."] * len(grid[0]))


# -----------------------
# Expand empty columns
# -----------------------

j = 0

while j < len(grid[0]):

    check = True

    for i in range(len(grid)):
        if grid[i][j] == "#":
            check = False
            break

    if check:
        ShiftRight(j)
        j += 1   # skip the new column

    j += 1


# -----------------------
# Expand empty rows
# -----------------------

i = 0

while i < len(grid):

    check = True

    for j in range(len(grid[0])):
        if grid[i][j] == "#":
            check = False
            break

    if check:
        ShiftDown(i)
        i += 1   # skip the new row

    i += 1


# -----------------------
# Find galaxies
# -----------------------

num = 1

for i in range(len(grid)):
    for j in range(len(grid[0])):

        if grid[i][j] == "#":

            grid[i][j] = str(num)

            array[0].append(i)
            array[1].append(j)

            num += 1


# -----------------------
# Calculate distances
# -----------------------

for i in range(len(array[0])):

    for j in range(i + 1, len(array[0])):

        distance = (
            abs(array[0][i] - array[0][j])
            +
            abs(array[1][i] - array[1][j])
        )

        total += distance


print(total)