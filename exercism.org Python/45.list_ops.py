def append(list1, list2):
    return list1 + list2


def concat(lists):
    if len(lists) == 0:
        return lists
    result = []
    index = 0
    total_length = 0
    for item in lists:
        total_length += len(item)
    result = [None] * total_length
    for item in lists:
        for item2 in item:
            result[index] = item2
            index += 1
    return result


def filter(function, lista):
    result = []
    index = 0
    total_length = 0
    for item in lista:
        if function(item):
            total_length += 1
    if total_length != 0:
        result = [None] * total_length
        for item in lista:
            if function(item):
                result[index] = item
                index += 1
    return result


def length(lista):
    counter = 0
    for item in lista:
        counter += 1
    return counter


def map(function, lista):
    for index, item in enumerate(lista):
        lista[index] = function(item)
    return lista


def foldl(function, lista, initial=None):
    if len(lista) == 0:
        return initial
    if initial is None:
        value = next(list)
    else:
        value = initial
    for element in lista:
        value = function(value, element)
    return int(value)


def foldr(function, lista, initial=None):
    if len(lista) == 0:
        return initial
    lista = reverse(lista)
    if initial is None:
        value = next(list)
    else:
        value = initial
    for element in lista:
        value = function(value, element)
    return value


def reverse(lista):
    cuantos = len(lista)
    invertida = [None] * cuantos
    for i in range(0, cuantos):
        invertida[i] = lista[cuantos-i-1]
    return invertida