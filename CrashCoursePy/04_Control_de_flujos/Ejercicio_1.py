#Escribe un programa que le pida al usuario la altura y que imprima una piramide de numeros con esa altura
#Como ejemplo, si el usuario ingresa 5, la piramide se debe ver de esta forma:
#    1
#   121
#  12321
# 1234321
#123454321

altura: int = int(input("Ingrese la altura: "))

for row in range(1, altura + 1):

#Imprimir los espacios en blanco antes de los numeros
    for space in range(altura - row):
        print(" ", end="")

#Imprimir los numeros en orden ascendente
    for num in range(1, row + 1):
        print(num, end="")

#Imprimir los numeros en orden descendente  
    for num in range(row - 1, 0, -1):
        print(num, end="")
    print()
