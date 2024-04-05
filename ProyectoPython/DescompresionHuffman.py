# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 07:34:33 2023

@author: Andre
"""

import json
import csv

def huffman_descomprimir_csv(compressed_data_file, huffman_dict_file, output_file):
    with open(huffman_dict_file, 'r') as dict_file:
        huffman_codes = json.load(dict_file)

    reverse_huffman_codes = {code: symbol for symbol, code in huffman_codes.items()}

    with open(compressed_data_file, 'r') as compressed_file:
        with open(output_file, 'w') as output_csv:
            writer = csv.writer(output_csv)
            for line in compressed_file:
                compressed_symbols = line.strip().split(',')
                symbols = [reverse_huffman_codes[code] for code in compressed_symbols]
                writer.writerow(symbols)

"""if __name__ == "__main__":
    compressed_data_file = "Datos/Huffman/31_Huffman_202310211300.csv"
    huffman_dict_file = "Datos/Huffman/31_Huffman_202310211300.json"
    output_file = "Resultado/DatosDescomprimidos/decompressed.csv"
    huffman_descomprimir_csv(compressed_data_file, huffman_dict_file, output_file)


#descompresion

"""