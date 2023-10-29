from os import system
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, nrocta, balance):
        super().__init__(nombre, apellido)
        self.nrocta = nrocta
        self.balance = balance

    def __str__(self):
        return "Nombre: " + self.nombre + " Apellido: " + self.apellido + " Balance: " + str(self.balance)

    def depositar(self, monto):
        self.balance = self.balance + monto

    def retirar(self, monto):
        self.balance = self.balance - monto

def limpia_consola():
    system('clear')

def crear_cliente():
    nombre = input("Cual es el nombre del cliente: ")
    apellido = input("Cual es el apellido del cliente: ")
    cuenta = input("Nro de cuenta?: ")
    balance = float(input("Balance actual "))
    cliente = Cliente(nombre, apellido, cuenta, balance)
    return cliente


cliente = crear_cliente()
opcion = '1'
limpia_consola()

while opcion != '4':
    print('''
                 [1] Consultar Balance
                 [2] Depositar 
                 [3] Retirar
                 [4] Salir''')
    opcion = input("Por favor, coloca tu opción y luego ENTER: ")
    limpia_consola()
    if opcion == '1':
        print(cliente)
    elif opcion == '2':
        monto = float(input("Monto a depositar?: "))
        cliente.depositar(monto)
    elif opcion == '3':
        monto = float(input("Monto a retirar?: "))
        if monto <= cliente.balance:
            cliente.retirar(monto)
        else:
            print("Balance insuficiente para retirar")