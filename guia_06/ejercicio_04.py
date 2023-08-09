# inputStr: input de strings (validar largo por mínimo y/o máximo).

def inputStr(welcomeMessage, min=0, maxi=30):
    validInput = False
    while validInput == False:
        inputText = input(welcomeMessage)
        if len(inputText) >= min and len(inputText) <= maxi:
            validInput = True
        else:
            print(f"The pass must content between {min} and {maxi} characters, you put {len(inputText)}")

    return inputText

# Ejemplo de uso de la función:
# password0 = inputStr('Password (entre 5 y 8 caracteres): ', 5, 8)
# password1 = inputStr('Password (al menos 4): ', 4)
# password2 = inputStr('Password (a lo sumo 5): ', maxi=5)
# password3 = inputStr('Password (sin rango): ')
