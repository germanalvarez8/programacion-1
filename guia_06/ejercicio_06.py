# Validar un número con la posibilidad de tener un rango (reutilizar inputInt/inputFloat o bien inputNumber si prefieren usar una sola función para validar ambos tipos de datos)

from functions.validations import inputInteger

edad = inputInteger('Ingrese su edad: ')
print(f'Tenés {edad} años') # f-string

n = inputInteger('Ingrese un entero entre 3 y 7: ', 3, 7)
m = inputInteger('Cualquier número entero: ')
maxito = inputInteger('ingrese un entero menor a 1000: ', maxi=999)
minito = inputInteger('ingrese un entero mayor a mil: ', 1001)

print(n, m, maxito, minito)
