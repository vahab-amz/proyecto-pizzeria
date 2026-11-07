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
        
class LineaCarrito:
    def __init__(self, tipo, nombre, precio, cantidad):
        self.tipo = tipo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def subtotal(self):
        return self.precio * self.cantidad
    
    def __str__(self):
        return f"{self.nombre} x{self.cantidad} - {self.precio:.2f} € c/u = {self.subtotal():.2f} €"
        
class Carrito:
    def __init__(self):
        self.lineas = []
        
    def esta_vacio(self):
        return len(self.lineas) == 0
        
    def buscar(self, tipo, nombre):
        for item in self.lineas:
            if item.tipo == tipo and item.nombre == nombre:
                return item
        return None
        
    def agregar(self, tipo, nombre, precio, cantidad):
        item_existe = self.buscar(tipo, nombre)
        if item_existe is not None:
            item_existe.cantidad += cantidad
        else:
            new_item = LineaCarrito(tipo, nombre, precio, cantidad)
            self.lineas.append(new_item)

    def quitar(self, posicion, cantidad):
        item = self.lineas[posicion]
        item.cantidad -= cantidad
        if item.cantidad <= 0:
            self.lineas.pop(posicion)
        return item

    def subtotal(self):
        total = 0
        for item in self.lineas:
            total += item.subtotal()
        return total

    def vaciar(self):
        self.lineas.clear()
        
    def mostrar(self, iva):
        if self.esta_vacio():
            print("\nTu carrito está vacío.")
            return
        print(f"\nTienes {len(self.lineas)} items en el carrito.")
        print("Carrito actual:")
        for i, item in enumerate(self.lineas, start=1):
            print(f"{i}. {item}")
        base_imponible = self.subtotal()
        print(f"Base imponible: {base_imponible:.2f} €")
        print(f"IVA ({iva:.0%}): {base_imponible * iva:.2f} €")
        print(f"Precio total: {base_imponible + base_imponible * iva:.2f} €")
        print("-------------------------")
        
