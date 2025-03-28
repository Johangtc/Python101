#Listas

nombres: list[str] = ["Juan", "Pedro", "Maria", "Ana"]
edades: list[int] = [23, 34, 45, 56]

lista_combinada: list = ["Johan", 12, 23.4, True]

print(nombres[0])
print(edades[1])

#para acceder al ultimo elemento de la lista
print(nombres[-1]) #ultimo
print(edades[-2]) #penultimo

#Slice List[Inicio : Fin : Salto]
#                     0 1 2 3 4 5 6 7 8 9    Indice que tiene cada numero
numeros: list[int] = [1,2,3,4,5,6,7,8,9,10]

print(numeros[1 : 6]) #2,3,4,5,6
# Primer numero inclusivo y el ultimo es exclusivo

#si queremos imprimir hasta el numero 7
print(numeros[1 : 7]) #2,3,4,5,6,7

#si queremos imprimir con un salto
print(numeros[1 : 7 : 2]) #2,4,6
    