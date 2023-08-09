# Implemente una función que calcule el promedio de una cantidad variable de números. Se tiene que poder pasar un argumento que descarte los valores negativos para sacar dicho promedio.

def promedio(*args, sinNegativos=False):
    total = 0
    negtiveNumber = 0

    for number in args:
        if sinNegativos:
            if number > 0:
                total += number
            else:
                negtiveNumber += 1
        else:
            total += number

    return total/(len(args) - negtiveNumber)

# Ejemplo de uso de la función:
print(promedio(121,65,-88,34,-9,27)) # 150/6=25
print(promedio(121,65,-88,34,-9,27, sinNegativos=True)) # 247/4=61.75
print(promedio(2,4)) # 3
