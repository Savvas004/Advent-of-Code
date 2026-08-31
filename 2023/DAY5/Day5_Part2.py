with open("DAY5/Day5_Input.txt", "r") as file:
    data = file.read().splitlines()


seeds = list(map(int, data[0].split(":")[1].split()))


# -------------------------
# Read maps
# -------------------------

maps = []
current_map = []

for line in data[2:]:

    if line == "":
        if current_map:
            maps.append(current_map)
            current_map = []

    elif "map:" in line:
        continue

    else:
        destination, source, length = map(int, line.split())

        current_map.append(
            (destination, source, length)
        )


if current_map:
    maps.append(current_map)


# -------------------------
# Convert seeds into ranges
# -------------------------

ranges = []

for i in range(0, len(seeds), 2):

    start = seeds[i]
    length = seeds[i + 1]

    ranges.append(
        (start, start + length)
    )


# -------------------------
# Process every map
# -------------------------

for current_map in maps:

    new_ranges = []

    while ranges:

        start, end = ranges.pop()

        mapped = False

        for destination, source, length in current_map:

            source_end = source + length

            # Find overlap
            overlap_start = max(start, source)
            overlap_end = min(end, source_end)

            if overlap_start < overlap_end:

                # Convert overlapping part
                new_start = destination + (overlap_start - source)
                new_end = destination + (overlap_end - source)

                new_ranges.append(
                    (new_start, new_end)
                )

                # Left side not mapped
                if start < overlap_start:
                    ranges.append(
                        (start, overlap_start)
                    )

                # Right side not mapped
                if overlap_end < end:
                    ranges.append(
                        (overlap_end, end)
                    )

                mapped = True
                break

        # No mapping affected this range
        if not mapped:
            new_ranges.append((start, end))

    ranges = new_ranges


# -------------------------
# Lowest location
# -------------------------

answer = min(start for start, end in ranges)

print("Lowest location:", answer)