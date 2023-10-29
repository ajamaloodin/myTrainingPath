from collections import Counter
from collections import defaultdict
from collections import deque
import os
import datetime
import re
import zipfile

lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

contador = Counter(lista)

# print(contador)

mi_diccionario = defaultdict(lambda: "nada")
mi_diccionario["edad"] = '44'

lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

# print(os.getcwd())

archivo = open("archivo.txt", 'w')
archivo.write("Esto es una prueba")
archivo.close()

# print(os.listdir())
'''
patron = 'Hola'

correo = 'Hola como esta la cosa'

resultado = re.search(patron, correo)
if resultado:
    if resultado.start() == 0:
        print("fino")
    else:
        print("esta pero no en 1")
else:
    print('no way jose')


patron = r'\w{2}\d{4}'
codigo = "P1234"
resultado = re.search(patron,codigo)
if resultado:
    print("fino")
'''
mi_zip = zipfile.ZipFile("Proyecto+Dia+9.zip", 'r')
mi_zip.extractall()

