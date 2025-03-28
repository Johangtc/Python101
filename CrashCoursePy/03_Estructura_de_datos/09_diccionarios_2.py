

poblacion_paises: dict = {
    "Mexico": 120_000_000,
    "Canada": 37_000_000,
    "Japon": 126_000_000,
    "Argentina": 44_000_000,
    "Colombia": 50_000_000
}

# Pop
print(poblacion_paises.pop("Canada"))
print(poblacion_paises)

#Si no encuentra una clave lo ideal es que regresemos algun comentario para evitar un error
print(poblacion_paises.get("Brasil", "No se encontro la clave"))
print(poblacion_paises)

#Del
#elimina un elemento de un diccionario

del poblacion_paises["Japon"]
print(poblacion_paises)


#como limpiar todo el diccionario

poblacion_paises.clear()
print(poblacion_paises) #{}