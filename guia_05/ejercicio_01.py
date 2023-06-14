# Cuántas veces se repite una letra cualquiera. Parámetros: letra, cadena.

def checkLetter(letter, string):
    apparitions = 0
    for stringLetter in string:
        if stringLetter == letter:
            apparitions += 1

    return apparitions

phrase = "Quiero comer manzanas, solamente manzanas."
letter = 'm'

letterQuantity = checkLetter(letter, phrase)

print(f"The phrase '{phrase}' has {letterQuantity} characters '{letter}'")