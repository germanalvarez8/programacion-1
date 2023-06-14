# Escribe una función que determine si dos listas tienen algún elemento en común.

def sumdigits(number):
    stringNumber = str(number)
    total = 0

    for char in stringNumber:
        total += int(char)

    return total

print(sumdigits(123))
print(sumdigits(236))
print(sumdigits(538))

