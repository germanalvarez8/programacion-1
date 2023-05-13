#  Ingresar nombres en una lista sin repetir, luego buscar un nombre y de encontrarlo decir en qué posición está.

nameList = []

keep = 'yes'
while keep != 'no':
    name = input('Name: ')

    isInArray = name not in nameList
    if isInArray:
        nameList.append(name)
    keep = input('Keep?')

nameToFind = input('Insert name to find: ')
found = False
for index in range(len(nameList)):
    if nameToFind == nameList[index]:
        print(f"Está en la posición {index + 1}")
        found = True

if not found:
    print(f"{nameToFind} Not found")
