with open("DAY9/Day9_Input.txt", "r") as file:
    data = file.read().splitlines()

def checkArray(A):
    for i in range(len(A)):
        if A[i] != 0:
            return False
        
    return True


Array2 = []
total = 0


for line in data:
    Array1 = list(map(int, line.split()))
    firstValues = []

    while not checkArray(Array1):
        firstValues.append(Array1[0])
        Array2 = []
        
        for i in range(len(Array1) - 1):
            Array2.append(Array1[i+1] - Array1[i])

        Array1 = Array2.copy()
    previous = 0

    for i in range(len(firstValues) - 1, -1, -1):
        previous = firstValues[i] - previous

    total += previous

print("Total: " + str(total))
    
    
