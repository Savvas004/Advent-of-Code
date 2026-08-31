with open("2025/DAY 5/Day5_Input.txt", "r") as file:
    data = file.read().splitlines()

R = []
numbers = []
Found = False
count = 0

for line in data:

    if line == "":
        Found = True
        continue

    if not Found:
        start, end = map(int, line.split("-"))
        R.append([start, end])

    else:
        numbers.append(int(line))

for num in numbers:
    for start,end in R:
        if start <= num <= end:
            count+=1
            break

print(count)
    