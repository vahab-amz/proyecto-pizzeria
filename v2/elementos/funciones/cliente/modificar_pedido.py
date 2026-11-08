from elementos.pizzas import pizzas
from elementos.bebidas import bebidas
from elementos.funciones.cliente.entradas import pedir_cantidad
from elementos.funciones.cliente.pedido import listar_pizzas, listar_bebidas
from elementos.carrito import carrito
from elementos.negocio import negocio


# Cambia el producto o la cantidad de una línea del carrito
def modificar_pedido():
    if carrito.esta_vacio():
        print("\nTu carrito está vacío.")
        return
    carrito.mostrar(negocio.iva)
    opcion = input("Número del producto que quieres cambiar (0 para volver): ").strip()
    if opcion == "0":
        return
    if not (opcion.isdigit() and 1 <= int(opcion) <= len(carrito.lineas)):
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
    producto = carrito.lineas[posicion]
    
    if producto.tipo == "pizza":
        listar_pizzas()
        numero = input("Elige la nueva pizza (0 para volver): ").strip()
        if numero == "0":
            return
        if not (numero.isdigit() and 1 <= int(numero) <= len(pizzas)):
            print("Opción no válida. Inténtalo de nuevo.")
            return
        pizzas_seleccionada = pizzas[int(numero) - 1]
        nombre = pizzas_seleccionada.nombre
        if nombre == producto.nombre:
            print("Es el mismo producto, no se ha cambiado nada.")
            return
        carrito.agregar("pizza", pizzas_seleccionada.nombre, pizzas_seleccionada.precio, producto.cantidad)
    else:
        listar_bebidas() 
        numero = input("Elige la nueva bebida (0 para volver): ").strip()
        if numero == "0":
            return
        if not (numero.isdigit() and 1 <= int(numero) <= len(bebidas)):
            print("Opción no válida. Inténtalo de nuevo.")
            return
        bebida_seleccionada = bebidas[int(numero) - 1]
        nombre = bebida_seleccionada.nombre
        if nombre == producto.nombre:
            print("Es el mismo producto, no se ha cambiado nada.")
            return
        carrito.agregar("bebida", bebida_seleccionada.nombre, bebida_seleccionada.precio, producto.cantidad)

    carrito.lineas.pop(posicion)
    print(f"Has cambiado {producto.nombre} por {nombre}.")
    
def cambiar_cantidad(posicion):
    producto = carrito.lineas[posicion]
    print(f"Ahora tienes {producto.cantidad} x {producto.nombre}.")
    cantidad = pedir_cantidad()
    if cantidad == 0:
        return
    producto.cantidad = cantidad
    print(f"Ahora tienes {cantidad} x {producto.nombre}.")