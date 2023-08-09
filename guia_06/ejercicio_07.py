# input con opciones

from functions.validations import inputInteger

def inputChoice(options, question='Elija una opción'):
    question += ': '
    optionList = options.split('/')
    for i in range(len(optionList)):
        print(f'{i+1}) {optionList[i]}')
    selected = inputInteger(question, 1, len(optionList))
    return optionList[selected-1]

q = inputChoice('si/no/a veces')
print(q)
r = inputChoice('rojo/verde/blanco/negro', 'Elija un color')
print(r)