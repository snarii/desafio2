a=""
while (a!="sair"):
    print("Olá! :)")
    a=input("Digite uma lista para obter sua mediana:")
    arr = []
    for i in a:
        if i.isdigit():
            arr.append(int(i))
    arr.sort()

    metade = len(arr) // 2
    if not len(arr) % 2:
        print((arr[metade - 1] + arr[metade]) / 2.0)
    else: 
        print(arr[metade])
     
