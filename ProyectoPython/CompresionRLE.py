# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 08:07:13 2023

@author: Andre
"""
import csv

def rle_compress_csv(input_file, output_file):
    encoded_list = []
    with open(input_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            for symbol in row:
                if not encoded_list or symbol != encoded_list[-1][0]:
                    encoded_list.append((symbol, 1))
                else:
                    encoded_list[-1] = (symbol, encoded_list[-1][1] + 1)

    formatted_data = ",".join([f'({float(symbol):.2f}, {count})' for symbol, count in encoded_list])

    with open(output_file, 'w', newline='') as output_csv:
        output_csv.write(formatted_data)

"""if __name__ == "__main__":
    input_file = "datos.csv"  # Reemplaza con la ruta de tu archivo CSV
    output_file = "rle_encoded_data.csv"  # Archivo de salida para los datos comprimidos con RLE
    rle_compress_csv(input_file, output_file)"""
