# Dada una lista cargada con números enteros, obtener el promedio de ellos. Mostrar por pantalla dicho promedio y los números ingresados que sean mayores que él. Dos funciones: promedio y mayorQue.


def promedio(numberList):
    # personList = []
    total = 0

    for number in numberList:
        total += number

    return int(total / len(numberList))

def mayorQue(numberList, baseNumber):
    greater = []
    for number in numberList:
        if baseNumber < number:
            greater.append(number)

    return greater

numbers = [10, 28, 9, 21, 20, 27, 8, 12, 26, 14]
average = promedio(numbers)

greater = mayorQue(numbers, average)

print(f"De la lista {numbers} el promedio es {average} y los mayores que el promedio son {greater}")
