# Ingresar autos y sus precios y contar cuantos valen entre $3.460.000 y $12.850.000. Terminar la carga cuando el valor ingresado sea 0.

inRangeCars = 0
step = 1
while step != 0:
    carName = input('Nombre del vehiculo: ')
    carValue = int(input('Precio: '))

    if carValue >= 3_460_000 and carValue <= 12_850_000:
        inRangeCars += 1

    step = int(input('Desea ingresar otro auto? (1/0)'))
print(f"{inRangeCars} se encuentran entre $3.460.000 y $12.850.000")

