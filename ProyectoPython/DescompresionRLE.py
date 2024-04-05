# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 16:00:21 2023

@author: Andre
"""

import csv
import re

def rle_decode(encoded_list):
    decoded_list = []
    for element, count in encoded_list:
        decoded_list.extend([element] * count)
    return decoded_list

def rle_descomprimir_csv(nombre_archivo, output_file):
    # Lista para almacenar los valores de humedad descomprimidos
    datos_descomprimidos = []

    # Abre el archivo CSV
    with open(nombre_archivo, mode='r') as archivo_csv:
        # Lee el contenido del archivo como una sola cadena
        csv_data = archivo_csv.read()

        # Utiliza una expresión regular para encontrar los pares (valor, cantidad) en la cadena
        matches = re.findall(r'\(([^)]+)\)', csv_data)

        for match in matches:
            valor, cantidad = match.split(',')
            valor = float(valor)
            cantidad = int(cantidad)
            datos_descomprimidos.append((valor, cantidad))

    # Descomprime los datos utilizando la función rle_decode
    datos_descomprimidos = rle_decode(datos_descomprimidos)

    # Escribe los datos descomprimidos en el archivo de salida
    with open(output_file, 'w') as output_csv:
        writer = csv.writer(output_csv)
        writer.writerow(datos_descomprimidos)

"""# Ejemplo de uso:
nombre_archivo = 'Datos/RLE/31_RLE_202310211300.csv'
output_file = 'Resultado/DatosDescomprimidos/31_Descomprimido_202310211300.csv'
rle_descomprimir_csv(nombre_archivo, output_file)"""


