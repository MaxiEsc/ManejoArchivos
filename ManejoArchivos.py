'''Refrescando la idea de archivos en Python es mucho mas intuitivo'''

try:
    archivo = open('Prueba1.txt', 'w')
    archivo.write('Agregamos información al archivo\n')
    archivo.write('Se realiza ciertas pruebas en el archivo\n')
    archivo.write('Se realizar Pruebas en el mismo\n')
    archivo.write('Se revisa el archivo con su extencion correspondiente\n')
    archivo.write('Hay caracteres faltantes\n')
    archivo.write('Caracteres especiales faltanes áééióúññññ\n')

    archivo.write('Adios')
except Exception as e:
    print(e)
finally:
    archivo.close()