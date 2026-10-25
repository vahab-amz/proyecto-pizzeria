from funciones.general import saludar, calcular_pizza, temporada
from funciones.cliente import menu_cliente
from funciones.trabajador import menu_trabajador
from listas import negocio, pizzas

def main():
    print("¡Bienvenido a la Pizzería!")

    temp = temporada()
    match temp:
        case "baja":
            t = 600
        case "media":
            t = 1000
        case "alta":
            t = 1500
    negocio.pizzas_vendidas_aprox = t

    # Se recalculan los precios en cada vuelta para ver los cambios del trabajador
    while True:
        calcular_pizza()

        rol = saludar()
        match rol:
            case "cliente":
                menu_cliente()
            case "trabajador":
                menu_trabajador()
            case "salir":
                print("¡Hasta pronto!")
                break


if __name__ == "__main__":
    main()
