def is_armstrong_number(number):
    tostr = str(number)
    separated = list(tostr)
    potencia = len(separated)

    suma = 0
    for item in separated:
        suma = suma + int(item)**potencia

    if suma == number:
        return True
    return False