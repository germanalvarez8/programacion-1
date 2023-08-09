# Tomar dos enteros y sumarlos
def inputStr(welcomeMessage, min=0, maxi=30):
    validInput = False
    while validInput == False:
        inputText = input(welcomeMessage)
        if len(inputText) >= min and len(inputText) <= maxi:
            validInput = True
        else:
            print(f"The pass must content between {min} and {maxi} characters, you put {len(inputText)}")

    return inputText

def inputInteger(message, mini=-10**308, maxi=10**308):
    valid = False

    while not valid:
        try:
            number = int(input(message))
            if mini <= number <= maxi:
                valid = True
            else:
                print('fuera de rango')
        except:
            print('a number, Stupid')
    return number
