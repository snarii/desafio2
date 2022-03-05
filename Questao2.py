a=""
while (a!="sair"):
    print("Olá! :)")
    a = input("Digite uma lista para obter os pares com a diferença x:") #Determinação da lsta para criação dos pares.
    x = int(input("Agora, digite o valor de x: ")) #Determinação do valor x (Resultado da subtração dos pares a partir da lista inserida)
    arr = []
    for i in a:
        if i.isdigit():
            arr.append(int(i))
    arr.sort()
    arr2 = []
    for i in arr:
        for j in arr:
            if (j - i == x): #Condição da subtração igual ao valor x inserido.
                arr2.append([j,i])
    print(len(arr2))
