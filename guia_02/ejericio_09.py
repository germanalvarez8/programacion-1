# Dada una serie de números reales positivos, determinar el valor máximo y mostrarlo al final. Se deberá ir preguntando si hay más números para ingresar.

maxNumber = 0
step = 1
while step != 0:
    number = int(input('Number: '))

    if number > maxNumber:
        maxNumber = number

    step = int(input("Desea agregar otro numero? "))

print(f"The maximum number is {maxNumber}")

