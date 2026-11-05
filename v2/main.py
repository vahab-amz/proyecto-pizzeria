from elementos.funciones.general.funciones_generales import saludar,temporada,calcular_pizza
from elementos.negocio import negocio
#from elementos.funciones.cliente import menu_cliente
from elementos.funciones.trabajador.menu import menu_trabajador
import os

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
                #menu_cliente()
                print("")
            case "trabajador":
                menu_trabajador()
            case "salir":
                print("¡Hasta pronto!")
                break


if __name__ == "__main__":
    os.system("cls")
    main()
    
