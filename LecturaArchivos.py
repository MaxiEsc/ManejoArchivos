'''
Para el manejo de archivos es importante tener en cuenta que:
'r' Es para la lectura de Archivos
'a' Es para el anexo de informacion de un archivo en caso de que exista y en caso de que no exista lo crea
'w' Abre un archivo para la escritura en caso de no existir este lo crea en consecuencia
'x' Crea un archivo en caso de no existir. Pero si este existe devuelve un error en consecuencia

't' escribe en archivo de tipo de texto.
'b' escribe el archivo en tipo binario.

'''

archivo = open('Prueba2.txt', 'r', encoding='utf8')
print(archivo.read()) #Lee toda la informacion completa comentar para realizar otras pruebas

# leer algunos caracteres
print(archivo.read(5)) #Lee solo 5 caracteres
print(archivo.read(3)) #Lee solo 3 caracteres

# leer lineas completas
print(archivo.readline())
print(archivo.readline())
