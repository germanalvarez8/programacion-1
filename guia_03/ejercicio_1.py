#Pedir el ingreso de 10 números. Contar los mayores de 23 y almacenar los que cumplen la condición.  Mostrar la cantidad y los números guardados.

listOfNumbers = []

for i in range(10):
  number = int(input("Numerito: "))
  if number > 23:
    listOfNumbers.append(number)

print(listOfNumbers, len(listOfNumbers))