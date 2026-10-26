from listas import ofertas

def añadir():
    while True:
        nombre = input("Dame el nombre de la oferta: ").strip()
        if nombre in ofertas:
            print("Nombre de la oferta registrada")
            continue
        else:
            precio = float(input("Cantidad a ingresar: "))
            ofertas[nombre] = precio
            print(f"La oferta {nombre} se ha registrado correctamente")
            break

        
def eliminar():
    while True:
        nombre = input("Dame el nombre de la oferta a eliminar: ").strip()
        if nombre not in ofertas:
            print(f"La oferta {nombre} no está registrada")
        else:
            del ofertas[nombre]
            break

def modificar():
    while True:
        nombre = input("Dame el nombre de la oferta: ").strip()
        if nombre not in ofertas:
            print("Nombre de la oferta no registrada")
            continue   
        else:
            precio = float(input("Dame la cantidad: "))
            ofertas[nombre] = precio
            break    

def listar():
    for oferta in ofertas:
        print(f"{oferta} - {ofertas[oferta]:.2f}")

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
