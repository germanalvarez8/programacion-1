# Buscar una palabra y reemplazarla por otra todas las veces que aparezca.

def replaceStringInPhrase(phrase, wordToReplace, newWord):
    newPhrase = ""

    while phrase.find(wordToReplace) != -1:
        newPhrase = phrase[0:phrase.find(wordToReplace)]
        newPhrase = newPhrase + newWord + phrase[phrase.find(wordToReplace) + len(wordToReplace):]

        phrase = newPhrase

    return newPhrase

wordToReplace = 'manzanas'
newWord = 'perros'
phrase = "Quiero comer manzanas, solamente manzanas."

newPhrase = replaceStringInPhrase(phrase, wordToReplace, newWord)
print(newPhrase)