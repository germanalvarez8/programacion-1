# Contar la cantidad de palabras.

def wordCounter(phrase):
    counter = 0

    while (phrase.find(' ') != -1) or len(phrase) >= 1:
        counter += 1

        if phrase.find(' ') != -1:
            phrase = phrase[(phrase.find(' ') + 1):]
        else:
            phrase = ''

    return counter

phrase = "Quiero comer manzanas, solamente manzanas."

lenght = wordCounter(phrase)
print(f"'{phrase}' has {lenght} words")