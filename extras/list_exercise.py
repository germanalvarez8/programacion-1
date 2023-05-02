#dada una lista de numeros obtener:
# 1) obtener el promedio
# 2) obtener los valores mayores al promedio

totalNumber = 0
average = 0
upToAverage = []
initialList = []

inputNumber = input("Insert a value: ")
while inputNumber != 'no':
    if inputNumber.isnumeric():
        initialList.append(int(inputNumber))
        print('value added')
    elif inputNumber != 'no':
        print('Insert numeric values, stupid')

    inputNumber = input('Insert another value? ')

for i in initialList:
    totalNumber += i

average = totalNumber / len(initialList)

for i in initialList:
    if i > average:
        upToAverage.append(i)

print(f"the average is {average} and the numbers up to average are {upToAverage}")
