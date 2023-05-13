# Decir cuántas veces se repite una letra cualquiera, en un texto dado. Por recorrido.

phrase = input("Ingresa una frase: ")
letterToFind = input("Ingresa una letra: ")
count = 0

for letter in phrase:
    if letter == letterToFind:
        count += 1

print(f"The letter {letterToFind} appears {count} times in the phrase '{phrase}'")