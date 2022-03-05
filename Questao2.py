a=""
while (a!="sair"):
    print("Olá! :)")
    a = input("Digite uma lista para obter os pares com a diferença x:")
    x = int(input("Agora, digite o valor de x: "))
    arr = []
    for i in a:
        if i.isdigit():
            arr.append(int(i))
    arr.sort()
    arr2 = []
    for i in arr:
        for j in arr:
            if (j - i == x):
                arr2.append([j,i])
    print(len(arr2))
