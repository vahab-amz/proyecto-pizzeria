from listas import ingredientes
from .gestion_bebidas import gestionar_bebidas
from .gestion_ingredientes import gestionar_ingredientes

def gestionar_almacen():
    while True:
        print("\n--- GESTIÓN DE ALMACEN ---")
        print("1. Gestionar ingredientes")
        print("2. Gestionar Bebidas")
        print("0. Volver")

        opcion = input("Elige una opción: ").strip()

        match opcion:
            case "1":
                gestionar_ingredientes()
            case "2":
                gestionar_bebidas()

            case "0":
                return
            case _:
                print("Opción no válida. Inténtalo de nuevo.")
