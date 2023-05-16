# Pedir el ingreso de un nombre completo en la forma <nombre> <apellido> (ejemplo: Juan Pérez) y mostrarlo invertido y con coma <apellido>,<nombre> (ejemplo: Perez, Juan)

phrase = input('Insert <name> <lastName>: ')
splited = phrase.split(' ')

print(f"{splited[1]}, {splited[0]}")