# Almacenar en dos  listas paralelas, nombres y sexos de 8 personas. Al finalizar, recorrerlas y mostrar los nombres de las mujeres. Dos funciones: carga y mostrarMujeres

def load():
    personData = []
    persons = ['Mario', 'Kara', 'Sid', 'Lucy', 'Susan', 'Maxim', 'Miles', 'Lottie']
    gender = ['m', 'f', 'm', 'f', 'f', 'm', 'm', 'f']

    personData.append(persons)
    personData.append(gender)

    return personData

def getWomens(names, genders):
    womens = []
    for i in range(len(names)):
        if genders[i] == 'f':
            womens.append(names[i])

    return womens

personList = load()
womens = getWomens(personList[0], personList[1])

print(f"Las mujeres son {womens}")