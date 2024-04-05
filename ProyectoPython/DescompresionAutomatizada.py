# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:15:01 2023

@author: Andre
"""

import os
import json
from DescompresionHuffman import huffman_descomprimir_csv
from DescompresionRLE import rle_descomprimir_csv

# Directorio de archivos comprimidos
directorio_comprimidos = "Resultado\DatosComprimidos"

# Directorio de archivos descomprimidos
directorio_descomprimidos = "Resultado\DatosDescomprimidos"

# Listar archivos en el directorio de comprimidos
archivos_comprimidos = os.listdir(directorio_comprimidos)

# Procesar cada archivo comprimido
for archivo in archivos_comprimidos:
    # Verificar la extensión del archivo
    if archivo.endswith(".csv"):
        ruta_comprimido = os.path.join(directorio_comprimidos, archivo)
        ruta_descomprimido = os.path.join(directorio_descomprimidos, archivo)  # Mismo nombre para el descomprimido
        
        # Extraer la técnica de compresión del nombre del archivo
        tecnica_compresion = archivo.split("_")[1]
        
        if tecnica_compresion == "Huffman":
            # Si es Huffman, necesitas el archivo JSON con el diccionario
            diccionario_huffman = archivo.replace("csv", "json")
            ruta_diccionario_huffman = os.path.join(directorio_comprimidos, diccionario_huffman)
            
            # Realizar la descompresión con Huffman
            huffman_descomprimir_csv(ruta_comprimido, ruta_diccionario_huffman, ruta_descomprimido)
        elif tecnica_compresion == "RLE":
            # Realizar la descompresión con RLE
            rle_descomprimir_csv(ruta_comprimido, ruta_descomprimido)
        else:
            print(f"Técnica de compresión no reconocida en el archivo: {archivo}")
