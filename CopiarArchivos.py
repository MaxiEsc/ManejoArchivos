'''Se realiza la apertura de 2 archiva mientras se itera'''
archivo = open('Prueba2.txt', 'r', encoding='utf8') #Siempre leer el archivo que tenga el mismo tipo de codificacion.
#print(archivo.read())

# leer algunos caracteres
# print(archivo.read(5))
# print(archivo.read(3))

# leer lineas completas
# print(archivo.readline())
# print(archivo.readline())

# iterar el archivo
#for linea in archivo:
#     print(linea)

# leer lineas
# print(archivo.readlines())

# acceder a una linea de la lista
# print(archivo.readlines()[2])

# abrimos un nuevo archivo
# a - anexar informacion
archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()
print('se ha terminado el proceso de leer y copiar archivos')