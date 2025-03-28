

number: int = 5

if number > 0:
    print(f'{number} es positivo')
elif number == 0:
    print(f'{number} es cero')
else:
    print(f'{number} es negativo')

is_user: bool = True
is_admin: bool = False

if is_user:
    print('El usuario es un usuario')
elif is_admin:
    print('El usuario es un administrador')