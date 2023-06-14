personas = [
    "Josefa Taponales,France(Europe),30-01-2000",
    "Virgie Brach,Argentina(America),04-02-1994",
    "Adeline Quispe,United States(America),18-06-2002",
    "Willy Branscombe,Norway(Europe),21-11-2007",
    "Diane Piffe,France(Europe),07-08-1993",
    "Britta Causbey,Germany(Europe),24-01-2000",
    "Elisabeth Cleeve,Norway(Europe),04-03-1991",
    "Sasha Ivanchenkov,Argentina(America),28-04-2002",
    "Zerk Milsom,Norway(Europe),03-12-1994",
    "Kathryn Backshell,United States(America),04-01-2000"
]

names = []
countrys = []
dateOfBirth = []

for persona in personas:
    splitted = persona.split(',')

    nameSplitted = splitted[0].split()
    names.append(nameSplitted)
    countrys.append(splitted[1])
    dateOfBirth.append(splitted[2])

print('1)')
bornBefore = []
year = int(input('Ingrese año: '))
for i in range(len(names)):
    birthdate = dateOfBirth[i].split('-')
    yearOfBirth = int(birthdate[2])

    if year > yearOfBirth:
        bornBefore.append(names[i][1])

print(f"Los apellidos de las personas nacidas antes del {year} son:")
for lastName in bornBefore:
    print(lastName)

print('2)')
bornInCountry = []
countryToFind = input('Ingrese país: ')
counter = 0
for country in countrys:
    if country.find(countryToFind) != -1:
        counter += 1

print(f"La cantidad de personas de {countryToFind} es {counter}")

print('3)')
aH = 2023
mH = 5
dH = 22

peopleFromEuropeIndexes = []
for i in range(len(countrys)):
    if countrys[i].find('Europe') != -1:
        peopleFromEuropeIndexes.append(i)

youngerName = ''
youngerAge = 100

for i in peopleFromEuropeIndexes:
    birthdate = dateOfBirth[i]
    birthdateSplit = birthdate.split('-')

    age = aH - int(birthdateSplit[2])
    if (int(birthdateSplit[1]) > mH) or (int(birthdateSplit[1]) == mH and int(birthdateSplit[0]) > dH):
        age -= 1

    if age < youngerAge:
        youngerName = names[i][0]
        youngerAge = age

print(f"La persona más joven de Europe es {youngerName}")

