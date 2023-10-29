class Personaje:

    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas -= 1


class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Alumno(Persona):
    pass


palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)



todos = [palabra, lista, tupla]
#for item in todos:
#   print(len(item))



class Libro:
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return '"' + self.titulo + '"' + ", de " + self.autor

    def __len__(self):
        return self.cantidad_paginas


l1 = Libro("Conversaciones", "el pana", 120)

print(l1)
print(len(l1))
