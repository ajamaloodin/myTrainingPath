def abrir_archivo(nombre_archivo):

    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")


def resta_vida(vida):
    while vida > -1:
        vida -= 1
        if vida > 0:
            yield f"Te quedan {vida} vidas"
        else:
            yield "Game Over"


vida = 8

perder_vida = resta_vida(vida)

print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))


