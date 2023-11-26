import re

patron_sum = r'-?\d*\splus\s-?\d*'
patron_minus = r'-?\d*\sminus\s-?\d*'
patron_mult = r'-?\d*\smultiplied by\s-?\d*'
patron_div = r'-?\d*\sdivided by\s-?\d*'
patron_only_num = r'-?\d+'
operaciones = ['plus ', 'minus ', 'multiplied by ', 'divided by ']

patrones = [patron_sum, patron_minus, patron_mult, patron_div]


def check_syntax(cadena):
    patron = r'\d+\s\d+'
    patrones = [r'plus\s\D{4}', r'minus\s\D{4}', r'multiplied by\s\D{4}', r'divided by\s\D{4}']

    if cadena == "What is?":
        raise ValueError("syntax error")

    found = re.search(patron, cadena)
    if found:
        raise ValueError("syntax error")

    for patron2 in patrones:
        found = re.search(patron2, cadena)
        if found:
            print(found)
            raise ValueError("syntax error")


def do_calculation(suma, index, numbers):
    if index == 0:
        return suma + sum(numbers)
    if index == 1:
        if len(numbers) > 1:
            return numbers[0] - numbers[1]
        return suma - numbers[0]
    if index == 2:
        if len(numbers) > 1:
            return numbers[0] * numbers[1]
        return suma * numbers[0]
    if index == 3:
        if len(numbers) > 1:
            return numbers[0] / numbers[1]
        return suma / numbers[0]


def whats_operation(cadena):
    minimo = len(cadena)
    found = ""
    idx = 0
    for index, patron in enumerate(patrones):
        operation = re.search(patron, cadena)
        if operation:
            tupla = operation.span()
            if tupla[0] < minimo:
                minimo = tupla[0]
                found = operation
                idx = index
    return found, idx


def answer(cadena):
    check_syntax(cadena)
    long = len(cadena)
    numbers = []
    suma = 0
    if cadena.find('What is ') != -1:
        operation, index = whats_operation(cadena)
        if operation:
            extract = operation.group().split(operaciones[index])
            for idx, num in enumerate(extract):
                numero = re.findall(patron_only_num, num)
                numbers.append(int(numero[0]))
            tupla = operation.span()
            if cadena[tupla[1]] == '?':
                return do_calculation(suma, index, numbers)
            else:
                if (tupla[1] + 1) < long:
                    suma = do_calculation(suma, index, numbers)
                    cadena = cadena[tupla[1]:]
                    numbers = []
                    for index2, patron2 in enumerate(patrones):
                        operation = re.search(patron2, cadena)
                        if operation:
                            extract = operation.group().split(operaciones[index2])
                            for idx, num in enumerate(extract):
                                numero = re.findall(patron_only_num, num)
                                if numero:
                                    numbers.append(int(numero[0]))
                                    suma = do_calculation(suma, index2, numbers)
                            return suma
                    raise ValueError("syntax error")
                raise ValueError("syntax error")
        number = re.search(patron_only_num, cadena)
        if number:
            tupla = number.span()
            if cadena[tupla[1]] == '?':
                return int(number.group())
            else:
                for oper in operaciones:
                    oper = oper.strip(' ')
                    if oper in cadena:
                        raise ValueError("syntax error")
                raise ValueError("unknown operation")
        raise ValueError("syntax error")
    else:
        raise ValueError("unknown operation")