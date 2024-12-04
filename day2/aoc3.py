def safec(a:int, b:int):
    diff = abs(a - b)
    return diff >= 1 and diff <= 3

def is_monotonic(row:list):
    is_increasing = all(int(row[i]) <= int(row[i + 1]) for i in range(len(row) - 1))
    is_decreasing = all(int(row[i]) >= int(row[i + 1]) for i in range(len(row) - 1))
    return is_increasing or is_decreasing

def safec_row(row:list):
    for i in range(len(row)-1):
        if not safec(int(row[i]), int(row[i+1])):
            return False
    return True

def check_levels(row:list):
    if not safec_row(row):
        return 0
    if is_monotonic(row):
        return 1
    else:
        return 0

def buffer_check_levels(row:list):
    issues = False
    for i in range(len(row)-1):
        if not safec(int(row[i]), int(row[i+1])):
            issues = True
    if is_monotonic(row) and issues == False:
        return 1
    else:
        for i in range(len(row)):
            temp_row = row[:i] + row[i+1:]
            if is_monotonic(temp_row) and safec_row(temp_row):
                return 1
        return 0

if __name__ == "__main__":
    with open('day2/input.txt', 'r') as f:
        biglist = list()
        for line in f:
            row = line.strip().split()
            biglist.append(row)

    safelist = list()
    for row in biglist:
        num = check_levels(row)
        safelist.append(num)

    print(sum(safelist))


    safelist = list()
    for row in biglist:
        num = buffer_check_levels(row)
        safelist.append(num)

    print(sum(safelist))
