from numeros import *
from os import system


def limpia_consola():
    system('clear')


limpia_consola()

opcion = 0


while opcion != '4':
    print('''
             [1] Farmacia
             [2] Perfumería
             [3] Cosméticos
             [4] Salir''')
    opcion = input("\nPor favor, coloca tu opción y luego ENTER: ")
    limpia_consola()
    if opcion == '1':
        decorador('1')
    elif opcion == '2':
        decorador('2')
    elif opcion == '3':
        decorador('3')

