# Ingresar 7 números enteros y en el caso de que sean naturales de una sola cifra mostrar un cartel por cada uno.

for i in range(7):
    number = int(input('Add a number: '))

    if number > 0 and number < 10:
        print(f"{number} is natural and have 1 digit")
