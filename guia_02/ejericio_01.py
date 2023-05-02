# Mostrar por pantalla una lista de 10 números enteros consecutivos, comenzando con un número ingresado por teclado.

start = int(input('Ingrese un numero: '))

print("Los 9 numeros consecutivos a tu numero son")
for element in range(start, start + 10):
    print(element)