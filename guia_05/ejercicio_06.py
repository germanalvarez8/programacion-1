# Definir una lista de 10 posiciones con letras. Contar las vocales y mostrar el total.

def getCharacterList():
    return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def vowelsCounter(characterList):
    counter = 0

    for char in characterList:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            counter += 1

    return counter

characterList = getCharacterList()

vowelsQuantity = vowelsCounter(characterList)
print(f"Las vocales en la lista {characterList} es {vowelsQuantity}")