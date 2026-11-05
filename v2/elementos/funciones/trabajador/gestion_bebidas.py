from objetos import Bebida
from elementos.bebidas import bebidas
from elementos.funciones.trabajador.entradas import pedir_nombre, pedir_numero


def buscar_bebida(nombre):
    for elemento in bebidas:
        if elemento.nombre == nombre:
            return elemento
    return None


def añadir():
    while True:
        nombre = pedir_nombre("Nombre del nuevo elemento: ")
        if buscar_bebida(nombre) is not None:
            print("El nombre ya está registrado")
            continue
        precio = pedir_numero("Precio por unidad: ")
        bebidas.append(Bebida(nombre, precio))
        print(f"{nombre} añadido correctamente")
        return


def eliminar():
    while True:
        nombre = pedir_nombre("Nombre del elemento a eliminar: ")
        elemento = buscar_bebida(nombre)
        if elemento is None:
            print("El nombre no está registrado")
            continue
        bebidas.remove(elemento)
        print(f"{nombre} eliminado correctamente")
        return


def modificar():
    while True:
        nombre = pedir_nombre("Nombre del elemento a modificar: ")
        elemento = buscar_bebida(nombre)
        if elemento is None:
            print("El nombre no está registrado")
            continue
        elemento.precio = pedir_numero("Precio por unidad: ")
        print(f"{nombre} modificado correctamente")
        return


def listar():
    for elemento in bebidas:
        print(f"{elemento.nombre} - {elemento.precio:.2f} €/unidad")


def gestionar_bebidas():
    while True:
        print("\n--- BEBIDAS ---")
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
