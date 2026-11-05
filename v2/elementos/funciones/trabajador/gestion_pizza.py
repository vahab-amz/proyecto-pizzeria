from objetos import Pizza, Ingrediente
from elementos.pizzas import pizzas
from elementos.ingredientes import ingredientes
from elementos.funciones.general.funciones_generales import calcular_pizza
from elementos.funciones.trabajador.entradas import pedir_nombre, pedir_numero


def buscar_pizza(nombre):
    for pizza in pizzas:
        if pizza.nombre == nombre:
            return pizza
    return None


def pedir_receta():
    receta = []
    while True:
        nombre = pedir_nombre("Ingrediente (Salir para terminar): ")
        if nombre.lower() == "salir":
            return receta
        if not any(ingrediente.nombre == nombre for ingrediente in ingredientes):
            print(f"El producto {nombre} no se encuentra en el almacén")
            continue
        cantidad = pedir_numero("Cantidad en kg: ")
        # Un objeto nuevo guarda los kilos de la receta, sin cambiar el catálogo.
        receta.append(Ingrediente(nombre, cantidad))


def crear_pizza():
    while True:
        nombre = pedir_nombre("Nombre: ")
        if buscar_pizza(nombre) is None:
            break
        print("Pizza ya registrada")

    descripcion = input("Descripción: ").strip()
    tamano = input("Tamaño: ").strip()
    tipo_masa = input("Masa: ").strip()
    receta = pedir_receta()
    pizzas.append(Pizza(nombre, None, descripcion, tamano, tipo_masa, receta))
    print(f"Pizza {nombre} añadida correctamente.")


def modificar_pizza():
    while True:
        nombre = pedir_nombre("Nombre de la pizza a modificar: ")
        pizza = buscar_pizza(nombre)
        if pizza is not None:
            break
        print(f"La pizza {nombre} no se encuentra en la carta")

    descripcion = input("Descripción: ").strip()
    tamano = input("Tamaño: ").strip()
    tipo_masa = input("Masa: ").strip()
    receta = pedir_receta()
    pizza.descripcion = descripcion
    pizza.tamano = tamano
    pizza.tipo_masa = tipo_masa
    pizza.ingredientes = receta
    pizza.precio = None
    print(f"Pizza {nombre} modificada correctamente.")


def eliminar_pizza():
    while True:
        nombre = pedir_nombre("Nombre de la pizza a eliminar: ")
        pizza = buscar_pizza(nombre)
        if pizza is None:
            print(f"La pizza {nombre} no se encuentra en la carta")
            continue
        pizzas.remove(pizza)
        print(f"Pizza {nombre} eliminada correctamente.")
        return


def listar_pizzas():
    calcular_pizza()
    for pizza in pizzas:
        print(f"{pizza.nombre} - {pizza.precio:.2f} €")


def gestionar_pizzas():
    while True:
        print("\n--- GESTIÓN DE PIZZAS ---")
        print("1. Crear pizza")
        print("2. Modificar pizza")
        print("3. Eliminar pizza")
        print("4. Listar pizzas")
        print("0. Volver")

        opcion = input("Elige una opción: ").strip()

        match opcion:
            case "1":
                crear_pizza()
            case "2":
                modificar_pizza()
            case "3":
                eliminar_pizza()
            case "4":
                listar_pizzas()
            case "0":
                return
            case _:
                print("Opción no válida. Inténtalo de nuevo.")
