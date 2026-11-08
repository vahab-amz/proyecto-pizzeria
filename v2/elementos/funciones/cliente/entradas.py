"""Entradas del cliente. Igual que en la versión 1 (v1/funciones/cliente/carrito.py)."""


# Pide una cantidad de 1 a 20. Devuelve 0 si el cliente cancela
def pedir_cantidad():
    while True:
        cantidad = input("¿Cuántas unidades quieres? (0 para cancelar): ").strip()
        if cantidad == "0":
            return 0
        if cantidad.isdigit() and 1 <= int(cantidad) <= 20:
            return int(cantidad)
        print("Cantidad no válida. Escribe un número del 1 al 20.")
