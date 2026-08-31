with open("2025/DAY 5/Day5_Input.txt", "r") as file:
    data = file.read().splitlines()

R = []
numbers = []
Found = False
count = 0

for line in data:

    if line == "":
        break

    start, end = map(int, line.split("-"))
    R.append([start, end])


R.sort(key=lambda x: (x[0], x[1]))

pStart = -1
pEnd = -1

for Start, End in R:
    if pStart == -1 and pEnd == -1:
        pStart = Start
        pEnd = End

    if pStart <= Start <= pEnd:
            if pEnd < End:
                 pEnd = End
    else:
         count += pEnd - (pStart - 1)
         pStart = Start
         pEnd = End

count += pEnd - pStart + 1
print(count)
    