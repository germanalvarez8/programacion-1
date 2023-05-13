# Recibir por teclado una cadena de números e insertar  un punto cada 3 dígitos como divisorio de miles. Ej.  1234567890 debería devolver 1.234.567.890

phrase = "1234567890000000000"
reversed = phrase[::-1]

newPhrase = ""

index = len(phrase) - 1

for letter in range(len(reversed)):
    if letter > 0 and letter % 3 == 0:
        newPhrase = newPhrase + '.'
    newPhrase = newPhrase + reversed[letter]

print(newPhrase[::-1])
