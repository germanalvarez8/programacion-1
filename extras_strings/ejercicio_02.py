# Dadas dos listas con nombres, una de varones y otra de mujeres, solicitar una letra inicial y mostrar los nombres que comiencen con ella en ambas listas en una string concatenada con guiones.

womens = ['Lisa', 'Ema', 'Juana', 'Ester']
mens = ['Eduardo', 'Pedro']

letterToFind = input('Inserte una letra para buscar nombres: ')

persons = womens + mens

finalList = ''

for names in persons:
    if names[0] == letterToFind:
        if finalList != '':
            finalList += '-'
        finalList += names

print(finalList)