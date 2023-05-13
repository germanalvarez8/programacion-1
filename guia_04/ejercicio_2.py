# Transformar la cadena "Curso de Python" en la cadena "Curso de Programación en Python". Cortar la cadena original, agregarle el literal "Programación en" y concatenar.

phrase = "Curso de Python"
intrude = "Programación en"

pos = phrase.find('Python')
finalPhrase = phrase[0:pos] + intrude + phrase[pos -1:]
print(finalPhrase)