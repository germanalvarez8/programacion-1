# Tomar dos enteros y sumarlos

def inputInteger(message):
    valid = False

    while not valid:
        number = input(message)
        try:
            number = int(number)
            valid = True
        except:
            print('a number, Stupid')
    return number
