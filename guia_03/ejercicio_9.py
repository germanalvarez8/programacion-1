# Cargar en dos listas paralelas nombres y sueldos. Luego mostrar los nombres de las personas que ganan más de $185000.

nameList = []
salaryList = []

keep = 'yes'
while keep != 'no':
    name = input('Name: ')
    salary = int(input('Salary: '))

    nameList.append(name)
    salaryList.append(salary)

    keep = input('Keep?')

richPeople = []
for i in range(len(nameList)):
    if salaryList[i] > 18500:
        richPeople.append(nameList[i])

print(f"From {nameList} only {richPeople} are not poor")
