
# "cantidad" = kg de ingrediente que se usan en una pizza
# "precio" se calcula con calcular_precio_pizza(), no se escribe a mano
pizzas = {
    "Margarita": {
        "nombre": "Margarita",
        "precio": None,
        "descripcion": "La clásica: tomate y queso.",
        "tamano": "mediana",
        "tipo_de_masa": "clasica",
        "ingredientes": [
            {"nombre": "harina", "cantidad": 0.25},
            {"nombre": "tomate", "cantidad": 0.10},
            {"nombre": "queso", "cantidad": 0.12}
        ]
    },
    "Prosciutto": {
        "nombre": "Prosciutto",
        "precio": None,
        "descripcion": "Tomate, queso y jamón.",
        "tamano": "mediana",
        "tipo_de_masa": "clasica",
        "ingredientes": [
            {"nombre": "harina", "cantidad": 0.25},
            {"nombre": "tomate", "cantidad": 0.10},
            {"nombre": "queso", "cantidad": 0.12},
            {"nombre": "jamon", "cantidad": 0.08}
        ]
    },
    "Barbacoa": {
        "nombre": "Barbacoa",
        "precio": None,
        "descripcion": "Tomate, queso, bacon y pollo.",
        "tamano": "mediana",
        "tipo_de_masa": "clasica",
        "ingredientes": [
            {"nombre": "harina", "cantidad": 0.25},
            {"nombre": "tomate", "cantidad": 0.10},
            {"nombre": "queso", "cantidad": 0.12},
            {"nombre": "bacon", "cantidad": 0.07},
            {"nombre": "pollo", "cantidad": 0.10}
        ]
    },
    "Pepperoni": {
        "nombre": "Pepperoni",
        "precio": None,
        "descripcion": "Tomate, mozzarella y pepperoni.",
        "tamano": "mediana",
        "tipo_de_masa": "fina",
        "ingredientes": [
            {"nombre": "harina", "cantidad": 0.20},
            {"nombre": "tomate", "cantidad": 0.10},
            {"nombre": "mozzarella", "cantidad": 0.15},
            {"nombre": "pepperoni", "cantidad": 0.07}
        ]
    },
    "Dos Quesos": {
        "nombre": "Dos Quesos",
        "precio": None,
        "descripcion": "Tomate, queso y mozzarella.",
        "tamano": "mediana",
        "tipo_de_masa": "fina",
        "ingredientes": [
            {"nombre": "harina", "cantidad": 0.20},
            {"nombre": "tomate", "cantidad": 0.10},
            {"nombre": "queso", "cantidad": 0.12},
            {"nombre": "mozzarella", "cantidad": 0.15}
        ]
    },
    "Atún": {
        "nombre": "Atún",
        "precio": None,
        "descripcion": "Tomate, queso, atún y cebolla.",
        "tamano": "mediana",
        "tipo_de_masa": "clasica",
        "ingredientes": [
            {"nombre": "harina", "cantidad": 0.25},
            {"nombre": "tomate", "cantidad": 0.10},
            {"nombre": "queso", "cantidad": 0.12},
            {"nombre": "atun", "cantidad": 0.08},
            {"nombre": "cebolla", "cantidad": 0.06}
        ]
    },
    "Funghi": {
        "nombre": "Funghi",
        "precio": None,
        "descripcion": "Tomate, queso y champiñones.",
        "tamano": "mediana",
        "tipo_de_masa": "fina",
        "ingredientes": [
            {"nombre": "harina", "cantidad": 0.20},
            {"nombre": "tomate", "cantidad": 0.10},
            {"nombre": "queso", "cantidad": 0.12},
            {"nombre": "champinones", "cantidad": 0.08}
        ]
    },
    "Vegetal": {
        "nombre": "Vegetal",
        "precio": None,
        "descripcion": "Tomate, queso, champiñones, cebolla y aceitunas.",
        "tamano": "mediana",
        "tipo_de_masa": "fina",
        "ingredientes": [
            {"nombre": "harina", "cantidad": 0.20},
            {"nombre": "tomate", "cantidad": 0.10},
            {"nombre": "queso", "cantidad": 0.12},
            {"nombre": "champinones", "cantidad": 0.08},
            {"nombre": "cebolla", "cantidad": 0.06},
            {"nombre": "aceitunas", "cantidad": 0.04}
        ]
    },
    "Pollo": {
        "nombre": "Pollo",
        "precio": None,
        "descripcion": "Tomate, mozzarella, pollo y cebolla.",
        "tamano": "mediana",
        "tipo_de_masa": "clasica",
        "ingredientes": [
            {"nombre": "harina", "cantidad": 0.25},
            {"nombre": "tomate", "cantidad": 0.10},
            {"nombre": "mozzarella", "cantidad": 0.15},
            {"nombre": "pollo", "cantidad": 0.10},
            {"nombre": "cebolla", "cantidad": 0.06}
        ]
    },
    "Bacon y Cebolla": {
        "nombre": "Bacon y Cebolla",
        "precio": None,
        "descripcion": "Tomate, queso, bacon y cebolla.",
        "tamano": "mediana",
        "tipo_de_masa": "clasica",
        "ingredientes": [
            {"nombre": "harina", "cantidad": 0.25},
            {"nombre": "tomate", "cantidad": 0.10},
            {"nombre": "queso", "cantidad": 0.12},
            {"nombre": "bacon", "cantidad": 0.07},
            {"nombre": "cebolla", "cantidad": 0.06}
        ]
    },
    "York y Champiñones": {
        "nombre": "York y Champiñones",
        "precio": None,
        "descripcion": "Tomate, queso, jamón y champiñones.",
        "tamano": "mediana",
        "tipo_de_masa": "clasica",
        "ingredientes": [
            {"nombre": "harina", "cantidad": 0.25},
            {"nombre": "tomate", "cantidad": 0.10},
            {"nombre": "queso", "cantidad": 0.12},
            {"nombre": "jamon", "cantidad": 0.08},
            {"nombre": "champinones", "cantidad": 0.08}
        ]
    },
    "Mediterránea": {
        "nombre": "Mediterránea",
        "precio": None,
        "descripcion": "Tomate, mozzarella, atún y aceitunas.",
        "tamano": "mediana",
        "tipo_de_masa": "fina",
        "ingredientes": [
            {"nombre": "harina", "cantidad": 0.20},
            {"nombre": "tomate", "cantidad": 0.10},
            {"nombre": "mozzarella", "cantidad": 0.15},
            {"nombre": "atun", "cantidad": 0.08},
            {"nombre": "aceitunas", "cantidad": 0.04}
        ]
    },
    "Campestre": {
        "nombre": "Campestre",
        "precio": None,
        "descripcion": "Tomate, queso, pollo y champiñones.",
        "tamano": "mediana",
        "tipo_de_masa": "clasica",
        "ingredientes": [
            {"nombre": "harina", "cantidad": 0.25},
            {"nombre": "tomate", "cantidad": 0.10},
            {"nombre": "queso", "cantidad": 0.12},
            {"nombre": "pollo", "cantidad": 0.10},
            {"nombre": "champinones", "cantidad": 0.08}
        ]
    },
    "Americana": {
        "nombre": "Americana",
        "precio": None,
        "descripcion": "Tomate, mozzarella, pepperoni y bacon.",
        "tamano": "mediana",
        "tipo_de_masa": "clasica",
        "ingredientes": [
            {"nombre": "harina", "cantidad": 0.25},
            {"nombre": "tomate", "cantidad": 0.10},
            {"nombre": "mozzarella", "cantidad": 0.15},
            {"nombre": "pepperoni", "cantidad": 0.07},
            {"nombre": "bacon", "cantidad": 0.07}
        ]
    },
    "Rústica": {
        "nombre": "Rústica",
        "precio": None,
        "descripcion": "Tomate, queso, cebolla y aceitunas.",
        "tamano": "mediana",
        "tipo_de_masa": "fina",
        "ingredientes": [
            {"nombre": "harina", "cantidad": 0.20},
            {"nombre": "tomate", "cantidad": 0.10},
            {"nombre": "queso", "cantidad": 0.12},
            {"nombre": "cebolla", "cantidad": 0.06},
            {"nombre": "aceitunas", "cantidad": 0.04}
        ]
    },
    "Carnívora": {
        "nombre": "Carnívora",
        "precio": None,
        "descripcion": "Tomate, queso, jamón, bacon y pepperoni.",
        "tamano": "mediana",
        "tipo_de_masa": "clasica",
        "ingredientes": [
            {"nombre": "harina", "cantidad": 0.25},
            {"nombre": "tomate", "cantidad": 0.10},
            {"nombre": "queso", "cantidad": 0.12},
            {"nombre": "jamon", "cantidad": 0.08},
            {"nombre": "bacon", "cantidad": 0.07},
            {"nombre": "pepperoni", "cantidad": 0.07}
        ]
    },
    "Bianca": {
        "nombre": "Bianca",
        "precio": None,
        "descripcion": "Sin tomate: mozzarella y queso.",
        "tamano": "mediana",
        "tipo_de_masa": "fina",
        "ingredientes": [
            {"nombre": "harina", "cantidad": 0.20},
            {"nombre": "mozzarella", "cantidad": 0.15},
            {"nombre": "queso", "cantidad": 0.12}
        ]
    },
    "Prosciutto y Aceitunas": {
        "nombre": "Prosciutto y Aceitunas",
        "precio": None,
        "descripcion": "Tomate, queso, jamón y aceitunas.",
        "tamano": "mediana",
        "tipo_de_masa": "fina",
        "ingredientes": [
            {"nombre": "harina", "cantidad": 0.20},
            {"nombre": "tomate", "cantidad": 0.10},
            {"nombre": "queso", "cantidad": 0.12},
            {"nombre": "jamon", "cantidad": 0.08},
            {"nombre": "aceitunas", "cantidad": 0.04}
        ]
    },
    "Pepperoni Funghi": {
        "nombre": "Pepperoni Funghi",
        "precio": None,
        "descripcion": "Tomate, mozzarella, pepperoni y champiñones.",
        "tamano": "mediana",
        "tipo_de_masa": "fina",
        "ingredientes": [
            {"nombre": "harina", "cantidad": 0.20},
            {"nombre": "tomate", "cantidad": 0.10},
            {"nombre": "mozzarella", "cantidad": 0.15},
            {"nombre": "pepperoni", "cantidad": 0.07},
            {"nombre": "champinones", "cantidad": 0.08}
        ]
    },
    "Bacon y Champiñones": {
        "nombre": "Bacon y Champiñones",
        "precio": None,
        "descripcion": "Tomate, queso, bacon y champiñones.",
        "tamano": "mediana",
        "tipo_de_masa": "clasica",
        "ingredientes": [
            {"nombre": "harina", "cantidad": 0.25},
            {"nombre": "tomate", "cantidad": 0.10},
            {"nombre": "queso", "cantidad": 0.12},
            {"nombre": "bacon", "cantidad": 0.07},
            {"nombre": "champinones", "cantidad": 0.08}
        ]
    }
}