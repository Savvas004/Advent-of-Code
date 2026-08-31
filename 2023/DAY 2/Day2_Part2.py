with open("Day2_Part2.txt", "r") as file:
    data = file.read().splitlines()

total = 0

for line in data:
    game_part, cubes_part = line.split(":")

    maximum = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    sets = cubes_part.split(";")

    for cube_set in sets:
        cubes = cube_set.split(",")

        for cube in cubes:
            amount, colour = cube.strip().split()
            amount = int(amount)

            if amount > maximum[colour]:
                maximum[colour] = amount

    power = maximum["red"] * maximum["green"] * maximum["blue"]
    total += power

print(total)