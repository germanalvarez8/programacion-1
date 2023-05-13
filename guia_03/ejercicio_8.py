# Cargar una lista con números. Invertir los elementos sin usar otra lista

inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 0
j = len(inputArray) - 1

while i < j:
    aux = inputArray[i]
    inputArray[i] = inputArray[j]
    inputArray[j] = aux

    i += 1
    j -= 1

print(inputArray)
