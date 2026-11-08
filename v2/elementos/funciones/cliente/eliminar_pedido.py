from elementos.carrito import carrito
from elementos.negocio import negocio


# Quita unidades de un producto o vacía el carrito
def eliminar_pedido():
    if carrito.esta_vacio():
        print("\nTu carrito está vacío.")
        return

    carrito.mostrar(negocio.iva)
    opcion = input("Número del producto a eliminar (V para vaciar el carrito, 0 para volver): ").strip()

    if opcion == "0":
        return

    if opcion.lower() == "v":
        carrito.vaciar()
        print("Has vaciado el carrito.")
        return

    if not (opcion.isdigit() and 1 <= int(opcion) <= len(carrito.lineas)):
        print("Opción no válida. Inténtalo de nuevo.")
        return

    posicion = int(opcion) - 1
    linea = carrito.lineas[posicion]

    cantidad = 1
    if linea.cantidad > 1:
        texto = input(f"¿Cuántas unidades de {linea.nombre} quieres quitar? (1-{linea.cantidad}): ").strip()
        if not (texto.isdigit() and 1 <= int(texto) <= linea.cantidad):
            print("Cantidad no válida.")
            return
        cantidad = int(texto)

    linea = carrito.quitar(posicion, cantidad)
    print(f"Has quitado {cantidad} x {linea.nombre} del carrito.")