# Escribe un programa que muestre la hora cada quince minutos, desde las 12 am hasta las 11.45 pm.

hour = 12
minutes = 0
range = 'am'

timestring = "12:00 am"
while timestring != '11:45 pm':
    minutesString = minutes
    if minutes == 0:
        minutesString = "00"

    print (f"{hour}:{minutesString} {range}")
    if minutes + 15 == 60:
        minutes = 0

        if hour == 12:
            hour = 1
        elif hour + 1 == 12:
            range = 'pm'
            hour += 1
        else:
            hour += 1
    else :
        minutes += 15

    minutesString = minutes
    if minutes == 0:
        minutesString = "00"

    timestring = f"{hour}:{minutesString} {range}"

print (f"{hour}:{minutes} {range}")
