# 4 formas de lectura

filePath = 'archivos/files/chotito.txt'
# 1. read()
# with open(filePath) as choty:
#     print(choty.tell()) # posición de lectura
#     todo = choty.read() # lee todo el archivo
#     # y lo guarda como una string
#     print(choty.tell()) 
#     choty.seek(3) # mueve el puntero de lectura
#     cuatroCars = choty.read(4) # lea 4 caracteres
#     print(cuatroCars)
#     print(todo)

# # 2. readline()
# with open(filePath) as choty:
#     print(choty.readline(5))

# 3. readlines()
with open(filePath) as choty:
    lineas = choty.readlines()
    print(lineas)

# # 4. recorrido con for
# with open(filePath) as choty:
#     for linea in choty:
#         print(linea, end='')
