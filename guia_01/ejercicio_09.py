number = int(input('un numero: '))

isPossitive = number > 0
hasTwoDigits = (number < -9 & number > -100) | (number > 9 & number < 100)

if (isPossitive and hasTwoDigits):
    print(number, 'Es positivo y con dos digitos')
elif (isPossitive and (not hasTwoDigits)):
    print(number, 'Es positivo pero no tiene dos digitos')
elif ((not isPossitive) and hasTwoDigits):
    print(number, 'No es positivo pero tiene dos digitos')
elif ((not isPossitive) and (not hasTwoDigits)):
    print(number, 'No cumple nada')