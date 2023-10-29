import os
import datetime
import re
from pathlib import Path
import time
import math

patron = r'N\D{3}-\d{5}'

print("-"*45)
print("Fecha de Búsqueda: " + str(datetime.date.today()))
print("\nArchivo\t\t\tNro de Serie")
print("-------\t\t\t------------")

ruta_ppal = '/Users/macmini/Documents/Python/Dia9/Mi_Gran_Directorio'
arbol = os.walk(ruta_ppal)
cuantos = 0
inicio = time.time()
for carpeta, subcarpeta, archivo in arbol:
    pass
    for sub in subcarpeta:
        pass
    for arch in archivo:
        if arch[0].upper() == "A":
            ruta = Path(carpeta, arch)
            filer = open(ruta, 'r')
            contenido = filer.read()
            if re.search(patron, contenido):
                cuantos += 1
                lista = re.findall(patron, contenido)
                for item in lista:
                    print(f"{arch}\t{item}")
            filer.close()
final = time.time()
duracion = final - inicio
print(f"\nNúmero de Encontrados: {cuantos}")
print(f"Duración de la Búsqueda: {math.ceil(duracion)} segundo(s)")
print("-"*45)
