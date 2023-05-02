# Programa el juego Piedra-Papel-Tijera.
# Una vez funcionando se modifica para que gane el que llegue a 3 triunfos.
# Al principio del programa, se debe colocar la siguiente línea:
# from random import choice

# Luego, para obtener la elección de la computadora se debe usar la siguiente línea:
# computerChoice = choice(['piedra', 'papel', 'tijera'])

# Por último, si quieren probar el resultado de la selección aleatoria (random), prueben con un print:
# print(computerChoice)

from random import choice

matchWinsByUser = 0
matchWinsByComputer = 0

while matchWinsByUser < 3 and matchWinsByComputer < 3:
    computerChoice = choice(['piedra', 'papel', 'tijera'])
    userChoice = input("Inserte su jugada(piedra/papel/tijera): ")

    itsDraw = userChoice == computerChoice
    userWins = (userChoice == 'piedra' and computerChoice == 'tijera') or (userChoice == 'tijera' and computerChoice == 'papel') or (userChoice == 'papel' and computerChoice == 'piedra')
    print(f"Computer choice: {computerChoice}")
    if itsDraw:
        print(f"Its draw, User: {matchWinsByUser}, Computer: {matchWinsByComputer}")
    elif userWins:
        matchWinsByUser += 1
        print(f"User wins, User: {matchWinsByUser}, Computer: {matchWinsByComputer}")
    else:
        matchWinsByComputer += 1
        print(f"Computer wins, User: {matchWinsByUser}, Computer: {matchWinsByComputer}")

if matchWinsByUser == 3:
    winner = "User"
else:
    winner = "Computer"

print("And the winner is")
print(winner, "!!!!")
