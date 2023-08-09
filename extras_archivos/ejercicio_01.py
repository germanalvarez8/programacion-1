def insertContent(file, position, insertion):
    with open(file) as readFile:
        content = readFile.read()
        print(content)

    with open(file, 'w') as fileToWrite:
        finalContent = content[:position] + insertion + content[position:]
        print(finalContent)
        fileToWrite.write(finalContent)

def insertarFila(file, position, insertion):
    with open(file) as readFile:
        content = readFile.readlines()
        print(content)

    head = content[:position]
    tail = content[position:]

    print('head', head, 'tail', tail, insertion)

    head.append(insertion)

    finalContent = head + tail
    print(finalContent)

    with open(file, 'w') as fileToWrite:
        fileToWrite.writelines(finalContent)

# insertContent('extras_archivos/files/data.txt', 5, 'chotito')
insertarFila('extras_archivos/files/data.txt', 2, 'fila nueva')
