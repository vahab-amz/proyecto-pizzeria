from .pedido import pedir
from .listar_pedido import listar_pedido
from .modificar_pedido import modificar_pedido
from .eliminar_pedido import eliminar_pedido
from .pagar import pagar


def menu_cliente():
    while True:
        print("\n--- MENÚ CLIENTE ---")
        print("1. Hacer pedido")
        print("2. Ver pedido")
        print("3. Modificar pedido")
        print("4. Eliminar pedido")
        print("5. Pagar / Finalizar pedido")
        print("0. Volver")

        opcion = input("Elige una opción: ").strip()
        match opcion:
            case "1":
                pedir()
            case "2":
                listar_pedido()
            case "3":
                modificar_pedido()
            case "4":
                eliminar_pedido()
            case "5":
                pagar()
            case "0":
                return
            case _:
                print("Opción no válida. Inténtalo de nuevo.")
