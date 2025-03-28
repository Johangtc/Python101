#Calculadora de calificaciones/notas:
#Estas creando un programa que ayudara a un profesor a calcular si un alumno aprobo o no
#El programa pedira nombre del alumno y 3 calificaciones/notas
#El resultado del programa debe ser parecido a: "Eduardo aprobo = True, su promedio fue 8.50"
#La calificacion aprobatoria sera 6

#Ingresar el nombre del alumno
nombre: str = input(" Ingrese el nombre del alumno ")

#Ingresar las calificaciones 
calificacion_1: float = float(input(" Ingrese la calificacion 1: "))
calificacion_2: float = float(input(" Ingrese la calificacion 2: "))
calificacion_3: float = float(input(" Ingrese la calificacion 3: "))

#Calcular el promedio
promedio: float = (calificacion_1 + calificacion_2 + calificacion_3) / 3

#Revisar si aprobo o no

aprobo: bool = promedio >= 6 ; True

#Imprimir el resultado
print(f"{nombre} {aprobo = }, su promedio fue {promedio:.2f}")