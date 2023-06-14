# Averiguar qué cantidad de letras tiene la palabra más larga.  Para ello, primero cargar cada palabra en una lista y luego obtener la solicitada. Usar dos funciones.

def countCharacters(phrase):
    count = 0

    for letter in phrase:
        if letter != ' ' and letter != ',' and letter != '.':
            count += 1

    return count

def largestWord(words):
    largest = ""
    for word in words:
        if len(word) > len(largest):
            largest = word

    return largest

phrase = "Quiero comer manzanas, solamente manzanas."
splitted = phrase.split()

cleanWords = []
for word in splitted:
    if word.find(',') != -1 or word.find('.') != -1:
        cleanWords.append(word[0:(len(word) - 1)])
    else:
        cleanWords.append(word)

longWord = largestWord(cleanWords)

print(longWord, countCharacters(longWord))