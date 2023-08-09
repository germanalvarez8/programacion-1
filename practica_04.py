
# nacidos2008="Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"

nacidos2008 = {
    'male': [
        {'name':'Daniel', 'quantity': 19005},
        {'name':'Ethan', 'quantity': 20216},
        {'name':'Jacob', 'quantity': 22594},
        {'name':'Joshua', 'quantity': 19205},
        {'name':'Michael', 'quantity': 20626}
    ],
    'female': [
        {'name': 'Eva', 'quantity': 17039},
        {'name': 'Emily', 'quantity': 17434},
        {'name': 'Emma', 'quantity': 18813},
        {'name': 'Julia', 'quantity': 18616},
        {'name': 'Olivia', 'quantity': 17081},
    ]
}

nacidos2018 = {
    'male': [
        {'name':'Liam', 'quantity': 19837},
        {'name':'Noah', 'quantity': 18267},
        {'name':'Michael', 'quantity': 14516},
        {'name':'James', 'quantity': 13525},
        {'name':'Oliver', 'quantity': 13389}
    ],
    'female': [
        {'name': 'Emma', 'quantity': 18688},
        {'name': 'Olivia', 'quantity': 17921},
        {'name': 'Ava', 'quantity': 14924},
        {'name': 'Isabella', 'quantity': 14464},
        {'name': 'Sophia', 'quantity': 13928},
    ]
}

# Primer consigna
pos = 1
gender = 'male'

oldchild = nacidos2008['male'][pos - 1]
newchild = nacidos2018['male'][pos - 1]

diffQuantity = 0
if oldchild['quantity'] > newchild['quantity']:
    diffQuantity = oldchild['quantity'] - newchild['quantity']
    maxName = oldchild['name']
    minName = newchild['name']
    maxYear = 2008
    minnorYear = 2018
else:
    diffQuantity = newchild['quantity'] - oldchild['quantity']
    maxName = newchild['name']
    minName = oldchild['name']
    maxYear = 2018
    minnorYear = 2008

print(f"{diffQuantity} nacimientos de {gender} más del {pos} del ranking de {maxYear} {maxName} sobre {minName}")


# Segunda consigna
char = 'J'

names = []
for child in nacidos2008['male']:
    if child['name'][0] == char:
        names.append(child['name'])

for child in nacidos2008['female']:
    if child['name'][0] == char:
        names.append(child['name'])

for child in nacidos2018['male']:
    if child['name'][0] == char:
        names.append(child['name'])

for child in nacidos2018['female']:
    if child['name'][0] == char:
        names.append(child['name'])

print(names)

