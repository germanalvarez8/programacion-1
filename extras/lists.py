# lastF1Champions = winners = ['Max Verstappen', 'Lewis Hamilton', 'Michael Schumacher', 'Kimi Raikkonen', 'Jenson Button', 'Sebastian Vettel', 'Nico Rosberg', 'Fernando Alonso']

# for champion in lastF1Champions:
#     print(champion)

numbers = []
for i in range(1, 11):
    numbers.append(i * 3)

print (f"the first 10 multiplies of 4 are {numbers}")

# Pop obtiene el elemento en el indice, lo quita del array y lo asigna a la variable
poppedValue = numbers.pop(1)
print(poppedValue, numbers)

# Remove elimina el elemento que coincide con el parametro
poppedValue = numbers.remove(30)
print(poppedValue, numbers)

# Del elimina los elementos del array en el rango de posiciones
del numbers[1:5]
print(numbers)


