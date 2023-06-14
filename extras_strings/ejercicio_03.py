# Tengo una lista con direcciones completas (calle y número). Mostrar cada calle y la cantidad de veces que se repite.

directions = ['Mitre 1234', '9 de Julio 345', 'Alvear 999', '9 de Julio 11']
streets = []

for direction in directions:
    parts = direction.split(' ')
    streetNameArray = parts[:-1]

    streetName = ''
    for part in streetNameArray:
        if streetName != '':
            streetName += ' '
        streetName += part
    streets.append(streetName)

streetDistincts = []
repeats = []

for street in streets:
    if street in streetDistincts:
        index = streets.index(street)
        repeats[index] += 1
    else:
        streetDistincts.append(street)
        repeats.append(1)

for i in range(len(streetDistincts)):
    print(streetDistincts[i], repeats[i])