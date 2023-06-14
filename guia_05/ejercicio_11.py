# Cargar en listas los nombres y fechas de nacimiento de varias personas, luego recorrerlo y mostrar los nombres de los mayores de edad. Funciones de carga y cálculo de edad.

def load():
    return [['Ana', 'Juan', 'María', 'Carlos', 'Laura', 'Pedro', 'Sofía', 'Andrés'], ['19/05/2010', '02/02/2004', '24/09/2017', '27/01/2012', '22/09/1969', '12/11/1963', '12/01/1999', '10/06/2009']]

def getAge(ageInString):
    aH = 2023
    mH = 5
    dH = 8

    ageSplit = ageInString.split('/')

    age = aH - int(ageSplit[2])
    if (int(ageSplit[1]) > mH) or (int(ageSplit[1]) == mH and int(ageSplit[0]) > dH):
        age -= 1

    return age

nameData = load()

bigBoys = []
for i in range(len(nameData[0])):
    age = getAge(nameData[1][i])

    if age >= 18:
        bigBoys.append(nameData[0][i])

print(f"{bigBoys}")
