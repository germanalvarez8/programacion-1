# Buscar una palabra y reemplazarla por otra todas las veces que aparezca. Ej.: ‘peras’ en lugar de ‘manzanas’ quedaría 'Quiero comer peras, solamente peras.' Sin usar replace.

phrase = "Quiero comer manzanas, solamente manzanas."
newPhrase = ""
wordToReplace = 'manzanas'
newWord = 'peras'

while phrase.find(wordToReplace) != -1:
    newPhrase = phrase[0:phrase.find(wordToReplace)]
    newPhrase = newPhrase + newWord + phrase[phrase.find(wordToReplace) + len(wordToReplace):]

    phrase = newPhrase

print(phrase)