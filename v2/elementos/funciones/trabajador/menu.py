from elementos.funciones.trabajador.gestion_almacen import gestionar_almacen
from elementos.funciones.trabajador.gestion_ofertas import gestionar_ofertas
from elementos.funciones.trabajador.gestion_pizza import gestionar_pizzas



def menu_trabajador():
    while True:
        print("\n--- MENÚ TRABAJADOR ---")
        print("1. Gestionar pizzas")
        print("2. Gestionar almacén")
        print("3. Gestionar ofertas")
        print("0. Volver")

        opcion = input("Elige una opción: ").strip()
        match opcion:
            case "1":
                gestionar_pizzas()
            case "2":
                gestionar_almacen()
            case "3":
                gestionar_ofertas()
            case "0":
                return
            case _:
                print("Opción no válida. Inténtalo de nuevo.")
