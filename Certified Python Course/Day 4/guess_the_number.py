from random import *

numero = randrange(1,100)
jugar = "Y"
intentos = 1
jugador = input("Ok, dime tu nombre, por favor: ")
print(f"Bueno {jugador}, he pensado un número entre 1 y 100, y tienes solo 8 intentos para adivinarlo")
print(" ")
while jugar == "Y" and intentos <= 8:

    numero_dado = input(f"Ok intento Nro {intentos}, dime un numero del 1 al 100: ")
    numero_dado = int(numero_dado)
    if numero_dado < 1 or numero_dado > 100:
        print("Este número es inválido. Debe ser entre 1 y 100")
        intentos -= 1
    elif numero_dado < numero:
        print("respuesta es incorrecta, ya que has elegido un número menor al número secreto")
    elif numero_dado > numero:
        print("respuesta es incorrecta, ya que has elegido un número mayor al número secreto")
    elif numero_dado == numero:
        print(f"Felicitaciones! Acertaste al intento Nro: {intentos}")
        jugar = input("¿Seguir jugando? (Y/N)")
        jugar = jugar.upper()
        if jugar == "Y":
            intentos = 0
            numero = randrange(1, 100)
    if intentos == 8:
        print("Se han agotado el máximo de intentos\n")
        jugar = input("¿Seguir jugando? (Y/N)")
        jugar = jugar.upper()
        if jugar == "Y":
            intentos = 1
            numero = randrange(1, 100)
    else:
        intentos += 1


