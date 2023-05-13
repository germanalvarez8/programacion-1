# Cargar en listas los nombres y fechas de nacimiento de varias personas, luego recorrerlo y mostrar los nombres de los mayores de edad.

aH = 2023
mH = 5
dH = 4

nameList = []
birthdayList = []

keep = 'yes'
while keep != 'no':
    name = input('Name: ')
    birthday = input('Birthday: ')

    nameList.append(name)
    birthdayList.append(birthday)

    keep = input('Keep?')

# test = '22/07/1998'
# print(test.split('/'))
maxRain = 0
legalPeople = []
for i in range(len(nameList)):
    ageSplit = birthdayList[i].split('/')

    age = aH - int(ageSplit[2])
    if (int(ageSplit[1]) > mH) or (int(ageSplit[1]) == mH and int(ageSplit[0]) > dH):
        age -= 1

    if age >= 18:
        legalPeople.append(nameList[i])

print(f"{legalPeople} are legal people")
