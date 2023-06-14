# Hacer una función que dibuje una raya con un caracter y una longitud dada.

def drawLineWith(char, length):
    finalLine = ''
    for i in range(length):
        finalLine += char

    return finalLine

print(drawLineWith('-', 35))
print(drawLineWith('═', 35))
print(drawLineWith('=', 35))
