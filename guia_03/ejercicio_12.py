# Pedir nombres y sexo de personas y mostrar al final el total de mujeres y el nombre de cada una.

listOfNames = []
listOfGender = []

name = input("Name: ")
gender = input("Gender: ")

keep = 'yes'
while keep != 'no':
    name = input("Name: ")
    gender = input("Gender: ")

    listOfNames.append(name)
    listOfGender.append(gender)

    keep = input('Keep?')

girlList = []
for index in range(len(listOfNames)):
    if listOfGender[index] == 'w':
        girlList.append(listOfNames[index])


print(len(girlList), girlList)
