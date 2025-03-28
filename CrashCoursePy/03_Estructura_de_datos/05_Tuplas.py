

#Tuplas
mi_tupla: tuple[str, int, float] = ("Manzana", 10, 3.1415)


#Modificar tupla
#mi_tupla[0] = "Naranja"

#como se ve no se puede modificar la tupla, por lo que es diferente a las listas

#podemos acceder con un Slice
print(mi_tupla[1 : 3])

#desempaquetar datos
fruta, cantidad, pi = mi_tupla
print(f"{fruta = }") #Manzana
print(f"{cantidad = }") #10
print(f"{pi = }") #3.1415


print(len(mi_tupla)) #3
print("manzana" in mi_tupla) #True , es para verificar si existe un elemento en la tupla

numeros: tuple [ int, str] = (5, "hola")

print(mi_tupla + numeros) #('Manzana', 10, 3.1415, 5, 'hola') es una concatenacion



