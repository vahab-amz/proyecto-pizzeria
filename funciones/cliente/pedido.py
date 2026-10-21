from listas import pizzas
from listas.bebidas import bebidas
from .carrito import carrito, mostrar_carrito

# Funciones para el menú del cliente
def pedir():
    while True:
        mostrar_carrito()
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
      
# Funciones para pedir productos   
def pedir_pizza():
    listar_pizzas()
    numero_pizza = input("Elige el número de la pizza que quieres añadir al carrito (o 0 para volver): ").strip()
    if numero_pizza == "0":
        return
    if numero_pizza.isdigit() and 1 <= int(numero_pizza) <= len(pizzas):
        pizza_seleccionada = list(pizzas.values())[int(numero_pizza) - 1]
        carrito.append({
            "tipo": "pizza",
            "nombre": pizza_seleccionada["nombre"],
            "precio": pizza_seleccionada["precio"],
        })
        print(f"Has añadido {pizza_seleccionada['nombre']} al carrito.")
    else:
        print("Opción no válida. Inténtalo de nuevo.")


# Funciones para pedir bebidas
def pedir_bebida():
    listar_bebidas()
    numero_bebida = input("Elige el número de la bebida que quieres añadir al carrito (o 0 para volver): ").strip()
    if numero_bebida == "0":
        return
    if numero_bebida.isdigit() and 1 <= int(numero_bebida) <= len(bebidas):
        nombre, precio = list(bebidas.items())[int(numero_bebida) - 1]
        carrito.append({
            "tipo": "bebida",
            "nombre": nombre,
            "precio": precio,
        })
        print(f"Has añadido {nombre} al carrito.")
    else:
        print("Opción no válida. Inténtalo de nuevo.")

# Funciones para listar pizzas
def listar_pizzas():
    print("\n--- LISTA DE PIZZAS ---")
    for i, pizza in enumerate(pizzas.values(), start=1):
        print(f"{i}. {pizza['nombre']} - {pizza['precio']:.2f} €")
    print("------------------------")

# Funciones para listar bebidas
def listar_bebidas():
    print("\n--- LISTA DE BEBIDAS ---")
    for i, (nombre, precio) in enumerate(bebidas.items(), start=1):
        print(f"{i}. {nombre} - {precio:.2f} €")
    print("------------------------")