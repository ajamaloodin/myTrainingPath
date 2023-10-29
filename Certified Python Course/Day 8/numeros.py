# Definiendo los generadores para cada area de atencion
def generador_perfurmeria():
    n = 1
    while True:
        yield str(n)
        n += 1


def generador_farmacia():
    n = 1
    while True:
        yield str(n)
        n += 1


def generador_cosmeticos():
    n = 1
    while True:
        yield str(n)
        n += 1

f = generador_farmacia()
p = generador_perfurmeria()
c = generador_cosmeticos()

def decorador(dpto):

    print(f"Su turno es el:")
    if dpto == '1':
        print(f"F - {next(f)}")
    elif dpto == '2':
        print(f"P - {next(p)}")
    else:
        print(f"C - {next(c)}")
    print("Espere su turno con paciencia :)")
