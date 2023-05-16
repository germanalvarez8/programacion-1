# Mostrar el valor doble del número de dos cifras (que es el único número) encontrado en la cadena. Ej.: 'Juan tiene 25 años' mostraría el número 50, ‘El dólar va a llegar este mes a 500 pesos casi seguro’,  mostraría 1000

phrase = "Quiero comer 30 manzanas, solamente manzanas."

splited = phrase.split(' ')

number = 0
for word in splited:
    if word.isdigit():
        number = int(word) * 2

print(number)