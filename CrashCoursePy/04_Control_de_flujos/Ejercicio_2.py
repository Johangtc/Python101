#Desarrolla un programa que genere un número aleatorio entre 1 y 100 (usando el módulo random) y 
#le pida al usuario que lo adivine.
#El programa debe:
#- Obtener el input de la adivinanza.
#- Comparar el número ingresado con el número aleatorio.
#- Mostrar un mensaje si el número es correcto o incorrecto.
#- Detenerse si el usuario adivina el número.
#- Proporcionar pistas al usuario si el número es demasiado alto o bajo.
#- Limitar el número de intentos del usuario (10).
#- Al final, mostrar el número aleatorio y el número de intentos realizados.
#
#EXTRA: Manejar entradas no válidas (por ejemplo, letras en lugar de números).

import random

# Generar un número aleatorio entre 0 y 100
numero_aleatorio: int = random.randint(0, 100)

# Inicializar el contador de intentos
intentos: int = 0
intento_maximo: int = 10

print("¡Bienvenido al juego de adivinar el número!")
print("Tienes que adivinar un número entre 1 y 100. ¡Tienes 10 intentos!")

while intentos < intento_maximo:
    # Obtener la entrada del usuario
    adivinanza = input("Intento #{}: Ingresa tu numero: ".format(intentos + 1))

    # Validar la entrada
    try:
        adivinanza = int(adivinanza)  # Convertir a entero
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue  # Volver al inicio del bucle sin contar el intento

    # Incrementar el contador de intentos
    intentos += 1

    # Comparación del número ingresado con el número aleatorio
    if adivinanza < numero_aleatorio:
        print("El número es muy bajo. Intenta de nuevo.")
    elif adivinanza > numero_aleatorio:
        print("El número es muy alto. Intenta de nuevo.")
    else:
        print("¡Felicidades! ¡Adivinaste el número!")
        break  # Salir del bucle si el usuario adivina

# Si no se adivina el número
if intentos == intento_maximo:
    print("¡Lo siento! ¡Te has quedado sin intentos! El número era {}.".format(numero_aleatorio))

# Mostrar el número aleatorio y el número de intentos realizados
print("El número aleatorio era {}.".format(numero_aleatorio))
print("Número de intentos realizados: {}.".format(intentos))