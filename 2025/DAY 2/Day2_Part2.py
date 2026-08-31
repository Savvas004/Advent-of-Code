with open("2025/DAY 2/Day2_Input.txt", "r") as file:
    data = file.read().splitlines()

line = data[0].split(",")

total = 0

for i in range(len(line)):
    R = line[i].split("-")

    for j in range(int(R[0]), int(R[1]) + 1):
        StrJ = str(j)

        # Try every possible pattern length
        for length in range(1, len(StrJ) // 2 + 1):

            # The pattern must divide the full string exactly
            if len(StrJ) % length == 0:

                pattern = StrJ[:length]

                repeats = len(StrJ) // length

                if pattern * repeats == StrJ:
                    total += j
                    break

print(total)