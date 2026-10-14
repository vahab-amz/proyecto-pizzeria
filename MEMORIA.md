# Memoria del proyecto: Caja registradora de una pizzería

**Integrantes:** Vahab Azimzadeh · Elias Rafols
**Repositorio:** [enlace al repositorio de GitHub]
**Tablero Trello:** https://trello.com/b/6XcZJMjy/proyecto-pizzaria

---

## Día 1 · Miércoles, 7 de octubre de 2026

### Resumen

Primer día de trabajo. Leímos el enunciado, creamos el tablero de Trello, definimos la estructura de datos de las pizzas y montamos la estructura base del proyecto para que cada integrante pueda trabajar en su propia rama.

### Reunión inicial y acuerdos

- Empezar con **20 pizzas sencillas**, sin ingredientes complejos.
- Usar solo los ingredientes que da el enunciado.
- El programa tendrá un **menú principal** donde el usuario elige si es **cliente** o **trabajador**.

### Organización en Trello

- Creamos el tablero `proyecto-pizzaria` y añadimos a los dos integrantes.
- Las listas al principio eran `ToDo`, `Doing` y `Done`. Las cambiamos a **pendientes, en proceso, revisión y terminadas**, porque el enunciado pide reflejar también las tareas en revisión.
- Tarjetas creadas:
  - Crear base de datos
  - Crear menú principal (elegir cliente o trabajador)
  - Crear menú Trabajador (pizzas, almacén, ofertas)
  - Crear menú Cliente (pedir, listar, modificar y eliminar pedido)

> 📸 *Captura del tablero (Día 1)*

### Estructura de datos de las pizzas

Cada pizza se guarda en un diccionario, usando su nombre como clave:

```python
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
}
```

Decisiones tomadas:

- **El precio no se escribe a mano.** Se deja en `None` y lo calculará la función `calcular_precio_pizza()`, como exige el enunciado.
- **Los precios de los ingredientes son en €/kg** y la `cantidad` de cada ingrediente está en kg. Así, el coste de un ingrediente es `precio_por_kg * cantidad`.
- **Tipo de masa:** la masa fina usa 0.20 kg de harina y la clásica 0.25 kg, así que el tipo de masa influye en el coste.
- **Tamaño:** de momento todas las pizzas son medianas, para mantenerlo sencillo.
- Las claves del diccionario van sin tildes ni ñ (`descripcion`, `tamano`), igual que en el enunciado (`jamon`, `champinones`).

Comprobación: con la fórmula del enunciado (temporada media, margen del 35 %), la Margarita sale a unos **10.85 €** con IVA.

### Estructura del proyecto

Organizamos el código en paquetes de Python usando archivos `__init__.py`, que funcionan como un "índice" de cada carpeta:

```
proyecto-pizzeria/
├── main.py
├── listas/
│   ├── ingredientes.py
│   └── pizzas.py
└── funciones/
    ├── general/       ← funciones compartidas
    ├── cliente/       ← parte cliente
    └── trabajador/    ← parte trabajador
```

- `main.py` contiene el menú principal con `match-case`.
- Cada carpeta tiene un `__init__.py` que exporta sus funciones principales. Por ejemplo, en `main.py` basta con escribir `from funciones.cliente import menu_cliente`.
- Añadimos un `.gitignore` para no subir la carpeta `__pycache__`.

### Problemas detectados y cómo se resolvieron

| Problema | Solución |
|----------|----------|
| La tarjeta "Crear base de datos" choca con el enunciado, que prohíbe usar bases de datos. | Los datos se guardan en diccionarios y listas dentro del programa. |
| El carrito y la opción de pagar aparecían en el menú del trabajador. | El carrito pasa a la parte del cliente (`funciones/cliente/pedido.py`). |
| Algunas tarjetas no tenían responsable ni descripción. | Hay que completarlas, ya que el enunciado lo exige para cada tarea. |
| Si una función reasigna el diccionario (`pizzas = {...}`), el otro módulo no ve el cambio. | Acordamos modificar el diccionario sin reasignarlo, por ejemplo `pizzas["Nueva"] = {...}` o `del pizzas[nombre]`. |

### Cambios respecto a la idea inicial

- La lista `ToDo / Doing / Done` pasó a tener cuatro estados, añadiendo **revisión**.
- La "base de datos" se sustituye por estructuras de datos en memoria.
- El carrito se movió del menú del trabajador al del cliente.

### Próximos pasos

- [ ] Completar las tarjetas de Trello con responsable y descripción.
- [ ] Crear las tarjetas que faltan: temporada, cálculo de precios, bebidas, ofertas, ticket, pruebas, README y memoria.
- [ ] Crear las ramas `feature/cliente` y `feature/trabajador`.
- [ ] Implementar `calcular_coste_ingredientes()` y `calcular_precio_pizza()`.