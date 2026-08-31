with open("Day2_Part1.txt", "r") as file:
    data = file.read().splitlines()

limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

total = 0

for line in data:
    game_part, cubes_part = line.split(":")

    game_id = int(game_part.split()[1])
    possible = True

    sets = cubes_part.split(";")

    for cube_set in sets:
        cubes = cube_set.split(",")

        for cube in cubes:
            amount, colour = cube.strip().split()
            amount = int(amount)

            if amount > limits[colour]:
                possible = False

    if possible:
        total += game_id

print(total)