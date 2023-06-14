# Contar la cantidad de letras (mayúsculas, minúsculas, acentuadas, eñes).

def countCharacters(phrase):
    count = 0

    for letter in phrase:
        if letter != ' ' and letter != ',' and letter != '.':
            count += 1

    return count

phrase = "Quiero comer manzanas, solamente manzanas."

lenght = countCharacters(phrase)
print(f"'{phrase}' has {lenght} letters")