# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 08:33:52 2023

@author: Andre
"""

from pymata4 import pymata4
import time
import socket

# Configuración del servidor en localhost
server_address = ('localhost', 12345)

board = pymata4.Pymata4()

analog_pin = 0
digital_pin = 8

board.set_pin_mode_analog_input(analog_pin)
board.set_pin_mode_analog_input(digital_pin)

def mapear_valor(valor, rango_entrada_min, rango_entrada_max, rango_salida_min, rango_salida_max):
    # Asegurarse de que el valor esté dentro del rango de entrada
    valor = max(rango_entrada_min, min(valor, rango_entrada_max))

    # Aplicar la regla de tres para mapear el valor al rango de salida
    resultado = int((valor - rango_entrada_min) * (rango_salida_max - rango_salida_min) / (rango_entrada_max - rango_entrada_min) + rango_salida_min)
    return resultado  # Devolver un número entero

# Crear el socket una vez antes del bucle while
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(server_address)
    
    while True:
        value, time_stamp = board.analog_read(analog_pin)
        print(value)
        valor_mapeado = mapear_valor(value, 0, 1023, 0, 100)
        print(int(valor_mapeado))
        
        # Enviar el valor mapeado al servidor
        s.sendall(str(int(valor_mapeado)).encode())

        
        time.sleep(60)
