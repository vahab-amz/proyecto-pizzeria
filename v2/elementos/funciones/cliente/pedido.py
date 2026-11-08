from elementos.pizzas import pizzas
from elementos.bebidas import bebidas
from elementos.funciones.cliente.entradas import pedir_cantidad
from elementos.carrito import carrito
from elementos.negocio import negocio

# Menú para añadir productos al carrito
def pedir():
    while True:
        carrito.mostrar(negocio.iva)
        print("\n¿Qué quieres añadir?")
        print("1. Pizza")
        print("2. Bebida")
        print("0. Volver")
        opcion = input("Elige una opción: ").strip()
        match opcion:
            case "1":
                pedir_pizza()
            case "2":
                pedir_bebida()
            case "0":
                break
            case _:
                print("Opción no válida. Inténtalo de nuevo.")


# Muestra las pizzas numeradas con su precio
def listar_pizzas():
    print("\n--- LISTA DE PIZZAS ---")
    for i, pizza in enumerate(pizzas, start=1):
        print(f"{i}. {pizza.nombre} - {pizza.precio:.2f} €")
    print("------------------------")

# Muestra las bebidas numeradas con su precio
def listar_bebidas():
    print("\n--- LISTA DE BEBIDAS ---")
    for i, bebida in enumerate(bebidas, start=1):
        print(f"{i}. {bebida.nombre} - {bebida.precio:.2f} €")
    print("------------------------")


# Elige una pizza, pide la cantidad y la añade al carrito
def pedir_pizza():
    listar_pizzas()
    numero_pizza = input("Elige el número de la pizza que quieres añadir al carrito (o 0 para volver): ").strip()
    if numero_pizza == "0":
        return
    if numero_pizza.isdigit() and 1 <= int(numero_pizza) <= len(pizzas):
        pizza_seleccionada = pizzas[int(numero_pizza) - 1]
        cantidad = pedir_cantidad()
        if cantidad == 0:
            return
        carrito.agregar("pizza", pizza_seleccionada.nombre, pizza_seleccionada.precio, cantidad)
        print(f"Has añadido {cantidad} x {pizza_seleccionada.nombre} al carrito.")
    else:
        print("Opción no válida. Inténtalo de nuevo.")

# Elige una bebida, pide la cantidad y la añade al carrito
def pedir_bebida():
        listar_bebidas()
        numero_bebida = input("Elige el número de la bebida que quieres añadir al carrito (o 0 para volver): ").strip()
        if numero_bebida == "0":
            return
        if numero_bebida.isdigit() and 1 <= int(numero_bebida) <= len(bebidas):
            bebida_seleccionada = bebidas[int(numero_bebida) - 1]
            cantidad = pedir_cantidad()
            if cantidad == 0:
                return
            carrito.agregar("bebida", bebida_seleccionada.nombre, bebida_seleccionada.precio, cantidad)
            print(f"Has añadido {cantidad} x {bebida_seleccionada.nombre} al carrito.")
        else:
            print("Opción no válida. Inténtalo de nuevo.")
