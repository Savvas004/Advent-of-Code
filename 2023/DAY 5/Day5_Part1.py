with open("DAY5/Day5_Input.txt", "r") as file:
    data = file.read().splitlines()


# Get seeds
seeds = list(map(int, data[0].split(":")[1].split()))

maps = []
current_map = []


# Start from line 2 because:
# line 0 = seeds
# line 1 = blank
for line in data[2:]:

    # Blank line means current map finished
    if line == "":
        if current_map:
            maps.append(current_map)
            current_map = []

    # Skip map titles
    elif "map:" in line:
        continue

    else:
        destination, source, length = map(int, line.split())

        current_map.append([
            destination,
            source,
            length
        ])


# Add the final map
if current_map:
    maps.append(current_map)


locations = []


# Process every seed
for seed in seeds:

    number = seed

    # Pass through every map
    for current_map in maps:

        for destination, source, length in current_map:

            if source <= number < source + length:

                number = destination + (number - source)

                # Only ONE range can map the number
                break

    locations.append(number)


print("Locations:", locations)
print("Lowest location:", min(locations))