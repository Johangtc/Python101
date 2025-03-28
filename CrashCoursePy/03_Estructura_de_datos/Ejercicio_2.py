"""Crea un diccionario llamado inventario que contenga los siguientes productos y cantidades:
"smartphone": 10
"laptop": 5
"tablet": 8
Muestra el inventario completo.
Pregunta al usuario que producto quiere consultar, e imprime el valor,
Si el producto no existe el progrma debe imprimir none

Extra: Crea un segundo diccionario llamado 
nuevos_productos con otros tres productos y sus cantidades. 
Luego, combina ambos diccionarios en uno solo llamado inventario_total
usando una función adecuada."""

inventario: dict = {
    "smartphone": 10,
    "laptop": 5,
    "tablet": 8
}

print(inventario)

producto: str = input("¿Qué producto quieres consultar? ")
cantidad = inventario.get(producto, None)
print(cantidad)

nuevos_productos: dict = {
    "teclado": 4,
    "mouse": 7,
    "monitor": 3
}

inventario_total: dict = dict(inventario, **nuevos_productos)

print(inventario_total)