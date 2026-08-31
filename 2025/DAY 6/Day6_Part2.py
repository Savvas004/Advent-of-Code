with open("2025/DAY 6/Day6_Input.txt", "r") as file:
    data = file.read().splitlines()

number_rows = data[:-1]
operator_row = data[-1]

total = 0

# Make all rows the same length
width = max(len(line) for line in data)

number_rows = [line.ljust(width) for line in number_rows]
operator_row = operator_row.ljust(width)

start = 0

while start < width:

    # Skip completely empty separator columns
    empty = True

    for row in data:
        if start < len(row) and row[start] != " ":
            empty = False
            break

    if empty:
        start += 1
        continue

    # Find the end of this problem
    end = start

    while end < width:
        empty = True

        for row in data:
            if end < len(row) and row[end] != " ":
                empty = False
                break

        if empty:
            break

        end += 1

    # Find operator
    op = None

    for j in range(start, end):
        if operator_row[j] == "+" or operator_row[j] == "*":
            op = operator_row[j]

    numbers = []

    # PART 2:
    # Each COLUMN becomes one number
    for j in range(start, end):

        num = ""

        for i in range(len(number_rows)):
            if number_rows[i][j] != " ":
                num += number_rows[i][j]

        if num != "":
            numbers.append(int(num))

    # Calculate this problem
    if op == "+":
        result = sum(numbers)

    elif op == "*":
        result = 1

        for num in numbers:
            result *= num

    total += result

    start = end + 1


print(total)