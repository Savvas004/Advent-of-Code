x=""

for i in range(0, 10):
    for j in range(0, 10):
        x += str(i) + "," + str(j) + " "
    print(x)
    x = ""