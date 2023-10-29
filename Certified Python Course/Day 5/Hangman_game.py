from random import choice


def elegir_palabra():
    lista_de_palabras = ["carro", "pleito", "avioneta", "raya"]
    return choice(lista_de_palabras)

def inicia_juego():
    print("Tienes seis(6) intentos")
    palabra = elegir_palabra()
    return palabra

def pedir_una_letra():
    letra = "1"
    while letra not in "abcdefghijklmnñopqrstuvwxyz":
        letra = input("Dime una letra: \n")
    return letra.lower()
def muestra_dibujo(dibujo):
    formato_dibujo = ""
    for item in dibujo:
        formato_dibujo = formato_dibujo + item + " "
    print(formato_dibujo)

def actualiza_dibujo(dibujo, letra, palabra):
    indice = 0
    Nro_adivinadas = 0
    for let in palabra:
        if let == letra:
            dibujo[indice] = letra
            Nro_adivinadas += 1
        indice += 1
    return dibujo, Nro_adivinadas

def checka_la_letra(letra, palabra, acertadas):
    if letra in palabra and letra not in acertadas:
        print("Acertaste esa letra!")
        return True
    else:
        return False


print("Bienvenido al Juego del Ahorcado!")
intentos = 0
la_palabra = inicia_juego()
cantidad_letras = len(la_palabra)
dibujo = []
dibujo = ["_"] * cantidad_letras
muestra_dibujo(dibujo)
letras_adivinadas = 0
adivinadas = 0
letras_acertadas = []

while intentos < 6:
    letra_en_juego = pedir_una_letra()
    if checka_la_letra(letra_en_juego, la_palabra, letras_acertadas):
        letras_acertadas.append(letra_en_juego)
        dibujo, adivinadas = actualiza_dibujo(dibujo, letra_en_juego, la_palabra)
        letras_adivinadas = letras_adivinadas + adivinadas
        muestra_dibujo(dibujo)
        if letras_adivinadas == cantidad_letras:
            print("Excelente! Ganaste!")
            break
    else:
        intentos += 1
    print(f"Ok, te quedan {6-intentos} intentos\n")
