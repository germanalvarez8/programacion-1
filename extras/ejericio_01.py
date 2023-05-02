# Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
#  - Múltiplos de 3 por la palabra "fizz".
#  - Múltiplos de 5 por la palabra "buzz".
#  - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

daysOfWeek = 7
totalMilimeters = 0
daysOfRain = ""
# step = 'yes'
for index in range(1, 101):
    isMultipleOf3 = index % 3 == 0
    isMultipleOf5 = index % 5 == 0

    if isMultipleOf3 and isMultipleOf5:
        print ("fizzbuzz")
    else:
        if isMultipleOf3:
            print('fizz')
        elif isMultipleOf5:
            print('buzz')
        else:
            print(index)
