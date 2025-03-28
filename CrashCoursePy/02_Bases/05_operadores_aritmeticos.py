x: int = 10
y: int = 3

suma = x + y
resta = x - y
multiplicacion = x * y
division = x / y
division_entera = x // y 
modulo = x % y #modulo se refiere a el residuo de la operacion 
exponente = x ** y

#print(f"{}) hace referencia a f-strings


print(f"{suma = }")
print(f"{resta = }")
print(f"{multiplicacion = }")
print(f"{division = }")
print(f"{division_entera = }")
print(f"{modulo = }")
print(f"{exponente = }")

#x = x + 5 es exactamente igual que x += 5 

x += 5 
print(x)

x -= 2
print(x)