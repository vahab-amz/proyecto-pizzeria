# Ejecutable para elegir la versión del programa
import time
import subprocess
import sys
from pathlib import Path
import os

os.system("cls")
carpeta_base = Path(__file__).resolve().parent
print("BIENVENIDO A LA PIZZERIA")
print("Actualmente hay 2 versiones del programa.")

while True:
    print("1. Version con Listas")
    print("2. Version con Objetos")
    print("0. Salir")

    opc = int(input("¿Qué versión quieres? "))

    match opc:
        case 1:
            carpeta_version = carpeta_base / "v1"
            print("Cargando versión de listas.")
            

        case 2:
            carpeta_version = carpeta_base / "v2"
            print("Cargando la versión de Objetos. ") 
            
        case 0:
            print("Hasta pronto")
            time.sleep(3)
            break
        case _:
            print("Opción incorrecta.")
            continue

    time.sleep(5)
    subprocess.run([sys.executable, str(carpeta_version / "main.py")], cwd=carpeta_version)