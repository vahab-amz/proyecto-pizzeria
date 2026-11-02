from listas import pizzas, ingredientes
from funciones.general import calcular_pizza

def crear_pizza():
    while True:
        nombre = input("Nombre: ").strip()

        if nombre in pizzas:
            print("Pizza ya registrada")
        else:
            break

    descripcion = input("Descripción: ").strip()
    tamanyo = input("Tamaño: ").strip()
    tipo_masa = input("Masa: ").strip()

    ingre = []

    while True:
        item = input("Dame el ingrediente (Salir para terminar): ").strip()

        if item.lower() == "salir":
            break

        if item not in ingredientes:
            print(f"El producto {item} no se encuentra en el almacén")
            continue

        cantidad = float(input("Ingresa la cantidad en KG: "))

        ingre.append({"nombre": item, "cantidad": cantidad})

    pizzas[nombre] = {
    "nombre": nombre,
    "precio": None,
    "descripcion": descripcion,
    "tamano": tamanyo,
    "tipo_de_masa": tipo_masa,
    "ingredientes": ingre
}

    print(f"Pizza {nombre} añadida correctamente.")


def modificar_pizza():
    while True:
        nombre = input("Nombre de la pizza a modificar: ").strip()

        if nombre not in pizzas:
            print(f"La pizza {nombre} no se encuentra en la carta")
            continue
        else:
            break
    
    descripcion = input("Descripción: ").strip()
    tamanyo = input("Tamaño: ").strip()
    tipo_masa = input("Masa: ").strip()

    ingre = []

    while True:
        item = input("Dame el ingrediente (Salir para terminar): ").strip()

        if item.lower() == "salir":
            break

        if item not in ingredientes:
            print(f"El producto {item} no se encuentra en el almacén")
            continue

        cantidad = float(input("Ingresa la cantidad en KG: "))

        ingre.append({"nombre": item, "cantidad": cantidad})

    pizzas[nombre] = {
    "nombre": nombre,
    "precio": None,
    "descripcion": descripcion,
    "tamano": tamanyo,
    "tipo_de_masa": tipo_masa,
    "ingredientes": ingre
}

    print(f"Pizza {nombre} modificada correctamente.")   

def eliminar_pizza():
    while True:
            nombre = input("Nombre de la pizza a eliminar: ").strip()

            if nombre in pizzas:
                del pizzas[nombre] 
                break
            else:
                print(f"La pizza {nombre} no se encuentra en la carta")
                continue


def listar_pizzas():
    calcular_pizza()
    for pizza in pizzas.values():
        print(f"{pizza['nombre']} - {pizza['precio']}")

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
