# 2 formas de escritura

filePath = 'archivos/files/chotito.txt'

# 1. write()
# 'w' escribe de cero
# with open(filePath, 'w') as pedorry:
#     pedorry.write('cualquier gilada\n')

# 'a' agrega al fondo del archivo
# with open(filePath, 'a') as pedorry:
#     # write() escribe una string
#     pedorry.write('segunda gilada')
#     pedorry.write('\nTercer')


# # 2. writelines() escribe una lista
lista = ['Josefa\n', 'Antonio\n']
with open(filePath, 'w') as pedorry:
    pedorry.writelines(lista)
