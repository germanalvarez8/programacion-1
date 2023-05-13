# Cargar letras en una lista (while). Contar las vocales (for). Mostrar el total.

listOfCharacters = []
character = ''
newCharacter = input("Character: ")

while character != 'no':
    listOfCharacters.append(newCharacter)

    newCharacter = input("Character: ")
    character = newCharacter

vowelsList = []
for char in listOfCharacters:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vowelsList.append(char)


print(listOfCharacters, vowelsList, len(vowelsList))
