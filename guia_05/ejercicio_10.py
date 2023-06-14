# Ingresar la lluvia caída en milímetros para cada día de la semana. Mostrar al final el total de lluvia caída y el nombre del día que más llovió.

def maxRainDayIndex(rainQuantity):
    maxRainIndex = 0
    maxRain = 0
    for i in range(len(rainQuantity)):
        if rainQuantity[i] > maxRain:
            maxRainIndex = i
            maxRain = rainQuantity[i]

    return maxRainIndex

numbers = [10, 28, 9, 21, 20, 27, 8]
daysOfWeek = ['Lun', 'Mar', 'Mier', 'Jue', 'Vier', 'Sab', 'Dom']

index = maxRainDayIndex(numbers)

print(f"El dia de mas lluvia fue {daysOfWeek[index]}, con {numbers[index]}mm")
