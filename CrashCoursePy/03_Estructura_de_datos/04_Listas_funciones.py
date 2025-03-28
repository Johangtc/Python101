

# Funciones utiles

numeros: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Len
print(len(numeros))  # 10 numeros en la lista

#Max / Min
print(max(numeros))  # 10 es el numero mas grande
print(min(numeros))  # 1 es el numero mas pequeño

#Sum
print(sum(numeros))  # 55 suma de todos los numeros

nombres: list[str] = ["Fernando" , "Hugo", "Maria", "Luis"]
                      
#Sort ordena la lista
print(nombres.sort())  # None
print(nombres)  # ['Fernando', 'Hugo', 'Luis', 'Maria']

#por lo que es mejor utilizar el metodo sorted
print(sorted(nombres))  # ['Fernando', 'Hugo', 'Luis', 'Maria']

#Count cuantas veces se repite un elemento
print(nombres.count("Fernando"))  # 1

#Index devuelve el indice de un elemento
print(nombres.index("Fernando"))  # 0

#Reverse invierte la lista
#funciona igual que sort no devuelve nada
print(nombres.reverse())  # None    
print(nombres)  # ['Luis', 'Maria', 'Hugo', 'Fernando']

#Saludando a todos con un ciclo for

for nombres in nombres:
    print(f"Hola {nombres = }")

