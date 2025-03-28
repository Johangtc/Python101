

# and, or,  not
#devuelven siempre un valor booleano



#AND
edad: int = 17
tiene_licencia: bool = True

puede_conducir: bool = (edad >= 18 ) and tiene_licencia
print(f"{ puede_conducir = }")

#OR
tiene_hambre: bool = False
tiene_frio: bool = False
esta_enojado: bool = tiene_hambre or tiene_frio

print(f"{ esta_enojado = }") #En caso de que alguna sola afirmacion sea True esta devolvera True 
#En caso de que las dos sean False entonces esta_enojado devuelve False

print(f"{ not esta_enojado = }") # el not lo utilizamos como una doble negacion por lo que nos devolvera un True



