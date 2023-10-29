import face_recognition as fr

#Cargar imagenes
foto_control = fr.load_image_file('FotoA.jpg')
foto_prueba = fr.load_image_file('FotoB.jpg')

#Pasar imagenes de BGR a RGB no se pudo por el fucking paquete opencv-python (cv2)

#localizar cara control
lugar_cara_A = fr.face_locations(foto_control)[0]
cara_codificada_A = fr.face_encodings(foto_control)[0]

#localizar cara prueba
lugar_cara_B = fr.face_locations(foto_prueba)[0]
cara_codificada_B = fr.face_encodings(foto_prueba)[0]

#comparar caras
resultado = fr.compare_faces([cara_codificada_A], cara_codificada_B)
print(resultado)

#el valor de la distancia de comparacion como medida. El default es 0.6
distancia = fr.face_distance([cara_codificada_A], cara_codificada_B)
