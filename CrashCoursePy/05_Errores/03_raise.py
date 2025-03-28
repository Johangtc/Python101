

try:
    edad: int = int(input("Introduce tu edad: "))
    if edad < 0:
        raise Exception("La edad no puede ser negativa")
except ValueError as e:
    print("ValueError")
except Exception as e:
    print(f"Excepcion: {e}")
#else: CASI NADIE USA ELSE
#    print("Todo fue un exito!, ingresaste bien la edad ")