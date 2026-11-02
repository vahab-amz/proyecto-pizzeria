from listas import pizzas
from listas.bebidas import bebidas
from .carrito import carrito, mostrar_carrito, pedir_cantidad, buscar_en_carrito
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
    print("1. Cambiar producto")
    print("2. Cambiar cantidad")
    print("0. Volver")
    accion = input("Elige una opción: ").strip()
    match accion:
        case "1":
            cambiar_producto(posicion)
        case "2":
            cambiar_cantidad(posicion)
        case "0":
            return
        case _:
            print("Opción no válida. Inténtalo de nuevo.")


# Cambia el producto de una línea manteniendo su cantidad
def cambiar_producto(posicion):
    producto = carrito[posicion]

    if producto["tipo"] == "pizza":
        listar_pizzas()
        numero = input("Elige la nueva pizza (0 para volver): ").strip()
        if numero == "0":
            return
        if not (numero.isdigit() and 1 <= int(numero) <= len(pizzas)):
            print("Opción no válida. Inténtalo de nuevo.")
            return
        nueva = list(pizzas.values())[int(numero) - 1]
        nombre = nueva["nombre"]
        precio = nueva["precio"]
    else:
        listar_bebidas()
        numero = input("Elige la nueva bebida (0 para volver): ").strip()
        if numero == "0":
            return
        if not (numero.isdigit() and 1 <= int(numero) <= len(bebidas)):
            print("Opción no válida. Inténtalo de nuevo.")
            return
        nombre, precio = list(bebidas.items())[int(numero) - 1]

    # Si el producto nuevo ya está en otra línea, se juntan las cantidades
    existente = buscar_en_carrito(producto["tipo"], nombre)
    if existente != -1 and existente != posicion:
        carrito[existente]["cantidad"] += producto["cantidad"]
        carrito.pop(posicion)
    else:
        carrito[posicion] = {
            "tipo": producto["tipo"],
            "nombre": nombre,
            "precio": precio,
            "cantidad": producto["cantidad"],
        }
    print(f"Has cambiado {producto['nombre']} por {nombre}.")


# Cambia la cantidad de una línea
def cambiar_cantidad(posicion):
    producto = carrito[posicion]
    print(f"Ahora tienes {producto['cantidad']} x {producto['nombre']}.")
    cantidad = pedir_cantidad()
    if cantidad == 0:
        return
    producto["cantidad"] = cantidad
    print(f"Ahora tienes {cantidad} x {producto['nombre']}.")
