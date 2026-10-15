from listas import bebidas

def añadir():
    while True:
        nombre = input("Dame el nombre de la nueva bebida: ").strip()

        if nombre in bebidas:
            print(f"La bebida {nombre} ya está registrado")
            continue
        else:
            break

    precio = float(input("Dame el precio por unidad: "))
    bebidas[nombre] = precio
    print(f"La bebida {nombre} se ha agregado correctamente")


    
def eliminar():
    while True:
            nombre = input("Nombre de la bebida a eliminar: ").strip()

            if nombre in bebidas:
                del bebidas[nombre] 
                break



def modificar():
    while True:
        nombre = input("Dame el nombre del ingrediente: ").strip()

        if nombre not in bebidas:
            print(f"El ingrediente {nombre} no está registrado")
            continue
        else:
            break

    precio = float(input("Dame el precio al kg: "))
    bebidas[nombre] = precio
    print(f"El ingrediente {nombre} se ha agregado correctamente")

def listar():
    for i in bebidas:
        print(f"{i} - {bebidas[i]:.2f} €/Kg")


def gestionar_bebidas():
    while True:
        print("\n--- bebidas ---")
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