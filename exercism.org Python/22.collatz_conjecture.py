def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    paso = 0
    result = number
    while result != 1:
        paso += 1
        if result % 2 == 0:
            result = result / 2
        else:
            result = result * 3 + 1
    return paso