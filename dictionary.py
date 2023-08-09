# row
dictionary = {
    'nombre': 'Ana',
    'hijos': ['hugo', 'paco', 'luis'],
    'edad': 59,
    'vehiculos': {
        'auto': 1,
        'moto': 2
    }
}

print(dictionary['nombre'], dictionary['vehiculos'])

# Insertion
dictionary['genero'] = 'W'
print(dictionary)

# Delete
dictionary.pop('edad')
del dictionary['genero']

# loops
for key, value in dictionary.items():
    print(key, value)

for key in dictionary.keys():
    print(key)

for value in dictionary.values():
    print(value)
