# Pedir el ingreso de un nombre completo (Juan Pérez) y mostrarlo invertido y con coma (Pérez, Juan).

def formatLastNameFirst(name):
    nameSplitted = name.split()

    return nameSplitted[1] + ', ' + nameSplitted[0]

name = input('Ingresa un nombre: ')

print(formatLastNameFirst(name))
