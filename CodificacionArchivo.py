'''Refrescando la idea de archivos en Python es mucho mas intuitivo parte 2'''

try:
    archivo = open('Prueba2.txt', 'w', encoding='utf8')
    archivo.write('Agregamos información al archivo\n')
    archivo.write('Se realiza ciertas pRuebas en el archivo\n')
    archivo.write('Se realizar Pruebas en el mismo\n')
    archivo.write('Se revisa el archivo con su extencion correspondiente\n')
    archivo.write('Se prueban caracteres especiales\n')
    archivo.write('Vocales: Á É Í Ó Ú\n')
    archivo.write('Adios')
except Exception as e:
    print(e)
finally:
    archivo.close()
    print('Fin del archivo')
    # archivo.write('nueva info')