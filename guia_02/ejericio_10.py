# Dada una lista de nombres y de salarios respectivos, determinar el salario mínimo y mostrar el nombre de la persona que menos gana.

poorest = ""
minimumSalary = 99999999999999999999999
step = 'si'
while step != 'no':
    name = input('Name: ')
    salary = int(input('Salary: '))

    if salary < minimumSalary:
        minimumSalary = salary
        poorest = name

    step = int(input("Add another employee? "))

print(f"The poorest guy is {poorest} with a salary of {minimumSalary}")

