# Eliminar todos los valores iguales de una lista. Previamente, solicitar el valor y si no está, mostrar un cartel diciendo que no lo ha encontrado.

elementList = []

keep = 'yes'
while keep != 'no':
    element = input('element: ')
    elementList.append(element)

    keep = input('Keep?')

nameToFind = input('Insert element to delete: ')

if nameToFind in elementList:
    while nameToFind in elementList:
        elementList.remove(nameToFind)
else:
    print(f"{nameToFind} Not found {elementList}")

print(f"{nameToFind} found and delete: {elementList}")
