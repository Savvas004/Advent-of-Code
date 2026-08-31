with open("DAY10/Day10_Input.txt", "r") as file:
    data = file.read().splitlines()

grid = [list(line) for line in data]

rows = len(grid)
cols = len(grid[0])

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

connections = {
    "|": [UP, DOWN],
    "-": [LEFT, RIGHT],
    "L": [UP, RIGHT],
    "J": [UP, LEFT],
    "7": [LEFT, DOWN],
    "F": [RIGHT, DOWN]
}

opposite = {
    UP: DOWN,
    DOWN: UP,
    LEFT: RIGHT,
    RIGHT: LEFT
}


# Find S
start = None

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "S":
            start = (i, j)


# Find which pipes connect to S
start_connections = []

for direction in [UP, DOWN, LEFT, RIGHT]:

    di, dj = direction

    ni = start[0] + di
    nj = start[1] + dj

    if 0 <= ni < rows and 0 <= nj < cols:

        pipe = grid[ni][nj]

        if pipe in connections:
            if opposite[direction] in connections[pipe]:
                start_connections.append(direction)


# ---------------------------------
# Find the complete loop
# ---------------------------------

loop = [start]

direction = start_connections[0]

current = (
    start[0] + direction[0],
    start[1] + direction[1]
)

previous = start


while current != start:

    loop.append(current)

    i, j = current
    pipe = grid[i][j]

    for direction in connections[pipe]:

        ni = i + direction[0]
        nj = j + direction[1]

        next_position = (ni, nj)

        if next_position != previous:
            previous = current
            current = next_position
            break


# ---------------------------------
# Find what type of pipe S is
# ---------------------------------

start_set = set(start_connections)

if start_set == {UP, DOWN}:
    start_pipe = "|"

elif start_set == {LEFT, RIGHT}:
    start_pipe = "-"

elif start_set == {UP, RIGHT}:
    start_pipe = "L"

elif start_set == {UP, LEFT}:
    start_pipe = "J"

elif start_set == {LEFT, DOWN}:
    start_pipe = "7"

elif start_set == {RIGHT, DOWN}:
    start_pipe = "F"


# ---------------------------------
# Part 2
# ---------------------------------

loop_set = set(loop)

inside_count = 0


for i in range(rows):

    inside = False

    for j in range(cols):

        current = (i, j)

        if current in loop_set:

            pipe = grid[i][j]

            if pipe == "S":
                pipe = start_pipe

            if pipe in ["|", "L", "J"]:
                inside = not inside

        else:

            if inside:
                inside_count += 1


print("Part 2:", inside_count)