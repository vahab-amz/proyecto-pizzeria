from objetos import Pizza, Ingrediente
pizzas = [
    Pizza(
        "Margarita", None, "La clásica: tomate y queso.", "mediana", "clasica",
        [
            Ingrediente("harina", 0.25),
            Ingrediente("tomate", 0.10),
            Ingrediente("queso", 0.12),
        ],
    ),
    Pizza(
        "Prosciutto", None, "Tomate, queso y jamón.", "mediana", "clasica",
        [
            Ingrediente("harina", 0.25),
            Ingrediente("tomate", 0.10),
            Ingrediente("queso", 0.12),
            Ingrediente("jamon", 0.08),
        ],
    ),
    Pizza(
        "Barbacoa", None, "Tomate, queso, bacon y pollo.", "mediana", "clasica",
        [
            Ingrediente("harina", 0.25),
            Ingrediente("tomate", 0.10),
            Ingrediente("queso", 0.12),
            Ingrediente("bacon", 0.07),
            Ingrediente("pollo", 0.10),
        ],
    ),
    Pizza(
        "Pepperoni", None, "Tomate, mozzarella y pepperoni.", "mediana", "fina",
        [
            Ingrediente("harina", 0.20),
            Ingrediente("tomate", 0.10),
            Ingrediente("mozzarella", 0.15),
            Ingrediente("pepperoni", 0.07),
        ],
    ),
    Pizza(
        "Dos Quesos", None, "Tomate, queso y mozzarella.", "mediana", "fina",
        [
            Ingrediente("harina", 0.20),
            Ingrediente("tomate", 0.10),
            Ingrediente("queso", 0.12),
            Ingrediente("mozzarella", 0.15),
        ],
    ),
    Pizza(
        "Atún", None, "Tomate, queso, atún y cebolla.", "mediana", "clasica",
        [
            Ingrediente("harina", 0.25),
            Ingrediente("tomate", 0.10),
            Ingrediente("queso", 0.12),
            Ingrediente("atun", 0.08),
            Ingrediente("cebolla", 0.06),
        ],
    ),
    Pizza(
        "Funghi", None, "Tomate, queso y champiñones.", "mediana", "fina",
        [
            Ingrediente("harina", 0.20),
            Ingrediente("tomate", 0.10),
            Ingrediente("queso", 0.12),
            Ingrediente("champinones", 0.08),
        ],
    ),
    Pizza(
        "Vegetal", None,
        "Tomate, queso, champiñones, cebolla y aceitunas.",
        "mediana", "fina",
        [
            Ingrediente("harina", 0.20),
            Ingrediente("tomate", 0.10),
            Ingrediente("queso", 0.12),
            Ingrediente("champinones", 0.08),
            Ingrediente("cebolla", 0.06),
            Ingrediente("aceitunas", 0.04),
        ],
    ),
    Pizza(
        "Pollo", None, "Tomate, mozzarella, pollo y cebolla.",
        "mediana", "clasica",
        [
            Ingrediente("harina", 0.25),
            Ingrediente("tomate", 0.10),
            Ingrediente("mozzarella", 0.15),
            Ingrediente("pollo", 0.10),
            Ingrediente("cebolla", 0.06),
        ],
    ),
    Pizza(
        "Bacon y Cebolla", None, "Tomate, queso, bacon y cebolla.",
        "mediana", "clasica",
        [
            Ingrediente("harina", 0.25),
            Ingrediente("tomate", 0.10),
            Ingrediente("queso", 0.12),
            Ingrediente("bacon", 0.07),
            Ingrediente("cebolla", 0.06),
        ],
    ),
    Pizza(
        "York y Champiñones", None, "Tomate, queso, jamón y champiñones.",
        "mediana", "clasica",
        [
            Ingrediente("harina", 0.25),
            Ingrediente("tomate", 0.10),
            Ingrediente("queso", 0.12),
            Ingrediente("jamon", 0.08),
            Ingrediente("champinones", 0.08),
        ],
    ),
    Pizza(
        "Mediterránea", None, "Tomate, mozzarella, atún y aceitunas.",
        "mediana", "fina",
        [
            Ingrediente("harina", 0.20),
            Ingrediente("tomate", 0.10),
            Ingrediente("mozzarella", 0.15),
            Ingrediente("atun", 0.08),
            Ingrediente("aceitunas", 0.04),
        ],
    ),
    Pizza(
        "Campestre", None, "Tomate, queso, pollo y champiñones.",
        "mediana", "clasica",
        [
            Ingrediente("harina", 0.25),
            Ingrediente("tomate", 0.10),
            Ingrediente("queso", 0.12),
            Ingrediente("pollo", 0.10),
            Ingrediente("champinones", 0.08),
        ],
    ),
    Pizza(
        "Americana", None, "Tomate, mozzarella, pepperoni y bacon.",
        "mediana", "clasica",
        [
            Ingrediente("harina", 0.25),
            Ingrediente("tomate", 0.10),
            Ingrediente("mozzarella", 0.15),
            Ingrediente("pepperoni", 0.07),
            Ingrediente("bacon", 0.07),
        ],
    ),
    Pizza(
        "Rústica", None, "Tomate, queso, cebolla y aceitunas.",
        "mediana", "fina",
        [
            Ingrediente("harina", 0.20),
            Ingrediente("tomate", 0.10),
            Ingrediente("queso", 0.12),
            Ingrediente("cebolla", 0.06),
            Ingrediente("aceitunas", 0.04),
        ],
    ),
    Pizza(
        "Carnívora", None, "Tomate, queso, jamón, bacon y pepperoni.",
        "mediana", "clasica",
        [
            Ingrediente("harina", 0.25),
            Ingrediente("tomate", 0.10),
            Ingrediente("queso", 0.12),
            Ingrediente("jamon", 0.08),
            Ingrediente("bacon", 0.07),
            Ingrediente("pepperoni", 0.07),
        ],
    ),
    Pizza(
        "Bianca", None, "Sin tomate: mozzarella y queso.", "mediana", "fina",
        [
            Ingrediente("harina", 0.20),
            Ingrediente("mozzarella", 0.15),
            Ingrediente("queso", 0.12),
        ],
    ),
    Pizza(
        "Prosciutto y Aceitunas", None, "Tomate, queso, jamón y aceitunas.",
        "mediana", "fina",
        [
            Ingrediente("harina", 0.20),
            Ingrediente("tomate", 0.10),
            Ingrediente("queso", 0.12),
            Ingrediente("jamon", 0.08),
            Ingrediente("aceitunas", 0.04),
        ],
    ),
    Pizza(
        "Pepperoni Funghi", None,
        "Tomate, mozzarella, pepperoni y champiñones.",
        "mediana", "fina",
        [
            Ingrediente("harina", 0.20),
            Ingrediente("tomate", 0.10),
            Ingrediente("mozzarella", 0.15),
            Ingrediente("pepperoni", 0.07),
            Ingrediente("champinones", 0.08),
        ],
    ),
    Pizza(
        "Bacon y Champiñones", None, "Tomate, queso, bacon y champiñones.",
        "mediana", "clasica",
        [
            Ingrediente("harina", 0.25),
            Ingrediente("tomate", 0.10),
            Ingrediente("queso", 0.12),
            Ingrediente("bacon", 0.07),
            Ingrediente("champinones", 0.08),
        ],
    ),
]