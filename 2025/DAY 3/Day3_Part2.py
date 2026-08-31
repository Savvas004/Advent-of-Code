with open("2025/DAY 3/Day3_Input.txt", "r") as file:
    data = file.read().splitlines()

total = 0
jLen = 12

for line in data:
    joltage = []
    start = 0

    for p in range(jLen):
        remaining = jLen - p - 1

        # We can search only this far,
        # because we need enough digits left afterward
        end = len(line) - remaining

        max_digit = -1
        max_index = -1

        for i in range(start, end):
            digit = int(line[i])

            if digit > max_digit:
                max_digit = digit
                max_index = i

        joltage.append(max_digit)

        # Next digit must come after this one
        start = max_index + 1

    number = 0

    for i in range(jLen):
        number += joltage[i] * 10 ** (jLen - 1 - i)

    total += number

print(total)