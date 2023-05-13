# Dada una lista con números, crear otra con los cuadrados de esos valores.

numberList = []

response = 'si'
while response != 'no':
    number = int(input('Number: '))
    numberList.append(number)

    response = input('Another number? ')

squadList = []
for i in range(len(numberList)):
    squadList.append(numberList[i] * numberList[i])

print(squadList)
