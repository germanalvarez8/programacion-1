# Guardar en una lista los números pares mayores que 0 y menores que 31.

pairList = []

for i in range(32):
    if i % 2 == 0:
        pairList.append(i)

print(pairList)
