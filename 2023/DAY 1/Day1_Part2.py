with open("Day1_Part2.txt", "r") as file:
    data = file.read().splitlines()

NUMBERS = [
    "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine"
]

total = 0

for line in data:
    found_numbers = []

    for j in range(len(line)):
        # Check normal digits
        if line[j].isdigit():
            found_numbers.append(int(line[j]))

        # Check written numbers beginning at position j
        for index, word in enumerate(NUMBERS):
            if line.startswith(word, j):
                found_numbers.append(index + 1)

    num1 = found_numbers[0]
    num2 = found_numbers[-1]

    total += num1 * 10 + num2

print(total)