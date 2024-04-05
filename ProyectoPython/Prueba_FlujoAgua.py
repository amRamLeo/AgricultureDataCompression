# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 16:27:19 2023

@author: Andre
"""

import serial
import time
import socket

# Inicializa variables
list_in_floats = []
max_readings = 30  # Número de lecturas para guardar en el archivo CSV
readings_count = 0  # Inicializa el contador como global

# Configuración del servidor
server_address = ('localhost', 12345)

def main_func():
    global readings_count  # Declarar readings_count como global
    arduino = serial.Serial('COM4', 9600)  # Cambia 'COM4' al puerto COM correcto
    print('Conexión serial establecida con Arduino')

    # Configura el socket para enviar datos al servidor
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.connect(server_address)
        print(f'Conexión establecida con el servidor en {server_address}')

        while True:
            arduino_data = arduino.readline()

            if arduino_data:
                decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
                list_values = decoded_values.split('\n')

                for item in list_values:
                    if item:
                        value = float(item)
                        print(f'Lectura recopilada desde Arduino: {value}')  # Imprime la lectura
                        list_in_floats.append(value)
                        readings_count += 1

                        # Envía el dato al servidor
                        server_socket.sendall(str(value).encode())

    arduino.close()  # Esto se ejecutará cuando se detenga manualmente el programa

# Ejecuta la función principal
if __name__ == "__main__":
    main_func()

