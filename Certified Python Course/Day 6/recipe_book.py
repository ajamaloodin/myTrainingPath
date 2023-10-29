import os
from pathlib import Path
from os import system
import shutil

def limpia_consola():
    system('clear')

def cuenta_recetas(base, directorio):
    ruta = Path(base, directorio)
    recetas = []
    for file in Path(ruta).glob("**/*.txt"):
        recetas.append(file)
    return recetas


def categorias(base,directorio):
    ruta = Path(base, directorio)
    categoria = []
    for carpeta in Path(ruta).glob("**/"):
        categoria.append(carpeta.stem)
    return categoria

def leer_receta(all_cat, all_rec):
    print("Las categorías disponibles son:")
    opt = 0
    for cat in all_cat:
        opt += 1
        print(f"{str(opt)}-->{cat}")
    if opt == 0:
        print("No hay categorías disponibles")
    else:
        opcion = input("Por favor, elige el número de la Categoría: ")
        opcion = int(opcion)
        opcion -= 1
        recetas_asociadas = []
        opt = 0
        limpia_consola()

        for receta in all_rec:
            ruta1 = Path(receta)
            if ruta1.parent.name == all_cat[opcion]:
                if opt == 0:
                    print(f"Recetas Disponible en la Categoría:")
                opt += 1
                recetas_asociadas.append(receta)
                print(f"{str(opt)}-->{ruta1.name}")
        if opt == 0:
            print("No hay Recetas disponibles en esa Categoría")
        else:

            opcion = input("\nPor favor, elige el número de la Receta a leer: ")
            opcion = int(opcion)
            opcion -= 1
            archivo = open(recetas_asociadas[opcion])
            print("\nRECETA:")
            print(archivo.read())
            print(" ")
            archivo.close()
            enter = input("Pulse ENTER para regresar")
            limpia_consola()


def crear_receta(all_cat, base, directorio):
    print("Las categorías son:")
    opt = 0
    for cat in all_cat:
        opt += 1
        print(f"{str(opt)}-->{cat}")
    if opt == 0:
        print("No hay categorías disponibles. Contactar al Admin")
    else:
        opcion = input("Por favor, elige el número de la Categoría: ")
        opcion = int(opcion)
        opcion -= 1
        nombre_archivo = input("\nEscribe el nombre de tu nueva receta: ")
        nombre_archivo = nombre_archivo + '.txt'
        contenido = input("\nAhora escribe la receta: ")
        ruta = Path(base, directorio, all_cat[opcion], nombre_archivo)
        file = open(ruta, 'x')
        file.write(contenido)
        file.close()
        print("\nTu receta ha sido registrada!")
        enter = input("\n Enter para regresar...")
        limpia_consola()

def crear_categoria(base, directorio):
    limpia_consola()
    categoria = input("Cual es el nombre de la categoria: ")
    ruta = Path(base, directorio, categoria)
    os.mkdir(ruta)
    print(f"\nLa categoría {categoria} ha sido creada")
    enter = input("\nEnter para regresar...")

def eliminar_receta(all_cat, all_rec):
    print("Elija primero la categoría a la cual pertenece la receta a eliminar")
    opt = 0
    for cat in all_cat:
        opt += 1
        print(f"{str(opt)}-->{cat}")
    if opt == 0:
        print("No hay categorías disponibles. Contacte al Admin")
    else:
        opcion = input("Por favor, elige el número de la Categoría: ")
        opcion = int(opcion)
        opcion -= 1
        recetas_asociadas = []
        opt = 0
        limpia_consola()

        for receta in all_rec:
            ruta1 = Path(receta)
            if ruta1.parent.name == all_cat[opcion]:
                if opt == 0:
                    print(f"Recetas Disponible en la Categoría:")
                opt += 1
                recetas_asociadas.append(receta)
                print(f"{str(opt)}-->{ruta1.name}")
        if opt == 0:
            print("No hay Recetas disponibles en esa Categoría")
        else:
            opcion = input("\nPor favor, elige el número de la Receta a borrar: ")
            opcion = int(opcion)
            opcion -= 1
            os.remove(recetas_asociadas[opcion])
            print("\nLa receta ha sido eliminada!")
            enter = input("Pulse ENTER para regresar")
            limpia_consola()

def eliminar_categoria(all_cat, base, directorio):
    limpia_consola()
    print("Elija primero la categoría eliminar")
    opt = 0
    for cat in all_cat:
        opt += 1
        print(f"{str(opt)}-->{cat}")
    if opt == 0:
        print("No hay categorías disponibles. Contacte al Admin")
    else:
        opcion = input("Por favor, elige el número de la Categoría: ")
        opcion = int(opcion)
        opcion -= 1
        ruta = Path(base, directorio, all_cat[opcion])
        shutil.rmtree(ruta)
        print(f"\nLa categoría {all_cat[opcion]} ha sido eliminada")
    enter = input("\nEnter para regresar...")


base = Path.home()
dirRecetas = Path('Documents', 'Python', 'Dia6', 'Recetas')
todas_las_recetas = cuenta_recetas(base, dirRecetas)
todas_las_categorias = categorias(base, dirRecetas)
todas_las_categorias.pop(0)
limpia_consola()

print("Bienvenido al Administrador de Recetas")
print(" ")
print(f"Las Recetas se encuentran en:\n {dirRecetas}")
print(" ")
print(f"Hay disponible un total de {len(todas_las_recetas)} recetas.")


opcion = 0
while opcion != '6':
    print('''
             [1] Leer receta
             [2] Crear receta
             [3] Crear categoría
             [4] Eliminar receta
             [5] Eliminar Categoría
             [6] Salir''')
    opcion = input("Por favor, coloca tu opción y luego ENTER: ")
    limpia_consola()

    match opcion:
        case '1': leer_receta(todas_las_categorias, todas_las_recetas)
        case '2': crear_receta(todas_las_categorias, base, dirRecetas)
        case '3': crear_categoria(base, dirRecetas)
        case '4': eliminar_receta(todas_las_categorias, todas_las_recetas)
        case '5': eliminar_categoria(todas_las_categorias, base, dirRecetas)
        case '6': continue
        case   _: print("Opción inválida. Elija una de las seis opciones")





