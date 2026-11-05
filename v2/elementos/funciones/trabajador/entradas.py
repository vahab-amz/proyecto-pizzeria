"""Entradas comunes para los menús de gestión."""
from math import isfinite


def pedir_nombre(mensaje):
    while True:
        nombre = input(mensaje).strip()
        if nombre:
            return nombre
        print("El nombre no puede estar vacío.")


def pedir_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
        except ValueError:
            print("Introduce un número válido.")
            continue
        if isfinite(valor) and valor >= 0:
            return valor
        print("Introduce un número finito mayor o igual que cero.")
