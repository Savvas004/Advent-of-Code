with open("DAY11/Day11_Input.txt", "r") as file:
    grid = file.read().splitlines()

EXPANSION = 1_000_000

empty_rows = []
empty_cols = []

# Find empty rows
for i in range(len(grid)):
    if "#" not in grid[i]:
        empty_rows.append(i)

# Find empty columns
for j in range(len(grid[0])):
    check = True

    for i in range(len(grid)):
        if grid[i][j] == "#":
            check = False
            break

    if check:
        empty_cols.append(j)


# Find galaxies
galaxies = []

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "#":
            galaxies.append([i, j])


total = 0

for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):

        r1, c1 = galaxies[i]
        r2, c2 = galaxies[j]

        distance = abs(r1 - r2) + abs(c1 - c2)

        # Check empty rows between galaxies
        for row in empty_rows:
            if min(r1, r2) < row < max(r1, r2):
                distance += EXPANSION - 1

        # Check empty columns between galaxies
        for col in empty_cols:
            if min(c1, c2) < col < max(c1, c2):
                distance += EXPANSION - 1

        total += distance

print(total)