def check_if_triangle(sides):
    s1 = sides[0]
    s2 = sides[1]
    s3 = sides[2]

    if s1 * s2 * s3 == 0:
        return False
    if s1 + s2 >= s3 and s2 + s3 >= s1 and s1 + s3 >= s2:
        return True
    return False


def equilateral(sides):
    if check_if_triangle(sides):
        check = set(sides)
        if len(check) == 1:
            return True
    return False


def isosceles(sides):
    if check_if_triangle(sides):
        check = set(sides)
        if len(check) == 2 or len(check) == 1:
            return True
    return False


def scalene(sides):
    if check_if_triangle(sides):
        check = set(sides)
        if len(check) == 3:
            return True
    return False