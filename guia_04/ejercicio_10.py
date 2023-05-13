# Averiguar qué cantidad de letras tiene la palabra más larga y cual es.

phrase = "Quiero comer manzanas, solamente manzanas."

splited = phrase.split(' ')
quantityList = phrase.split(' ')

for i in range(len(splited)):
    lenght = len(splited[i])

    if splited[i].find(',') != -1 or splited[i].find('.') != -1:
        lenght -= 1
    quantityList[i] = lenght

maxQuantity = 0
maxQuantityindex = 0
for i in range(len(quantityList)):
    if quantityList[i] > maxQuantity:
        maxQuantity = quantityList[i]
        maxQuantityindex = i

print(maxQuantity, splited[maxQuantityindex])