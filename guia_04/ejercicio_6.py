# Buscar una palabra completa en un texto y contar cuántas veces está.

phrase = "Quiero comer manzanas, solamente manzanas."
word = 'manzanas'
counter = 0

while phrase.find(word) != -1:
    counter += 1
    phrase = phrase[phrase.find(word) + len(word):]

print(counter)