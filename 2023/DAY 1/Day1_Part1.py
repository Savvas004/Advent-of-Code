with open("Day1.txt", "r") as file:
    data = file.read().splitlines()

f=0
total = 0
num1 = 0
num2 = 0

for i in range(len(data)):
    for j in range(len(data[i])):
        if f==0 :
            if '0' <= data[i][j] <= '9':
                num1 = int(data[i][j])
                f=1
        if f==1 :
            if '0' <= data[i][j] <= '9':
                num2 = int(data[i][j])
            
    f=0
    total =total + num1*10 + num2
    
print(total)
    
            