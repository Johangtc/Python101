""" Imagina que tienes una tienda en línea que vende varios productos, 
y quieres manejar los precios de los productos. 
Crea una lista con los precios de 5 productos: 50.0, 75.5, 23.9, 80.1, 99.99 
luego convertir esa lista a una tupla (ya que los precios no cambiarán después de ser establecidos). 
Finalmente, debes obtener el precio del producto que el usuario indique"""

#EXTRA convertir los precios a una tupla de cadena que incluya el simbolo moneda $ al inicio de cada precio

precios: list = [50.0, 75.5, 23.9, 80.1, 99.99]
tuple_precios: tuple = tuple(precios)

producto: int = int(input("Ingrese el numero del producto que desea consultar (1,2,3,4,5): "))
# Restamos 1 porque los índices en Python comienzan en 0
print(f"El precio del producto {producto} es: ${tuple_precios[producto - 1]:.2f}")

print("Si desea consultar el precio de otro producto, vuelva a ejecutar el programa.")

# El código no maneja casos en los que el usuario ingrese un número fuera del rango de  
# índices válidos (por ejemplo, 0 o un número mayor que 5). Esto podría causar un error IndexError.