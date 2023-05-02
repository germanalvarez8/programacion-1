# Calcular el sueldo a cobrar teniendo en cuenta que  los empleados que no han faltado y  cuya antigüedad es superior a 5 años, tienen un adicional del 30% sobre el sueldo básico ($47.000). Pedir la cantidad de días no trabajados y año de ingreso en la empresa.

# name = input('Nombre: ')
# daysOff = int(input('Days off: '))
# yearOfOnboard = int(input('Year of onboard: '))
# basicPayment = 47000

# hasSeniority = (2023 - yearOfOnboard) > 5
# hasDaysOff = daysOff != 0

# if (hasSeniority and (not hasDaysOff)):
#     basicPayment += (30 * basicPayment) / 100

# print(f"Para {name} el sueldo correspondiente es de {basicPayment} ya que tiene {yearOfOnboard} años de antiguedad y {daysOff} ausencias")

# -----------------------

# for employees in range(3):
#     name = input('Nombre: ')
#     daysOff = int(input('Days off: '))
#     yearOfOnboard = int(input('Year of onboard: '))
#     basicPayment = 47000

#     hasSeniority = (2023 - yearOfOnboard) > 5
#     hasDaysOff = daysOff != 0

#     if (hasSeniority and (not hasDaysOff)):
#         basicPayment += (30 * basicPayment) / 100

#     print(f"Para {name} el sueldo correspondiente es de {basicPayment} ya que tiene {yearOfOnboard} años de antiguedad y {daysOff} ausencias")

# -----------------------

# import json

# array = []
# for employees in range(3):
#     name = input('Nombre: ')
#     daysOff = int(input('Days off: '))
#     yearOfOnboard = int(input('Year of onboard: '))
#     basicPayment = 47000

#     hasSeniority = (2023 - yearOfOnboard) > 5
#     hasDaysOff = daysOff != 0

#     if (hasSeniority and (not hasDaysOff)):
#         basicPayment += (30 * basicPayment) / 100

#     x = {
#         "name": name,
#         "daysOff": daysOff,
#         "yearOfOnboard": yearOfOnboard,
#         "payment": basicPayment
#     }

#     array.append(x)

# for employee in array:
#     print(f"Para {employee['name']} el sueldo correspondiente es de {employee['payment']} ya que tiene {employee['yearOfOnboard']} años de antiguedad y {employee['daysOff']} ausencias")