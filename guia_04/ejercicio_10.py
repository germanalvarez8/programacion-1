# Determinar cuál es la vocal que aparece con mayor frecuencia.

phrase = "Quiero comer manzanas, solamente manzanas."

vowels = ['a', 'e', 'i', 'o', 'u']
vowelsQuantity = [0, 0, 0, 0, 0]

for letter in phrase:
    if letter == 'a':
        vowelsQuantity[0] += 1
    elif letter == 'e':
        vowelsQuantity[1] += 1
    elif letter == 'i':
        vowelsQuantity[2] += 1
    elif letter == 'o':
        vowelsQuantity[3] += 1
    elif letter == 'u':
        vowelsQuantity[4] += 1

maxQuantity = 0
maxQuantityindex = 0
for i in range(len(vowels)):
    if vowelsQuantity[i] > maxQuantity:
        maxQuantity = vowelsQuantity[i]
        maxQuantityindex = i

print(f"The most used vowel is {vowels[maxQuantityindex]}, with {maxQuantity} aparitions")