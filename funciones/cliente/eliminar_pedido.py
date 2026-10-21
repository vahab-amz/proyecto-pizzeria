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
        producto = carrito.pop(int(opcion) - 1)
        print(f"Has eliminado {producto['nombre']} del carrito.")
    else:
        print("Opción no válida. Inténtalo de nuevo.")