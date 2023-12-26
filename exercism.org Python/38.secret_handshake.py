def commands(binary_str):
    keys = ['wink', 'double blink', 'close your eyes', 'jump']
    msg = []
    lista = list(binary_str)

    invert = False
    if lista[0] == '1':
        invert = True

    lista.reverse()
    lista.pop()

    for index, digit in enumerate(lista):
        if digit == '1':
            msg.append(keys[index])

    if invert:
        msg.reverse()
    return msg