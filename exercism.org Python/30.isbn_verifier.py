import re


def is_valid(isbn):

    if len(isbn) == 0:
        return False

    if isbn[-1] not in '0123456789X':
        return False

    patron = r'\d{1}-\d{3}-\d{5}-'
    patron2 = r'\d{10}'
    patron3 = r'\d{9}X'
    if not re.search(patron, isbn):
        if not re.search(patron2, isbn):
            if not re.search(patron3, isbn):
                return False
        elif len(isbn) > 10:
            return False

    patron4 = r'\d'
    digits = re.findall(patron4, isbn)

    sum = 0
    qdigits = len(digits)
    for index in range(10, 1, -1):
        sum += int(digits[10-index]) * index
    if qdigits == 9:
        sum = sum + 10
    else:
        sum = sum + int(digits[9])

    if sum % 11 == 0:
        return True
    return False








