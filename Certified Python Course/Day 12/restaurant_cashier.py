from tkinter import *
import random
import datetime

# Iniciar Tkinter
aplicacion = Tk()

operador = ''

precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, resultado)
    operador = ''

def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_bebidas:
        if variables_bebida[x].get() == 1:
            cuadros_bebidas[x].config(state=NORMAL)
            if cuadros_bebidas[x].get() == '0':
                cuadros_bebidas[x].delete(0, END)
            cuadros_bebidas[x].focus()
        else:
            cuadros_bebidas[x].config(state=DISABLED)
            texto_bebidas[x].set('0')
        x += 1

    x = 0
    for c in cuadros_postres:
        if variables_postre[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0, END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1

def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebidas:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    sub_total_postre = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postre = sub_total_postre + (float(cantidad.get()) * precios_postres[p])
        p += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre
    impuestos = sub_total * 0.07  # suponiendo que ese sea el impuesto
    total = sub_total + impuestos

    var_costo_comida.set(f'$ {round(sub_total_comida, 2)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida, 2)}')
    var_costo_postre.set(f'$ {round(sub_total_postre, 2)}')
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuesto.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')

def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000,9999)}'
    fecha = datetime.datetime.today()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 95 + '\n')
    texto_recibo.insert(END, f'Items\t\tCant.\tCosto Item' + '\n')
    texto_recibo.insert(END, f'-' * 95 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t'
                                     f'${int(comida.get()) * precios_comida[x]}\n')
        x += 1
    x = 0
    for bebida in texto_bebidas:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t'
                                     f'${int(bebida.get()) * precios_bebida[x]}\n')
        x += 1
    x = 0
    for postre in texto_postres:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t'
                                     f'${int(postre.get()) * precios_postres[x]}\n')
        x += 1

    texto_recibo.insert(END, f'-' * 95 + '\n')
    texto_recibo.insert(END, f'Costo de las comidas: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de las bebidas: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo de los postres: \t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 95 + '\n')
    texto_recibo.insert(END, f'Subtotal: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f'Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 95 + '\n')
    texto_recibo.insert(END, f'Gracias por su visita!')

# tamaño de la ventana
aplicacion.geometry("1020x630")

# Evitar que el usuario maximice la pantalla
aplicacion.resizable(0,0)

# Titulo de la ventana
aplicacion.title("Mi Restaurante - Sistema de Facturación")

# Color de fondo de la ventana
aplicacion.config(bg="CadetBlue")

# Panel Superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# Etiqueta del titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturación', fg='black',
                        font=('Arial', 58), bg='CadetBlue', width=27)
etiqueta_titulo.grid(row=0, column=0)

# Panel Izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='Grey', padx=50)
panel_costos.pack(side=BOTTOM)

# Panel Comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Arial', 18, 'bold'),
                           bd=1, relief=FLAT, fg='CadetBlue')
panel_comidas.pack(side=LEFT)

# Panel Bebidas
panel_bedidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Arial', 18, 'bold'),
                           bd=1, relief=FLAT, fg='CadetBlue')
panel_bedidas.pack(side=LEFT)

# Panel Postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Arial', 18, 'bold'),
                           bd=1, relief=FLAT, fg='CadetBlue')
panel_postres.pack(side=LEFT)

# Panel Derecho
panel_derecho = Frame(aplicacion,
                      bd=1,
                      relief=FLAT)
panel_derecho.pack(side=RIGHT)

# Panel Calculadora
panel_calculadora = Frame(panel_derecho,
                          bd=1,
                          relief=FLAT,
                          bg='CadetBlue')
panel_calculadora.pack()  # si no pones nada, por default va arriba

# Panel recibo
panel_recibo = Frame(panel_derecho,
                     bd=1,
                     relief=FLAT,
                     bg='CadetBlue')
panel_recibo.pack()

# Panel botones
panel_botones = Frame(panel_derecho,
                      bd=1,
                      relief=FLAT,
                      bg='CadetBlue')
panel_botones.pack()

# Lista de productos
lista_comidas = ['pollo', 'cordero', 'salmon', 'merluza', 'kebab', 'pizza1', 'pizza2', 'pizza3']
lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino1', 'vino2', 'cerveza1', 'cerveza2']
lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'mousse', 'pastel1', 'pastel2', 'pastel3']

# Generar item comidas
variables_comida = []
cuadros_comida = []
texto_comida = []

