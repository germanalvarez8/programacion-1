# Crea una función que calcule la suma de los dígitos de un número entero.

def sumdigits(number):
    stringNumber = str(number)
    total = 0

    for char in stringNumber:
        total += int(char)

    return total

print(sumdigits(123))
print(sumdigits(236))
print(sumdigits(538))

