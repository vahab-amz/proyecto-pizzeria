from listas import negocio

# Carrito del cliente: lista de diccionarios {"tipo", "nombre", "precio"}
# Se modifica con append/pop, nunca se reasigna (carrito = [...])
carrito = []


def mostrar_carrito():
    numero_pedido = len(carrito)
    if numero_pedido == 0:
        print("\nTu carrito está vacío.")
        return
    print(f"\nTienes {numero_pedido} items en el carrito.")
    print("Carrito actual:")
    for i, item in enumerate(carrito, start=1):
        print(f"{i}. {item['nombre']} - {item['precio']:.2f} €")
    base_imponible = calcular_total_carrito()
    print(".\n.\n.")
    print(f"Base imponible: {base_imponible:.2f} €")
    print(f"IVA ({negocio.iva:.0%}): {base_imponible * negocio.iva:.2f} €")
    print(f"Precio total: {base_imponible + base_imponible * negocio.iva:.2f} €")
    print("-------------------------")
    
    
def calcular_total_carrito():
    total = 0
    for item in carrito:
        total += item["precio"]
    return total