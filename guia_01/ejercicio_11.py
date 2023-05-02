# El costo del pasaje a Córdoba es de $2000. La empresa realiza un descuento de un 40 % sobre el costo del boleto a los niños que tienen entre 5 y 10 años y a los jubilados (mayores de 65). Pedir nombre y edad y mostrar el nombre y el valor final del pasaje.

# name = input('Nombre: ')
# age = int(input('age: '))
# passage_amount = 2000

# itsAChild = age >= 5 or age <= 10
# isRetired = age >= 65

# if (itsAChild or isRetired):
#     passage_amount -= (40 * passage_amount) / 100

# print(f"Para {name} el valor del pasaje es {passage_amount} ya que tiene {age} años")

# -------- esteroides ------

stopWorld = 'si'
while stopWorld != 'no':
    name = input('Nombre: ')
    age = int(input('age: '))
    passage_amount = 2000

    itsAChild = age >= 5 or age <= 10
    isRetired = age >= 65

    if (itsAChild or isRetired):
        passage_amount -= (40 * passage_amount) / 100

    print(f"Para {name} el valor del pasaje es {passage_amount} ya que tiene {age} años")
    stopWorld = input('Desea agregar otro pasajero? ')
