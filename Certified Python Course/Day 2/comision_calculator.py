nombre = input("Cuál es tu nombre?: ")
ventas = input("Cuanto vendiste " + nombre + "? :")
ventas = float(ventas)
comision = round(ventas*0.13,2)
print(f"Ok {nombre}, tu comisión es: {comision}")