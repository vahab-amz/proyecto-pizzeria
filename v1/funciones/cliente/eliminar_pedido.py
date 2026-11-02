from .carrito import carrito, mostrar_carrito


def eliminar_pedido():
    if len(carrito) == 0:
        print("\nTu carrito está vacío.")
        return
    mostrar_carrito()
    opcion = input("Número del producto a eliminar (V para vaciar el carrito, 0 para volver): ").strip()
    if opcion == "0":
        return
    if opcion.lower() == "v":
        carrito.clear()
        print("Has vaciado el carrito.")
    elif opcion.isdigit() and 1 <= int(opcion) <= len(carrito):
        quitar_unidades(int(opcion) - 1)
    else:
        print("Opción no válida. Inténtalo de nuevo.")


# Quita unidades de una línea; si se quitan todas, se elimina la línea
def quitar_unidades(posicion):
    producto = carrito[posicion]
    quitar = 1
    if producto["cantidad"] > 1:
        respuesta = input(f"Tienes {producto['cantidad']}. ¿Cuántas unidades quieres quitar? (0 para volver): ").strip()
        if respuesta == "0":
            return
        if not respuesta.isdigit():
            print("Cantidad no válida. Inténtalo de nuevo.")
            return
        quitar = int(respuesta)

    if quitar >= producto["cantidad"]:
        carrito.pop(posicion)
        print(f"Has eliminado {producto['nombre']} del carrito.")
    else:
        producto["cantidad"] -= quitar
        print(f"Has quitado {quitar} x {producto['nombre']}. Quedan {producto['cantidad']}.")
