# Cuántas veces se repite una letra cualquiera. Parámetros: letra, cadena.
# Concatenar un número indeterminado de strings con un caracter específico (por defecto un espacio).

def concatWithConnector(*args, connector=' '):
    finalString = ''
    for i in range(len(args)):
        if i == 0:
            finalString += args[i]
        else:
            finalString += connector + args[i]

    return finalString

print(concatWithConnector('hola', 'pibe'))
print(concatWithConnector('hola', 'pibe', connector='@'))
print(concatWithConnector('techo', 'mesa', 'árbol', connector='###'))
print(concatWithConnector('techo', 'mesa', 'árbol', connector='|||||||'))
