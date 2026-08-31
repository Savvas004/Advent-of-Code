with open("DAY3/Day3_Input.txt", "r") as file:
    data = file.read().splitlines()

numebers = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}


#------------------FUNCTIONS-----------------

#----CHECKS----
def check_up(i,j, data):
    if i > 0:
        if data[i-1][j] == '*':
            return True
    return False

def check_down(i,j, data):
    if i < len(data)-1:
        if data[i+1][j] == '*':
            return True
    return False
def check_left(i,j, data):
    if j > 0:
        if data[i][j-1] == '*':
            return True
    return False

def check_right(i,j, data):
    if j < len(data[i])-1:
        if data[i][j+1] == '*':
            return True
    return False


#----CHECKS DIAGONAL----
def check_up_left(i,j, data):
    if i > 0 and j > 0:
        if data[i-1][j-1] == '*':
            return True
    return False

def check_down_left(i,j, data):
    if i < len(data)-1 and j > 0:
        if data[i+1][j-1] == '*':
            return True
    return False

def check_up_right(i,j, data):
    if i > 0 and j < len(data[i])-1:
        if data[i-1][j+1] == '*':
            return True
    return False

def check_down_right(i,j, data):
    if i < len(data)-1 and j < len(data[i])-1:
        if data[i+1][j+1] == '*':
            return True
    return False


def check(i,j, data):
    if (
        check_up(i,j,data)
        or check_down(i,j,data)
        or check_left(i,j,data)
        or check_right(i,j,data)
        or check_up_left(i,j,data)
        or check_up_right(i,j,data)
        or check_down_left(i,j,data)
        or check_down_right(i,j,data)
    ):
        print("check = True " + str(i) + "," + str(j))
        return True

    if j < len(data[i])-1 and data[i][j+1] in numebers:
        return check(i, j+1, data)

    print("check = False " + str(i) + "," + str(j))
    return False


def get_number(i,j, data):
    num=0
    while j < len(data[i]) and data[i][j] in numebers:
        j += 1

    j -= 1
    count = 0
    
    while j >= 0 and data[i][j] in numebers:
        num += 10**count * numebers[data[i][j]]
        j=j-1
        count += 1
    print("Number: " + str(num))
    return num

# -----------MAIN-----------------

total = 0


for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] in numebers and (j == 0 or data[i][j-1] not in numebers):
            if check(i,j, data):
                print("Get Number")
                total += get_number(i,j, data)

print("Total: " + str(total))