# Primer for: Almacenar en dos listas paralelas, nombres y sexos de 8 personas. Segundo for: Recorrerlas y guardar los nombres de las mujeres en una nueva lista. Mostrar los elementos de la lista resultante.

listOfNames = []
listOfGender = []

name = input("Name: ")
gender = input("Gender: ")

for i in range(8):
    listOfNames.append(name)
    listOfGender.append(gender)

    name = input("Name: ")
    gender = input("Gender: ")

girlList = []
for index in range(len(listOfNames)):
    if listOfGender[index] == 'w':
        girlList.append(listOfNames[index])


print(len(girlList), girlList)
