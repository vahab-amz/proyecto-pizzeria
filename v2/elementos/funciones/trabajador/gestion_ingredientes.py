# En el catálogo, Ingrediente.cantidad representa el precio por kg.
from objetos import Ingrediente
from elementos.ingredientes import ingredientes
from elementos.pizzas import pizzas
from elementos.funciones.trabajador.entradas import pedir_nombre, pedir_numero


def buscar_ingrediente(nombre):
    for elemento in ingredientes:
        if elemento.nombre == nombre:
            return elemento
    return None


def añadir():
    while True:
        nombre = pedir_nombre("Nombre del nuevo elemento: ")
        if buscar_ingrediente(nombre) is not None:
            print("El nombre ya está registrado")
            continue
        precio = pedir_numero("Precio por kg: ")
        ingredientes.append(Ingrediente(nombre, precio))
        print(f"{nombre} añadido correctamente")
        return


def eliminar():
    while True:
        nombre = pedir_nombre("Nombre del elemento a eliminar: ")
        elemento = buscar_ingrediente(nombre)
        if elemento is None:
            print("El nombre no está registrado")
            continue
        if any(
            item.nombre == nombre
            for pizza in pizzas
            for item in pizza.ingredientes
        ):
            print(f"El ingrediente {nombre} se usa en una pizza")
            continue
        ingredientes.remove(elemento)
        print(f"{nombre} eliminado correctamente")
        return


def modificar():
    while True:
        nombre = pedir_nombre("Nombre del elemento a modificar: ")
        elemento = buscar_ingrediente(nombre)
        if elemento is None:
            print("El nombre no está registrado")
            continue
        elemento.cantidad = pedir_numero("Precio por kg: ")
        print(f"{nombre} modificado correctamente")
        return


def listar():
    for elemento in ingredientes:
        print(f"{elemento.nombre} - {elemento.cantidad:.2f} €/kg")


def gestionar_ingredientes():
    while True:
        print("\n--- INGREDIENTES ---")
        print("1. Añadir")
        print("2. Eliminar")
        print("3. Modificar")
        print("4. Listar")
        print("0. Salir")

        opcion = input("Elige una opción: ").strip()

        match opcion:
            case "1":
                añadir()
            case "2":
                eliminar()
            case "3":
                modificar()
            case "4":
                listar()
            case "0":
                return
            case _:
                print("Opción no válida. Inténtalo de nuevo.")
