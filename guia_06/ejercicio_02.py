# Escribe una función que cuente la cantidad de ocurrencias de una subcadena en una cadena de texto, permitiendo especificar si se debe realizar una búsqueda sin distinguir mayúsculas y minúsculas. Se pueden usar los métodos lower() y upper() del objeto string. Por ejemplo, si tengo la cadena:
# s = 'River Plate', al aplicar s.lower() obtengo 'river plate' y si aplico s.upper(), obtengo 'RIVER PLATE'.

def contarSubCadena(phrase, substring, ignorarMayusculas=True):
    stringToFind = substring
    counter = 0

    if ignorarMayusculas:
        stringToFind = substring.lower()
        phrase = phrase.lower()

    while phrase.find(stringToFind) != -1:
        counter += 1
        phrase = phrase[phrase.find(stringToFind) + len(stringToFind):]

    return counter

# Ejemplo de uso de la función:
frase = 'Desde niña me encanta mirar la luna, por eso es que le puse de nombre Luna a mi hija'
print(contarSubCadena(frase, 'luna')) # 2
print(contarSubCadena(frase, 'luna', ignorarMayusculas=False)) # 1