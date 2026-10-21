from listas import pizzas
from listas.bebidas import bebidas
from .carrito import carrito, mostrar_carrito
from .pedido import listar_pizzas, listar_bebidas


def modificar_pedido():
    if len(carrito) == 0:
        print("\nTu carrito está vacío.")
        return
    mostrar_carrito()
    opcion = input("Número del producto que quieres cambiar (0 para volver): ").strip()
    if opcion == "0":
        return
    if not (opcion.isdigit() and 1 <= int(opcion) <= len(carrito)):
        print("Opción no válida. Inténtalo de nuevo.")
        return

    posicion = int(opcion) - 1
    producto = carrito[posicion]

    if producto["tipo"] == "pizza":
        listar_pizzas()
        numero = input("Elige la nueva pizza (0 para volver): ").strip()
        if numero == "0":
            return
        if numero.isdigit() and 1 <= int(numero) <= len(pizzas):
            nueva = list(pizzas.values())[int(numero) - 1]
            carrito[posicion] = {
                "tipo": "pizza",
                "nombre": nueva["nombre"],
                "precio": nueva["precio"],
            }
            print(f"Has cambiado {producto['nombre']} por {nueva['nombre']}.")
        else:
            print("Opción no válida. Inténtalo de nuevo.")
    else:
        listar_bebidas()
        numero = input("Elige la nueva bebida (0 para volver): ").strip()
        if numero == "0":
            return
        if numero.isdigit() and 1 <= int(numero) <= len(bebidas):
            nombre, precio = list(bebidas.items())[int(numero) - 1]
            carrito[posicion] = {
                "tipo": "bebida",
                "nombre": nombre,
                "precio": precio,
            }
            print(f"Has cambiado {producto['nombre']} por {nombre}.")
        else:
            print("Opción no válida. Inténtalo de nuevo.")