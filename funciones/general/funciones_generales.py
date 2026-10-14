from listas import pizzas, ingredientes, negocio

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
        
 

def calcular_pizza():
    iva = negocio.iva 
    margen_beneficio = negocio.margen_beneficio
    coste_gastos_por_pizza = (negocio.gastos_local + negocio.gastos_luz) / negocio.pizzas_vendidas_aprox
     
    for pizza in pizzas.values():
       coste_ingrediente = 0
       for ingrediente in pizza['ingredientes']:
           nombre = ingrediente['nombre']
           cantidad = ingrediente['cantidad']
           precio_kg = ingredientes[nombre]
           coste_ingrediente += precio_kg * cantidad

       coste_total = coste_ingrediente + coste_gastos_por_pizza
       pizza['precio'] = round(coste_total * (1 + margen_beneficio), 2)
    

        
           

         
