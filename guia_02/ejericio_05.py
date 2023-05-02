# Pedir los montos de sueldos de los empleados de una empresa hasta que no haya más y mostrar el total.

moreEmployees = 'si'
total = 0
employeesQuantity = 0
while moreEmployees == 'si':
    amount = int(input('Ingrese un monto: '))
    total += amount
    employeesQuantity += 1

    moreEmployees = input('Desea ingresar otro sueldo? ')

print(f"Ingresó {employeesQuantity} empleados, que y sus sueldos suman en total ${total}")