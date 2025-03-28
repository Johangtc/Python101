frutas: frozenset = frozenset(["manzana", "naranja", "kiwi"])
print(frutas)

# No se puede modificar un frozenset
# frutas.add("pera")  # AttributeError: 'frozenset' object has no attribute 'add'
# frutas.remove("naranja")  # AttributeError: 'frozenset' object has no attribute 'remove'

