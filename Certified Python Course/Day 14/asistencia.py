import face_recognition as fr
import os
import numpy
from datetime import datetime

# Crear B/D con las imagenes de los empleados
ruta = 'Empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = fr.load_image_file(f'{ruta}/{nombre}', 'RGB')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

# Codificar imagenes
def codificar_imagenes(imagenes):

    # Crear una lista nueva
    lista_codificada = []

    for imagen in imagenes:
        # Codificar
        codificado = fr.face_encodings(imagen)[0]

        lista_codificada.append(codificado)

    # Devolver lista codificada
    return lista_codificada


def registrar_ingreso(persona):

    f = open('registro.csv', 'r+')
    lista_archivo = f.readlines()
    empleados_registrados = []
    for linea in lista_archivo:
        ingreso = linea.split(',')
        empleados_registrados.append(ingreso[0])

    if persona not in empleados_registrados:
        ahora = datetime.now()
        formato = ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona}, {formato}')

    f.close()




lista_empleados_codificada = codificar_imagenes(mis_imagenes)

foto_control_acceso = fr.load_image_file('FotoA.jpg')

# reconocer la cara

#localizar cara control
cara_captura = fr.face_locations(foto_control_acceso)[0]
cara_captur_codificada = fr.face_encodings(foto_control_acceso)[0]

# Buscar coincidencias para dar acceso al empleado de foto_control_acces
coincidencias = fr.compare_faces(lista_empleados_codificada, cara_captur_codificada)
distancias = fr.face_distance(lista_empleados_codificada, cara_captur_codificada)

indice_coincidencia = numpy.argmin(distancias)

# Evaluar la coincidecia
if distancias[indice_coincidencia] > 0.6:
    print("Acceso Denegado. No coincide con la B/D de Empleados")
else:
    # Mostrar el nombre el empleado coincidente

    nombre = nombres_empleados[indice_coincidencia]
    registrar_ingreso(nombre)

