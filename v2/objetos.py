class Ingrediente:
    def __init__(self,nombre,cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

class Pizza:
    def __init__(self,nombre,precio,descripcion,tamano,tipo_masa,ingredientes):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.tamano = tamano
        self.tipo_masa = tipo_masa
        self.ingredientes = ingredientes

    def agregar_ingrediente(self,ingrediente):
        self.ingredientes.append(ingrediente)

class Bebida:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio

class Oferta:
    def __init__(self,nombre,descuento):
        self.nombre = nombre
        self.descuento = descuento

class Negocio:
    def __init__(self,iva,margen_beneficio,gastos_local,gastos_luz,pizzas_vendidas_aprox,gasto_personal_mensual): 
        self.iva = iva 
        self.margen_beneficio = margen_beneficio 
        self.gastos_local = gastos_local 
        self.gastos_luz = gastos_luz 
        self.pizzas_vendidas_aprox = pizzas_vendidas_aprox 
        self.gasto_personal_mensual = gasto_personal_mensual