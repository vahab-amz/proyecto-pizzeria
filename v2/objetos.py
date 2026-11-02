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

class Ofertas:
    def __init__(self,nombre,descuento):
        self.nombre = nombre
        self.descuento = descuento

