#Todas las funciones retornan un valor

def sumar(a: int, b: int, c: int) -> int:
    total = a + b + c
    print(f"El total es {total}")
    return total


def sumar2(a: int, b: int, c: int) -> None:
    total = a + b + c
    print(f"El total es {total}")
    

mi_variable = sumar(1,2,3)
mi_variable2 = sumar2(1,2,3)


print(mi_variable)

