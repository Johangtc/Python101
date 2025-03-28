
                                            #Sets

#sets , se parecen a las listas pero no tienen orden y no tienen elementos repetidos
#se crean con llaves
#se parecen a las tuplas pero no tienen orden y no tienen elementos repetidos
#se crean con llaves

basket: set[str] = {"apple", "orange", "banana", "kiwi", "apple"}
# basket_2: set[str, int ] = {"aldo", "johan", "carmela", "kiwi", 2} como se ve podemos tener combinacion
print(basket)

fruits: set[str] = set(["apple", "orange", "apple"])
print(fruits)

numbers: set[int] = {"1", "1", "2", "3"}
print(numbers)

#Agregar 

numbers.add(7)
print(numbers)

#Remover
numbers.remove("3")

#verificacion
print( 7 in numbers ) #True

set1: set[int] = {1, 2, 3}
set2: set[int] = {3, 4, 5}

#union |
print(set1 | set2) # {1, 2, 3, 4, 5}

#interseccion &
print(set1 & set2) # {3}
 
#diferencia -
print(set1 - set2) # {1, 2}

#es muy comun para remover los duplicados de una lista
