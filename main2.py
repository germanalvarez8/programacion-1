from libraries.validations import inputInteger

number = inputInteger("Inserte un numero: ")
anotherNumber = inputInteger("Inserte otro numero: ")

print('Usted insertó los numeros', number, 'y', anotherNumber, 'que sumados dan', number + anotherNumber)
