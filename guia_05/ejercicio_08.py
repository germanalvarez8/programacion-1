# Ingresar nombres, luego buscar un nombre y de encontrarlo decir en qué posición está.


def load():
    personList = []
    add = 's'
    while add != 'n':
        name = input('Inserta un nombre: ')
        personList.append(name)

        add = input('Desea ingresar otro (s/n)? ')

    return personList

def findPerson(names, name):
    result = []
    for i in range(len(names)):
        if names[i] == name:
            result.append(names[i])
            result.append(i + 1)

    return result

persons = load()
name = input('Ingrese un nombre que desee encontrar: ')
inList = findPerson(persons, name)

print(persons)
if len(inList) > 0:
    print(f"{inList[0]} Se encuentra en la posicion {inList[1]}")
