# Ingresar la lluvia caída en milímetros para cada día de la semana. Mostrar al final el total de lluvia caída y el nombre del día que más llovió.

daysOfWeey = ['Lun', 'Mar', 'Mier', 'Jue', 'Vier', 'Sab', 'Dom']
rainInDay = []

maxRain = 0
for i in range(len(daysOfWeey)):
    rain = int(input('Add rain in milimeters: '))
    rainInDay.append(rain)

    if rain > maxRain:
        maxRain = rain
        maxDayRainIndex = i

print(f"In {daysOfWeey[maxDayRainIndex]} rain {maxRain}")
