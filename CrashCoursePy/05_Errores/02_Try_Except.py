

try:
    numero: int = int(input("Ingrese un número: ")) 
    resultado: float = 10/numero
except ZeroDivisionError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"error {e}")
finally:
    print("Finally corrio")
    
print("Fin del programa")