contador = 0
for comida in lista_comidas:

    # Crear los check buttons
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Arial', 18, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W)

    # cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Arial', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)
    contador += 1

# Generar item bebidas
variables_bebida = []
cuadros_bebidas = []
texto_bebidas = []
contador = 0
for bebida in lista_bebidas:

    # Crear los check buttons
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bedidas,
                         text=bebida.title(),
                         font=('Arial', 18, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador],
                         command=revisar_check)
    bebida.grid(row=contador,
                column=0,
                sticky=W)

    # cuadros de entrada
    cuadros_bebidas.append('')
    texto_bebidas.append('')
    texto_bebidas[contador] = StringVar()
    texto_bebidas[contador].set('0')
    cuadros_bebidas[contador] = Entry(panel_bedidas,
                                     font=('Arial', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebidas[contador])
    cuadros_bebidas[contador].grid(row=contador,
                                   column=1)
    contador += 1

# Generar item postres
variables_postre = []
cuadros_postres = []
texto_postres = []
contador = 0
for postre in lista_postres:

    # Crear los check buttons
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Arial', 18, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postre[contador],
                         command=revisar_check)
    postre.grid(row=contador,
                column=0,
                sticky=W)

    # cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres,
                                      font=('Arial', 18, 'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador,
                                   column=1)
    contador += 1

# Variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# Etiqueta de costo y campos de entrada COMIDA

etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comidas',
                              font=('Arial', 12, 'bold'),
                              bg='Grey',
                              fg='white')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Arial', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1)

# Etiqueta de costo y campos de entrada BEBIDA

etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo bebidas',
                              font=('Arial', 12, 'bold'),
                              bg='Grey',
                              fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=('Arial', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

# Etiqueta de costo y campos de entrada POSTRES

etiqueta_costo_postre = Label(panel_costos,
                              text='Costo postres',
                              font=('Arial', 12, 'bold'),
                              bg='Grey',
                              fg='white')
etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(panel_costos,
                           font=('Arial', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)

# Etiqueta de costo y campos de entrada SUBTOTAL

etiqueta_subtotal = Label(panel_costos,
                          text='Subtotal',
                          font=('Arial', 12, 'bold'),
                          bg='Grey',
                          fg='white')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos,
                       font=('Arial', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

# Etiqueta de costo y campos de entrada IMPUESTOS

etiqueta_impuesto = Label(panel_costos,
                          text='Impuesto',
                          font=('Arial', 12, 'bold'),
                          bg='Grey',
                          fg='white')
etiqueta_impuesto.grid(row=1, column=2)

texto_impuesto = Entry(panel_costos,
                       font=('Arial', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_impuesto)
texto_impuesto.grid(row=1, column=3, padx=41)

# Etiqueta de costo y campos de entrada TOTAL

etiqueta_total = Label(panel_costos,
                       text='Total',
                       font=('Arial', 16, 'bold'),
                       bg='Grey',
                       fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                    font=('Arial', 16, 'bold'),
                    bd=1,
                    width=10,
                    state='readonly',
                    textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

# Botones
botones = ['Total', 'Recibo', 'Guardar', 'Resetear']
botones_creados = []

columnas = 0

for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Arial', 14, 'bold'),
                   fg='Black',
                   bg='Grey',
                   bd=1,
                   width=9)
    boton.grid(row=0,
               column=columnas)
    botones_creados.append(boton)

    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)

# Area Recibo
texto_recibo = Text(panel_recibo,
                    font=('Arial', 12, 'bold'),
                    bd=1,
                    width=60,
                    height=12)
texto_recibo.grid(row=0,
                  column=0)

# Calculadora A PIE (JODER)
visor_calculadora = Entry(panel_calculadora,
                          font=('Arial', 12, 'bold'),
                          bd=1,
                          width=60)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-',
                       '1', '2', '3', 'x', 'R', 'B', '0', '/']
botones_guardados = []

fila = 1  # Ya que la columna 0 esta ocupada por el visor
columna = 0

for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Arial', 16, 'bold'),
                   fg='Black',
                   bg='Grey',
                   bd=1,
                   width=8)
    boton.grid(row=fila,
               column=columna)
    botones_guardados.append(boton)

    if columna == 3:
        fila += 1
    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: click_boton('0'))
botones_guardados[15].config(command=lambda: click_boton('/'))

# Evitar que la pantalla se cierre
aplicacion.mainloop()