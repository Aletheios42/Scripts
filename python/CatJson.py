#!/usr/bin/env python3
import json
import sys

def format_json(file_path):
    try:
        # Leer el archivo JSON
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        # Formatear y mostrar el JSON
        formatted_json = json.dumps(data, indent=4)
        print(formatted_json)
    
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no existe.")
    except json.JSONDecodeError:
        print(f"Error: El archivo '{file_path}' no contiene un JSON válido.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 format_json.py <ruta_al_archivo_json>")
    else:
        file_path = sys.argv[1]
        format_json(file_path)

