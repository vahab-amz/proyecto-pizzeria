def saludar():
    print("¡Bienvenido a la Pizzería!")
    print("¿Quién eres?")
    print("1. Trabajador")
    print("2. Cliente")

    while True:
        opcion = input("Elige una opción (1 o 2): ").strip()
        if opcion == "1":
            return "trabajador"
        if opcion == "2":
            return "cliente"
        print("Opción no válida. Inténtalo de nuevo.")
        
        