# Preguntar cuántas personas se van a cargar y luego solicitar sus edades, mostrando al final la edad promedio.

peopleToAdd = input("cuantas personas va a cargar? ")
totalAge = 0
for i in range(peopleToAdd):
    age = int(input('age? '))
    totalAge += age

averageAge = round(totalAge / peopleToAdd)
print(f"La edad promedio de las {peopleToAdd} ingresadas es de {averageAge}")
