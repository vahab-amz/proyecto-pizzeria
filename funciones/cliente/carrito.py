from listas import negocio

# Carrito del cliente: lista de diccionarios {"tipo", "nombre", "precio", "cantidad"}
# "precio" es el de UNA unidad sin IVA
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
        subtotal = item['precio'] * item['cantidad']
        print(f"{i}. {item['nombre']} x{item['cantidad']} - {item['precio']:.2f} € c/u = {subtotal:.2f} €")
    base_imponible = calcular_total_carrito()
    print(".\n.\n.")
    print(f"Base imponible: {base_imponible:.2f} €")
    print(f"IVA ({negocio.iva:.0%}): {base_imponible * negocio.iva:.2f} €")
    print(f"Precio total: {base_imponible + base_imponible * negocio.iva:.2f} €")
    print("-------------------------")


def calcular_total_carrito():
    total = 0
    for item in carrito:
        total += item["precio"] * item["cantidad"]
    return total


# Pide una cantidad de 1 a 20. Devuelve 0 si el cliente cancela
def pedir_cantidad():
    while True:
        cantidad = input("¿Cuántas unidades quieres? (0 para cancelar): ").strip()
        if cantidad == "0":
            return 0
        if cantidad.isdigit() and 1 <= int(cantidad) <= 20:
            return int(cantidad)
        print("Cantidad no válida. Escribe un número del 1 al 20.")


# Devuelve la posición del producto en el carrito, o -1 si no está
def buscar_en_carrito(tipo, nombre):
    for i, item in enumerate(carrito):
        if item["tipo"] == tipo and item["nombre"] == nombre:
            return i
    return -1


# Si el producto ya está en el carrito suma la cantidad; si no, añade una línea nueva
def anadir_al_carrito(tipo, nombre, precio, cantidad):
    posicion = buscar_en_carrito(tipo, nombre)
    if posicion != -1:
        carrito[posicion]["cantidad"] += cantidad
    else:
        carrito.append({
            "tipo": tipo,
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad,
        })
