def score(x, y):
    calculus = (pow(x, 2) + pow(y, 2)) ** 0.5

    if calculus <= 1:
        return 10
    if calculus <= 5:
        return 5
    if calculus <= 10:
        return 1
    return 0