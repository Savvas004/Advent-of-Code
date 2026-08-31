with open("DAY8/Day8_Input.txt", "r") as file:
    data = file.read().splitlines()


directions = data[0]

nodes = {}

for line in data[2:]:
    node, destinations = line.split(" = ")

    destinations = destinations.strip("()")

    left, right = destinations.split(", ")

    nodes[node] = [left, right]


current = "AAA"
steps = 0


while current != "ZZZ":

    direction = directions[steps % len(directions)]

    if direction == "L":
        current = nodes[current][0]

    else:
        current = nodes[current][1]

    steps += 1


print("Steps:", steps)