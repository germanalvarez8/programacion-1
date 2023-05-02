# Ingresar la lluvia caída en milímetros para cada día de la semana. Mostrar al final el total de lluvia caída y la cantidad de días que no llovió.

daysOfWeek = 7
totalMilimeters = 0
daysOfRain = ""
# step = 'yes'
for day in range(daysOfWeek):
    dayName = input('Add name of day: ')
    milimetersOfRain = int(input('Insert milimeters of rain: '))

    if milimetersOfRain > 0:
        totalMilimeters += milimetersOfRain
        daysOfRain += dayName + " "

print(f"Total of rain: {totalMilimeters} mm, but no in the days {daysOfRain}")
