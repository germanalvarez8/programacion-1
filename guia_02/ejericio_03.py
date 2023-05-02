# Pedir el ingreso de 5 números. Contar los mayores de 23. Mostrar el resultado.

total = 0
for i in range(5):
    number = int(input('Ingrese un numero: '))

    if number > 23:
        total += 1

print(f"Ingresó {total} numeros mayores a 23")