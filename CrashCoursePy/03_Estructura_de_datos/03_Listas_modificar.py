

#Modificar listas

nombres: list[str] = ["Eduardo", "Maria", "Luis", "Pepe"]

nombres[2] = "Fernando"
print(f"{nombres = }") #Cambia el nombre en la posicion 2

#Append
nombres.append("Fiona")
print(f"{nombres = }") #Agrega al final de la lista

#Insert
nombres.insert(1, "Sofia")
print(f"{nombres = }") #Inserta en la posicion 1 el nombre Sofia

#Remove
nombres.remove("Eduardo")
print(f"{nombres = }") #Elimina el primer elemento que coincida con el parametro


otros_nombres: list[str] = ["Johan", "Carmela", "Mariana", "Alejandro"]

#pop
print(otros_nombres.pop())
print(f"{otros_nombres = }") #Elimina el ultimo elemento de la lista

