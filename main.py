from funciones.general import saludar, calcular_pizza
from funciones.cliente import menu_cliente
from funciones.trabajador import menu_trabajador


def main():
    calcular_pizza()
    rol = saludar()
    match rol:
        case "cliente":
            menu_cliente()
        case "trabajador":
            menu_trabajador()


if __name__ == "__main__":
    main()
