from concurrent.futures import ProcessPoolExecutor


def solve_problem(args):
    column, op = args

    if op == "+":
        return sum(column)

    elif op == "*":
        result = 1

        for num in column:
            result *= num

        return result


if __name__ == "__main__":

    with open("2025/DAY 6/Day6_Input.txt", "r") as file:
        data = file.read().splitlines()

    numbers = []

    for line in data[:-1]:
        numbers.append(list(map(int, line.split())))

    operators = data[-1].split()

    problems = list(zip(zip(*numbers), operators))

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(solve_problem, problems))

    total = sum(results)

    print(total)