# Dada una lista cargada con números enteros, obtener el promedio de ellos. Mostrar por pantalla dicho promedio y los números ingresados que sean mayores que él. Dos funciones: promedio y mayorQue.

def recu (word):
    borde_superior = '╔'
    for i in range(len(word)):
        borde_superior += '═'
    borde_superior += '╗'

    borde_inferior = '╚'
    for i in range(len(word)):
        borde_inferior += '═'
    borde_inferior += '╝'

    print(borde_superior)
    print(f"║{word}║")
    print(borde_inferior)

recu('Hola mundo')
recu('Hermoso recuadro verdad?')