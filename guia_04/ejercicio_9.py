# Contar la cantidad de palabras.

phrase = "Quiero comer manzanas, solamente manzanas."
newPhrase = phrase
counter = 0

while (phrase.find(' ') != -1) or len(phrase) >= 1:
    counter += 1

    if phrase.find(' ') != -1:
        phrase = phrase[(phrase.find(' ') + 1):]
    else:
        phrase = ''

print(f"The phrase '{newPhrase}' has {counter} words")