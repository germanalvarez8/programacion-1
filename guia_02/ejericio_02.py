# Preguntar si hay datos para ingresar, en caso afirmativo solicitar un número entero y decir si es negativo o no. Preguntar si repite.

moreData = input('Hay datos para ingresar?')
while moreData != 'no':
    number = int(input('Ingrese un numero: '))

    if number > 0:
        print('Es positivo')
    else:
        print('Es negativo')

    moreData = input('Desea testear otro numero? ')