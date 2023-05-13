# Pasar una palabra a mayúsculas cambiando los caracteres uno por uno usando la tabla ASCII de referencia (googlear la tabla y las funciones de conversión en Python).

# phrase = input("Ingresa una frase: ")
phrase = "Ingresa una Frase: "
finalPhrase = ""

for letter in phrase:
    concatLetter = letter
    if not letter.isupper() and letter != ' ':
        asciiLetter = ord(letter)
        asciiLetter -= 32

        concatLetter = chr(asciiLetter)

    finalPhrase = finalPhrase + concatLetter

print(finalPhrase)