# Pedir nombres y sexo de personas y mostrar el total de mujeres y el nombre de cada una.

totalWomen = 0
names = ""
step = 'yes'
while step != 'no':
    name = input('Add a name: ')
    gender = input('Add gender (m/w): ')

    if gender == 'w':
        totalWomen += 1
        names += name + " "

    step = input("Add another person(yes/no): ")

print(f"You add {totalWomen} womens and his names are {names}")
