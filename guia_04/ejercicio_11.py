# Averiguar qué cantidad de letras tiene la palabra más larga y cual es.

phrase = "Quiero comer manzanas, solamente manzanas."
splited = phrase.split(' ')

maxQuantity = 0
maxQuantityindex = 0

for i in range(len(splited)):
    length = len(splited[i])

    if splited[i].find(',') != -1 or splited[i].find('.') != -1:
        length -= 1

    if length > maxQuantity:
        maxQuantity = length
        maxQuantityindex = i

print(f"The largest word is '{splited[maxQuantityindex]}', with {maxQuantity} letters")