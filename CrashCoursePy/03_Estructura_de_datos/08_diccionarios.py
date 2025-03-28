

#son colecciones de datos que se almacenan con un indice, clave valor
#se pueden modificar, agregar y eliminar elementos

#poblacion_paises: dict = {
#    "Mexico": 126_000_000,
#    "Canada": 37_000_000,
#    "Japon": 125_000_000
#}


#un diccionario puede contener cualquier tipo de dato
#numeros: dict[str, list[int]] = {
#    "primos": [2, 3, 5, 7, 11],
#    "pares": [0, 2, 4, 6, 8],
#    "impares": [1, 3, 5, 7, 9]
#}




#incluso puede contener otros diccionarios
#ciudades_paises: dict[str, dict[str, int]] = {
#    "Mexico": {"CDMX": 9_000_000, "Guadalajara": 5_000_000, "Monterrey": 4_000_000},
#    "Canada": {"Toronto": 6_000_000, "Montreal": 4_000_000, "Vancouver": 3_000_000},
#    "Japon": {"Tokio": 9_000_000, "Osaka": 5_000_000, "Kyoto": 4_000_000}
#}



poblacion_paises: dict = {
    "Mexico": 126_000_000,
    "Canada": 37_000_000,
    "Japon": 125_000_000
}

vacio:dict = {

}

colores:dict = dict(rojo = "red", verde = "green", azul = "blue")

print(poblacion_paises) 
print(vacio)
print(colores)

#Accesar a valores
#print(f" Poblacion de Mexico: {poblacion_paises["Mexico"]}")

#Modificar valores
#poblacion_paises["Mexico"] = 130_000_000
#print(f" Poblacion de Mexico: {poblacion_paises["Mexico"]}")


poblacion_paises["Brasil"] = 210_000_000
print(poblacion_paises)

#GET

#print(poblacion_paises["Uruguay"])

print(poblacion_paises.get("Uruguay")) #none
print(poblacion_paises) #imprime el diccionario completo sin modificarlo



