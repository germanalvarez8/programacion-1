# Transformar esta cadena a dos listas paralelas de nombres y sueldos(sin el signo pesos): “Juan$120000,Ana$250000,Luis$76500,Vilma$98700”. Mostrar las listas resultantes completas.

initialString = "Juan$120000,Ana$250000,Luis$76500,Vilma$98700"
splittedList = initialString.split(',')

names = []
salaries = []

for splitted in splittedList:
    nameAndSalary = splitted.split('$')
    names.append(nameAndSalary[0])
    salaries.append(nameAndSalary[1])

print(names, salaries)