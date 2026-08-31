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


# Start following the pipe
direction = start_connections[0]

current = (
    start[0] + direction[0],
    start[1] + direction[1]
)

previous = start

loop_length = 1


while current != start:

    loop_length += 1

    i, j = current

    pipe = grid[i][j]

    for direction in connections[pipe]:

        ni = i + direction[0]
        nj = j + direction[1]

        next_position = (ni, nj)

        # Don't go back to the previous pipe
        if next_position != previous:

            previous = current
            current = next_position
            break


# Furthest point = half of the loop
answer = loop_length // 2

print("Part 1:", answer)