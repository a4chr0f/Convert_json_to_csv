#!/bin/python3
#author: achrafelk

import csv
import json
import signal
import sys

def conviete_Json_al_Csv(json_data, csv_file):
    with open(json_data) as file:
        data = json.load(file)

    keydata = list(data[0].keys())
    with open(csv_file, 'w', newline='') as f:

        escribir = csv.DictWriter(f, fieldnames=keydata)
        escribir.writeheader()
        
        for fila in data:
            escribir.writerow(fila)

    
    print("La conversión de JSON a CSV se ha completado exitosamente")


def signal_handler(signal, frame):
    print("\n Se ha presionado Ctrl+C. Saliendo...")
    sys.exit(0)



if __name__ == '__main__':
    # Asociar el manejador de señal con la señal SIGINT (Ctrl+C)
    signal.signal(signal.SIGINT, signal_handler)
    print("                                _         _                  _                       ")
    print("                               | |       (_)                | |                      ")
    print("   ___ ___  _ ____   _____ _ __| |_       _ ___  ___  _ __  | |_ ___   ___ _____   __")
    print("  / __/ _ \| '_ \ \ / / _ \ '__| __|     | / __|/ _ \| '_ \ | __/ _ \ / __/ __\ \ / /")
    print(" | (_| (_) | | | \ V /  __/ |  | |_      | \__ \ (_) | | | || || (_) | (__\__ \\ V / ")
    print("  \___\___/|_| |_|\_/ \___|_|   \__|     | |___/\___/|_| |_| \__\___/ \___|___/ \_/  ")
    print("                                 ______ _/ |             ______   ______             ")
    print("                                |______|__/             |______| |______|            ")
    print("                                                                                     ")
    print("                                  creado por : asfelk                                ")
    
    file_json = input("Ingrese la ruta del archivo JSON: ")
    file_csv = input("Ingrese la ruta del archivo CSV para guardar los datos: ")
    conviete_Json_al_Csv(file_json, file_csv)    
