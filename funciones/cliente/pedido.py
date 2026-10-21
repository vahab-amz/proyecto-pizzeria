from listas import pizzas
from listas import negocio

# Se modifica con append/remove, nunca se reasigna (carrito = [...])
# Carrito del cliente: lista de diccionarios {"tipo", "nombre", "precio"}
carrito = []


def pedir():
    # TODO: mostrar pizzas, pedir nombre y añadirlo al carrito
    listar_pizzas()
    while True:
        numero_pedido = len(carrito) 
        if numero_pedido == 0:
            print("\nTu carrito está vacío.")
        else:
            print(f"\nTienes {numero_pedido} items en el carrito.")
            print("Carrito actual:")
            base_imponible = 0
            for i, item in enumerate(carrito, start=1):
                print(f"{i}. {item['nombre']} - {item['precio']:.2f} €")
                base_imponible += item['precio']
            print(f"Base imponible: {base_imponible:.2f} €")
            print(f"IVA ({negocio.iva:.0%}): {base_imponible * negocio.iva:.2f} €")
            print(f"Precio total: {base_imponible + base_imponible * negocio.iva:.2f} €")
        numero_pizza = input("Elige el número de la pizza que quieres añadir al carrito (o 0 para volver): ").strip()
        if numero_pizza == "0":
            break
        if numero_pizza.isdigit() and 1 <= int(numero_pizza) <= len(pizzas):
            pizza_seleccionada = list(pizzas.values())[int(numero_pizza) - 1]
            carrito.append({
                "tipo": "pizza",
                "nombre": pizza_seleccionada["nombre"],
                "precio": pizza_seleccionada["precio"],
            })
            print(f"Has añadido {pizza_seleccionada['nombre']} al carrito.")
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            
        
        


def listar_pedido():
    # TODO: mostrar productos del carrito con su precio
    print("Pendiente: ver pedido")


def modificar_pedido():
    # TODO: cambiar un producto del carrito por otro
    print("Pendiente: modificar pedido")


def eliminar_pedido():
    # TODO: quitar un producto del carrito o vaciarlo
    print("Pendiente: eliminar pedido")


def listar_pizzas():
    print("\n--- LISTA DE PIZZAS ---")
    for i, pizza in enumerate(pizzas.values(), start=1):
        print(f"{i}. {pizza['nombre']} - {pizza['precio']} €")
    print("------------------------")