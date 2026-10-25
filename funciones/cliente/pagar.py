from listas import negocio
from .carrito import carrito, calcular_total_carrito


# Muestra el ticket final. La base imponible llega como parámetro
# porque más adelante se aplicarán ofertas antes de llamar a esta función
def mostrar_ticket(base_imponible):
    importe_iva = base_imponible * negocio.iva
    total = base_imponible + importe_iva
    print("\n=========================")
    print("     PIZZERÍA PYTHON")
    print("=========================")
    print("Productos:")
    for item in carrito:
        print(f"- {item['tipo'].capitalize()} {item['nombre']}: {item['precio']:.2f} €")
    print("-------------------------")
    print(f"Base imponible: {base_imponible:.2f} €")
    print(f"IVA ({negocio.iva:.0%}): {importe_iva:.2f} €")
    print(f"Total: {total:.2f} €")
    print("=========================")
    print("Gracias por su compra.")


# Pide confirmación, muestra el ticket y vacía el carrito
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
    carrito.clear()
