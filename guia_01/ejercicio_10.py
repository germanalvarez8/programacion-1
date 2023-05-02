# Preguntar nombre, carrera en la que se inscribe y ciudad donde vive un ingresante al Instituto. Los estudiantes de la carrera de Electromecánica y que no viven en Río Cuarto tendrán un 15% de descuento en la cuota que es de $7000. Mostrar nombre, ciudad, carrera y monto final de la cuota.
# name = input('Nombre: ')
# career = input('Carrera: ')
# city = input('Ciudad de residencia: ')
# amount = 7000

# if (career == 'Electromecanica' and (city != 'Rio cuarto')):
#     amount -= (15 * amount) / 100

# print(f"Para {name} que vive en {city} y estudia {career} el valor de la cuota es de {amount}")

# ------- refactor --------
studentsQuantity = int(input("Cuantos estudiantes desea inscribir? "))

for student in range(studentsQuantity):
    name = input('Nombre: ')
    career = input('Carrera: ')
    city = input('Ciudad de residencia: ')
    amount = 7000

    if (career == 'Electromecanica' and (city != 'Rio cuarto')):
        amount -= (15 * amount) / 100

    print(f"Para {name} que vive en {city} y estudia {career} el valor de la cuota es de {amount}")