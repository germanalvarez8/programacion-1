# Contar la cantidad de letras (no incluir los separadores).

phrase = "Quiero comer manzanas, solamente manzanas."
count = 0

for letter in phrase:
    if letter != ' ':
        count += 1

print(count, len(phrase))