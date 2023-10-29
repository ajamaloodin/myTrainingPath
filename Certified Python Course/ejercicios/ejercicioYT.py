
from pathlib import Path

#  base = '/Users/macmini'
#  directorio = Path('Documents', 'Python', 'ejercicios')
#  ruta = Path(base, directorio, "salida.txt")
#  file = open("salida.txt", 'w')

suma_objetivo = 0
lista = [-7, -1, 8, -10, 6, 4, -8, 1, 7]
lista.sort()
print(lista)
items = len(lista)
posicion = 0
while posicion < items:
    apuntador_left = posicion + 1
    apuntador_right = items - 1
    while apuntador_left < apuntador_right:
        suma = lista[posicion] + lista[apuntador_left] + lista[apuntador_right]
        if suma == suma_objetivo:
            #  file.write(f'[{lista[posicion]}, {lista[apuntador_left]}, {lista[apuntador_right]}]')
            print(f'[{lista[posicion]}, {lista[apuntador_left]}, {lista[apuntador_right]}]')
            apuntador_left += 1
            apuntador_right -= 1
        elif suma < suma_objetivo:
            apuntador_left += 1
        else:
            apuntador_right -= 1
    posicion += 1
#  file.close()

