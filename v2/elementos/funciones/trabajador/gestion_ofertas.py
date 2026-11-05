from objetos import Oferta
from elementos.ofertas import ofertas


def buscar_oferta(nombre):
    # La lista contiene objetos: comparamos su atributo nombre.
    return next((oferta for oferta in ofertas if oferta.nombre == nombre), None)


def pedir_descuento():
    # Se guarda el factor del precio: 0.9 significa pagar el 90% (10% menos).
    while True:
        try:
            descuento = float(input("Factor del precio entre 0 y 1 (0.9 = 10% de descuento): "))
        except ValueError:
            print("Introduce un número válido.")
            continue
        if 0 <= descuento <= 1:
            return descuento
        print("El factor debe estar entre 0 y 1.")


def añadir():
    while True:
        nombre = input("Dame el nombre de la oferta: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            continue
        if buscar_oferta(nombre) is not None:
            print("Nombre de la oferta registrada")
            continue
        ofertas.append(Oferta(nombre, pedir_descuento()))
        print(f"La oferta {nombre} se ha registrado correctamente")
        return


def eliminar():
    while True:
        nombre = input("Dame el nombre de la oferta a eliminar: ").strip()
        oferta = buscar_oferta(nombre)
        if oferta is None:
            print(f"La oferta {nombre} no está registrada")
            continue
        ofertas.remove(oferta)
        return


def modificar():
    while True:
        nombre = input("Dame el nombre de la oferta: ").strip()
        oferta = buscar_oferta(nombre)
        if oferta is None:
            print("Nombre de la oferta no registrada")
            continue
        oferta.descuento = pedir_descuento()
        return


def listar():
    for oferta in ofertas:
        print(f"{oferta.nombre} - factor de precio: {oferta.descuento:.2f}")


def gestionar_ofertas():
    while True:
        print("\n--- OFERTAS ---")
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
