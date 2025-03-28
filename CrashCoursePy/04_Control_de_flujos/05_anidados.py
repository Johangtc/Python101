
#
#username: str = input("Introduce el nombre de usuario: ")
#password: str = input("Introduce la contraseña: ")
#
#if username == "admin":
#    if password == "secret":
#        print("Login correcto")
#    else:
#        print("Password incorrecto")
#else: 
#    print("Nombre de usuario incorrecto")
#

#for i in range(1,6):
#    for j in range(1,6):
#        print(i*j, end="/t")
#    print()

rows: int = 5 
columns: int = 5

for row in range( 1, rows + 1):
    for column in range( 1, columns + 1):
        if (row + column) % 2 == 0:
            print("X", end="")
        else:
            print("O", end="")
    print()