import os
from datetime import datetime
from listas import negocio
from .carrito import carrito, calcular_total_carrito


# Construye el ticket como una lista de líneas (strings).
# La base imponible llega como parámetro porque más adelante
# se aplicarán ofertas antes de llamar a esta función
def crear_lineas_ticket(base_imponible):
    importe_iva = base_imponible * negocio.iva
    total = base_imponible + importe_iva
    lineas = [
        "=========================",
        "     PIZZERÍA PYTHON",
        "=========================",
        "Productos:",
    ]
    for item in carrito:
        subtotal = item['precio'] * item['cantidad']
        lineas.append(f"- {item['cantidad']} x {item['tipo'].capitalize()} {item['nombre']}: {subtotal:.2f} €")
    lineas.append("-------------------------")
    lineas.append(f"Base imponible: {base_imponible:.2f} €")
    lineas.append(f"IVA ({negocio.iva:.0%}): {importe_iva:.2f} €")
    lineas.append(f"Total: {total:.2f} €")
    lineas.append("=========================")
    lineas.append("Gracias por su compra.")
    return lineas


# Muestra el ticket en la terminal
def mostrar_ticket(base_imponible):
    print()
    for linea in crear_lineas_ticket(base_imponible):
        print(linea)


# Guarda las líneas del ticket en tickets/ticket_AAAAMMDD_HHMMSS.txt
def guardar_ticket(lineas):
    os.makedirs("tickets", exist_ok=True)
    fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
    ruta = f"tickets/ticket_{fecha}.txt"
    with open(ruta, "w", encoding="utf-8") as archivo:
        for linea in lineas:
            archivo.write(linea + "\n")
    print(f"Ticket guardado en: {ruta}")


# Pide confirmación, muestra y guarda el ticket y vacía el carrito
def pagar():
    if len(carrito) == 0:
        print("\nTu carrito está vacío.")
        return
    base_imponible = calcular_total_carrito()
    total = base_imponible + base_imponible * negocio.iva
    print(f"\nTotal a pagar (IVA incluido): {total:.2f} €")
    confirmacion = input("¿Confirmar el pago? (s/n): ").strip().lower()
    if confirmacion != "s":
        print("Pago cancelado.")
        return
    mostrar_ticket(base_imponible)
    guardar_ticket(crear_lineas_ticket(base_imponible))
    carrito.clear()
