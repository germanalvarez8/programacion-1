# Pedir dos nombres y edades respectivas y luego construir una sola cadena con un texto que muestre el nombre del mayor y cuanto le lleva al menor. (Ejemplo:  entrada -> 'Juan' 30 'Pedro' 23 / salida -> 'Juan le lleva 7 años a Pedro')

nameList = []
ageList = []

for i in range(2):
    nameAndAge = input("Insert name and age: ")
    nameAndAgeSplited = nameAndAge.split()

    nameList.append(nameAndAgeSplited[0])
    ageList.append(int(nameAndAgeSplited[1]))

if ageList[0] > ageList[1]:
    ageDiff = ageList[0] - ageList[1]
    message = f"{nameList[0]} is {ageDiff} years old bigger than {nameList[1]}"
elif ageList[0] < ageList[1]:
    ageDiff = ageList[1] - ageList[0]
    message = f"{nameList[1]} is {ageDiff} years old bigger than {nameList[0]}"
else:
    message = f"{nameList[0]} and {nameList[1]} has the same age"

print(message)