

#ARGS

#def sumar(*args:int ) -> int :
#    #print(args)
#    return(sum(args))
#
#print(sumar(1,2,3,4)) #se crea una tupla 


def saludar_sumar(saludo: str, *args: int , despedida: str) -> None:
    total = sum(args)
    print(saludo)
    print(f"El total es {total}")
    print(despedida)

saludar_sumar("Hola", 10,10,10,10,10, despedida = "Adios")


#KWARGS
#Key Words ARGumentS


from typing import Any
def mostrar_datos(**kwargs: Any ):
    print(kwargs)

mostrar_datos(Nombre ="Johan", a=1, b=2, c=317)
