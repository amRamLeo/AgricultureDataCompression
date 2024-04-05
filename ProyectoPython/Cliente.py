# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:33:49 2023

@author: Andre
"""
import socket
import time
import random

# Configura el socket del cliente
server_host = 'localhost'  # Utiliza 'localhost' para la misma máquina
server_port = 12345  # Puerto de destino para el servidor

# Crea un socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conéctate al servidor
client_socket.connect((server_host, server_port))

# Valor inicial de humedad
humidity = 0.6

while True:
    # Cambia gradualmente la humedad en un rango pequeño
    humidity += random.uniform(-0.005, 0.005)
    
    # Limita la humedad a un rango entre 0 y 1
    humidity = max(0, min(1, humidity))
    
    data_to_send = f"{humidity:.2f}"  # Formatea el valor en una cadena de texto
    
    # Envía los datos al servidor
    client_socket.send(data_to_send.encode())
    print(f"Dato enviado al servidor: {data_to_send}")
    
    time.sleep(0.5)  # Espera 1 segundo antes de enviar el próximo dato

# client_socket.close()
