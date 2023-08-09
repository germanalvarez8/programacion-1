# input de fechas (validar formato y devolver año, mes y día como enteros), debe forzar un formato estricto, por ejemplo dd/mm/aaaa.

def validateDay(day, month):
    longMonths = [1, 3, 5, 7, 8, 10, 12]
    shortMonths = [4, 6, 9, 11]

    if month in longMonths:
        limit = 31
    elif month in shortMonths:
        limit = 30
    else:
        limit = 29

    return 1 <= day <= limit

def isValidMonth(month):
    return 1 <= month <= 12

def isValidYear(year):
    return 0 <= year <= 9999

def dateFormat(options):
    dateInString = []
    optionList = options.split('/')

    if not isValidYear(int(optionList[2])) or not isValidMonth(int(optionList[1])) or not validateDay(int(optionList[0]), int(optionList[1])):
        print(f"date {options}")

        return []

    dateInString.append(int(optionList[2]))
    dateInString.append(int(optionList[1]))
    dateInString.append(int(optionList[0]))

    return dateInString

firstDate = dateFormat('22/07/1998')
secondDate = dateFormat('10/12/2000')
thirdDate = dateFormat('40/12/2002')
forthDate = dateFormat('10/20/2002')
fifthDate = dateFormat('10/10/10000')

print(firstDate, secondDate, thirdDate, forthDate, fifthDate)