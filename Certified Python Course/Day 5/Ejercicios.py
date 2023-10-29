def devolver_distintos(i1, i2, i3):
    suma = i1 + i2 + i3
    if suma > 15:
        return max(i1, i2, i3)
    elif suma < 10:
        return min(i1, i2, i3)
    elif suma in range(10, 16):
        lista = [i1, i2, i3]
        lista.sort()
        return lista[1]

def transf_word(palabra):
    lista = []
    for l in palabra:
        lista.append(l)
    lista2 = []
    palabra_final = ""
    for letra in lista:
        if letra not in lista2:
            lista2.append(letra)
            palabra_final = palabra_final + letra
    return palabra_final

def do_not_like_ceros(*arg):
    lista = []
    for n in arg:
       lista.append(n)
    cantidad_arg = len(lista)
    if cantidad_arg <= 1:
        return False
    index = 0
    while index <= cantidad_arg-1:
        if lista[index] == lista[index+1] and lista[index] == 0:
            return True
        elif index == cantidad_arg - 2:
            return False
        else:
            index += 1




