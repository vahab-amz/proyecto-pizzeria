from elementos.pizzas import pizzas
from elementos.ingredientes import ingredientes
from elementos.negocio import negocio

def saludar():
    print("\n¿Quién eres?")
    print("1. Trabajador")
    print("2. Cliente")
    print("0. Salir")

    while True:
        opcion = input("Elige una opción (1, 2 o 0): ").strip()
        if opcion == "1":
            return "trabajador"
        if opcion == "2":
            return "cliente"
        if opcion == "0":
            return "salir"
        print("Opción no válida. Inténtalo de nuevo.")
        
def temporada():
    print("Temporada") 
    print("1. Baja") 
    print("2. Media") 
    print("3. Alta") 
    
    while True:
        opc = int(input("Selecciona la temporada de pedidos que nos encontramos: "))
        if opc == 1:
            return "baja"
        if opc == 2:
            return "media"
        if opc == 3:
            return "alta"
        print("Opción no válida. Inténtalo de nuevo.")

def calcular_pizza():


    margen_beneficio = negocio.margen_beneficio

    coste_gastos_por_pizza = (negocio.gastos_local+ negocio.gastos_luz + negocio.gasto_personal_mensual) / negocio.pizzas_vendidas_aprox

    precios_por_nombre = {
        ingrediente.nombre: ingrediente.cantidad
        for ingrediente in ingredientes
    }

    for pizza in pizzas:
        coste_ingredientes = 0

        for ingrediente in pizza.ingredientes:
            precio_kg = precios_por_nombre[ingrediente.nombre]
            coste_ingredientes += precio_kg * ingrediente.cantidad

        coste_total = coste_ingredientes + coste_gastos_por_pizza
        pizza.precio = round(coste_total * (1 + margen_beneficio), 2)