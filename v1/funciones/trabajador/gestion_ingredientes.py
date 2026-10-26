from listas import ingredientes
from listas import pizzas

def añadir():
    while True:
        nombre = input("Dame el nombre del nuevo ingrediente: ").strip()

        if nombre in ingredientes:
            print(f"El ingrediente {nombre} ya está registrado")
            continue
        else:
            break

    precio = float(input("Dame el precio al kg: "))
    ingredientes[nombre] = precio
    print(f"El ingrediente {nombre} se ha agregado correctamente")


    
def eliminar():
    while True:
            nombre = input("Nombre de la pizza a eliminar: ").strip()
            eliminar = False
            for pizza in pizzas.values():
                for ingrediente in pizza['ingredientes']:
                    if ingrediente['nombre'] == nombre:
                        eliminar = True

            if nombre in ingredientes and  not eliminar:
                del ingredientes[nombre] 
                break
            elif eliminar == True :
                print(f"El ingrediente {nombre} se usa en una pizza")
            else:
                print(f"El ingrediente {nombre} no se encuentra en el almacen")
                continue


def modificar():
    while True:
        nombre = input("Dame el nombre del ingrediente: ").strip()

        if nombre not in ingredientes:
            print(f"El ingrediente {nombre} no está registrado")
            continue
        else:
            break

    precio = float(input("Dame el precio al kg: "))
    ingredientes[nombre] = precio
    print(f"El ingrediente {nombre} se ha agregado correctamente")

def listar():
    for i in ingredientes:
        print(f"{i} - {ingredientes[i]:.2f} €/Kg")

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