a=""
while (a!="sair"):
    print("Olá! :)")
    a=input("Digite uma lista para obter sua mediana:")
    a[a.index("[")+1:len(a)-1] #Obter os elementos entre "[" e "]", para trabalhar com os números contidos na lista inserida.
    arr=(a[a.index("[")+1:len(a)-1]).split(",") #Dividir os elementos com "," e criação da lista
    arr.sort() #Organizar a lista em ordem crescente
    h=[int(val) for val in arr] #Transformar os elementos strings em inteiros.
    if len(h)%2 == 0: #Se for par, é selecionado os valores do meio (na ordem crescente), somados e dividido por 2, obtendo a mediana.
        aux=h[(int(len(h)/2)-1)]
        aux=aux+h[int(len(h)/2)]
        aux=aux/2
        print(aux)
    else: #Caso não for par, como a lista presente na enunciado da questão, o valor da mediana é igual ao elemento do meio na ordem crescente. 
        print(h[int(len(h)/2)])
     
