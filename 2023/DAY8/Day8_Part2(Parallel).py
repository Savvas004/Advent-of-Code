import math
from concurrent.futures import ThreadPoolExecutor

with open("DAY8/Day8_Input.txt", "r") as file:
    data = file.read().splitlines()


directions = data[0]

nodes = {}

for line in data[2:]:
    node, destinations = line.split(" = ")
    destinations = destinations.strip("()")

    left, right = destinations.split(", ")

    nodes[node] = [left, right]


def findSteps(start):
    current = start
    steps = 0

    while current[-1] != "Z":

        direction = directions[steps % len(directions)]

        if direction == "L":
            current = nodes[current][0]
        else:
            current = nodes[current][1]

        steps += 1

    return steps


# Find all nodes ending in A
starts = []

for node in nodes:
    if node[-1] == "A":
        starts.append(node)


# Run each starting point in parallel
with ThreadPoolExecutor() as executor:
    cycles = list(executor.map(findSteps, starts))


print("Starting nodes:", starts)
print("Cycles:", cycles)

answer = math.lcm(*cycles)

print("Answer:", answer)