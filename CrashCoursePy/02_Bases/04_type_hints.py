


#age = 21
#print(age)
#print(type(age))
#
#name = "Johan"
#print(name)
#print(type(name))

#podemos obligar a declarar variables correctas, por ejemplo

age: int = 21
print(age)
print(type(age))


#esto nos dara un error
#age = "Johan"
#print(age)
#print(type(age))

#estas son buenas practicas de programacion en python
name: str = "Johan"
pi: float = 3.1416
is_active: bool = True

# print("Mi nombre es: " + name )
print(f"Mi nombre es: {name}")


print(f"{name =}")
