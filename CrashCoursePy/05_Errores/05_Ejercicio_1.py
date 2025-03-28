''' Calculadora con manejo de excepciones

Pide al usuario que ingrese dos números (no importa si son float) luego,
pide al usuario que elija una operación de las siguientes: +, -, *, /.

El programa debe prevenir errores usando try-except en caso de que:
El usuario ingresa un valor que no es numérico.
El usuario intenta dividir entre cero.
El usuario ingresa una operación no válida.
Usa raise para lanzar una excepción personalizada si la operación seleccionada no es válida. '''

try:
    #Solicita la entrada al usuario
    number1: float  = float(input('Ingrese el primer número: '))
    number2: float  = float(input('Ingrese el segundo número: '))
    
    #Solicita la operacion al usuario
    operation: str = input("Ingrese la operación que desea realizar (+, -, *, /): ")

    #Declara la variable resultado
    result: float = 0

    #Realiza la operacion
    if operation == "+":
        resultado = number1 + number2
    elif operation == "-":
        resultado = number1 - number2
    elif operation == "*":
        resultado = number1 * number2
    elif operation == "/":
        if number2 == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        resultado = number1 / number2
    else:
        #Levantar excepcion
        Exception("Operación no válida, elige +, -, *, /")
    print(f"EL resultado es: {resultado}")
except ValueError as e:
    print("Ingresaste un valor no numérico")
except ZeroDivisionError as e:
    print(f"Error de valor {e}")
except Exception as e:
    print(e)







