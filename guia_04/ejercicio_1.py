# Eliminar el plural en esta frase: “Real Madrid gana las copas.” Recorrer y quitar las eses. Sugerencia: Usar otra string.

phrase = "Real Madrid gana las copas."

# while phrase.find('s') != -1:
#     index = phrase.find('s')
#     firstSlice = phrase[0:index]
#     secondSlice = phrase[index + 1:len(phrase)]

#     phrase = firstSlice + secondSlice

newPhrase = ""
for letter in range(len(phrase)):
    if phrase[letter] == 's':
        newPhrase = newPhrase + ''
    else:
        newPhrase = newPhrase + phrase[letter]

print(newPhrase)
