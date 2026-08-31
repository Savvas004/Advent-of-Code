import math

with open("DAY8/Day8_Input.txt", "r") as file:
    data = file.read().splitlines()


# First line = directions
directions = data[0]


# Store the nodes
nodes = {}

for line in data[2:]:
    node, destinations = line.split(" = ")

    destinations = destinations.strip("()")

    left, right = destinations.split(", ")

    nodes[node] = [left, right]


# Find all starting nodes that end with A
starts = []

for node in nodes:
    if node[-1] == "A":
        starts.append(node)


# Find how many steps each start takes
# to reach a node ending in Z
cycles = []

for start in starts:

    current = start
    steps = 0

    while current[-1] != "Z":

        direction = directions[steps % len(directions)]

        if direction == "L":
            current = nodes[current][0]

        else:
            current = nodes[current][1]

        steps += 1

    cycles.append(steps)

    print(start, "->", current, "in", steps, "steps")


# Find when all paths line up
answer = math.lcm(*cycles)

print("Cycles:", cycles)
print("Answer:", answer)