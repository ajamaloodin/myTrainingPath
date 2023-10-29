texto = input("Escribe un texto y luego pulsa enter --> ")
letra1 = input("Escribe la primera letra y luego enter --> ")
letra2 = input("Escribe la segunda letra y luego enter --> ")
letra3 = input("Escribe la tercera letra y luego enter --> ")
texto = texto.upper()
letra1 = letra1.upper()
letra2 = letra2.upper()
letra3 = letra3.upper()
print(f"La letra {letra1} aparece {texto.count(letra1)} veces en el texto")
print(f"La letra {letra2} aparece {texto.count(letra2)} veces en el texto")
print(f"La letra {letra3} aparece {texto.count(letra3)} veces en el texto")
texto_a_lista = texto.split(" ")
print (f"El texto tiene un total de {len(texto_a_lista)} palabra(s)")
print(f"La primera letra del texto es {texto[0]} y la última es {texto[len(texto)-1]}")
texto_a_lista.reverse()
texto_inverso = ""
for item in texto_a_lista:
    texto_inverso = texto_inverso + item + " "
print(f"Su texto al invertir las palabras quedaría así:\n{texto_inverso}")
if "PYTHON" in texto_a_lista:
    print("La palabra PYTHON si se encuentra en su texto")
else:
    print("La palabra PYTHON no se encuentra en su texto")



