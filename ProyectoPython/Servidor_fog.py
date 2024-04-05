# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 08:35:55 2023

@author: Andre
"""

import socket
import csv
import os
from datetime import datetime
from CompresionHuffman import huffman_compress_csv
from CompresionRLE import rle_compress_csv
from APIDrive import upload_file

# Configuración del socket del servidor
server_host = 'localhost'
server_port = 12345

# Crea un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_host, server_port))
server_socket.listen(1)

print(f"Escuchando en {server_host}:{server_port}")

max_data_count = 30 #Cantidad de datos maxima en el archivo
current_data_count = 0

output_folder = "Datos/Sincomprimir"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

huffman_output_folder = "Datos/Huffman"
if not os.path.exists(huffman_output_folder):
    os.makedirs(huffman_output_folder)

rle_output_folder = "Datos/RLE"
if not os.path.exists(rle_output_folder):
    os.makedirs(rle_output_folder)

file_count = 1
data_list = []


while True:
    client_socket, client_address = server_socket.accept()
    print(f"Conexión aceptada desde {client_address}")

    while True:
        data_received = client_socket.recv(1024).decode()
        if not data_received:
            break

        print(f"Datos recibidos del cliente: {data_received}")

        try:
            data_as_float = float(data_received)
            data_list.append(data_as_float)
            current_data_count += 1

            if current_data_count >= max_data_count:
                timestamp = datetime.now().strftime("%Y%m%d%H%M")
                csv_file_path = os.path.join(output_folder, f'datos_{file_count}_{timestamp}.csv')

                with open(csv_file_path, 'w', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerows([data_list])

                #Compresion con Huffman
                huffman_file_base = os.path.join(huffman_output_folder, f'{file_count}_Huffman_{timestamp}')
                huffman_compress_csv(csv_file_path, f'{huffman_file_base}.csv', f'{huffman_file_base}.json')

                #Compresion con RLE
                rle_file_base = os.path.join(rle_output_folder, f'{file_count}_RLE_{timestamp}')
                rle_compress_csv(csv_file_path, f'{rle_file_base}.csv')

                # Calcula los tamaños de los archivos
                original_file_size = os.path.getsize(csv_file_path)
                huffman_csv_file_size = os.path.getsize(f'{huffman_file_base}.csv')
                huffman_json_file_size = os.path.getsize(f'{huffman_file_base}.json')
                rle_file_size = os.path.getsize(f'{rle_file_base}.csv')
                
                # Calcula el tamaño total de los archivos comprimidos con Huffman
                total_huffman_size = huffman_csv_file_size + huffman_json_file_size
                
                # Sube el archivo con menor tamaño (toma en cuenta el tamaño total en Huffman)
                if original_file_size <= total_huffman_size and original_file_size <= rle_file_size:
                    upload_file(csv_file_path)
                elif total_huffman_size <= rle_file_size:
                    upload_file(f'{huffman_file_base}.csv')
                    upload_file(f'{huffman_file_base}.json')
                else:
                    upload_file(f'{rle_file_base}.csv')


                file_count += 1
                data_list = []
                current_data_count = 0

        except ValueError:
            print(f"Error al convertir datos: {data_received}")

# client_socket.close()
# server_socket.close()
