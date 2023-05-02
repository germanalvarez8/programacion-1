totalSeconds = int(input('Ingrese periodo de tiempo: '))

days = totalSeconds // 86400
seconds = totalSeconds % 86400
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

print(f"{totalSeconds} segundos son {days} días, {hours} horas, {minutes} minutos y {seconds} segundos")