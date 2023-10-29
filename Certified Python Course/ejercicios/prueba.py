import collections

#  items = ["coal", "coal", "coal", "coal", "wood", "wood", "diamond", "diamond", "diamond", "diamond"]
'''
invent = collections.Counter()
for item in items:
    invent[item] += 1
diccionario = dict(invent)
print(diccionario)
'''

def create_inventory(items):
    invent = {}
    long = len(items)
    procesada = []
    for index, item in enumerate(items):
        if item not in procesada:
            count = 1
            index2 = index + 1
            while index2 < long and item not in procesada:
                if item in items[index2::]:
                    count += 1
                index2 += 1
            invent[item] = count
            procesada.append(item)
    return invent


def add_inventory(inventory, items):

    items.sort()
    nuevos = create_inventory(items)

    for key, value in nuevos.items():
        if inventory.get(key, 'nei') == 'nei':
            inventory[key] = value
        else:
            inventory[key] = inventory[key] + value
    return inventory


def decrement_items(inventory, items):

    items.sort()
    nuevos = create_inventory(items)

    for key, value in nuevos.items():
        if inventory.get(key, 'nei') != 'nei':
            new_value = inventory[key] - value
            if new_value < 0:
                new_value = 0
            inventory[key] = new_value

    return inventory


def remove_item(inventory, item):

    inventory.pop(item,'not_there')
    return inventory

def list_inventory(inventory):

    lista = []
    latupla = tuple()
    for key, value in inventory.items():
        if value != 0:
            latupla = (key,value)
            lista.append(latupla)
    return lista


inventory = {"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}

# print(list_inventory(inventory))

ultimo = 1
penultimo = 0
numero_de_terminos = int(input('Cantida de termino:'))
nuevo = 0
lista = []
lista.append(penultimo)
lista.append(ultimo)
for index in range(numero_de_terminos-2):
    nuevo = penultimo + ultimo
    lista.append(nuevo)
    penultimo = ultimo
    ultimo = nuevo
print(lista)



