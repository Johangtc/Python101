#Ejercicio 1 
#Crear un programa que calcule el área de un triángulo.
#El usuario debe ingresar la base y la altura del triángulo. El usuario puede ingresar floats
#El programa debe imprimir el área del triángulo en la consola.
#EXTRA: dar formato al numero dentro de la F string para siempre mostrar 2 decimales

base: float = float(input(" Ingrese la base del triangulo: "))
altura: float = float(input(" Ingrese la altura del triangulo: "))

area: float = (base * altura) / 2

print(f" El area del triangulo es: {area:.2f}")


