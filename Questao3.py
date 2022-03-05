import sys
from math import floor, ceil
print ("Olá, tudo bem?")
a=input("Digite um texto para ser encriptado:").replace(" ", "")
t=len(a)#Tamanho do vetor
raiz= t**.5#Raiz do tamanho do vetor para elaboração da proporção do grid
l=int(floor(raiz))#Determinar linha
c=int(ceil(raiz))#Determinar coluna
while l*c<t:
    if l<c:
        l+=1
    else:
        c+=1
a+= ((l*c-t)*" ")
grid=[]
for i in range(l):
    grid.append(a[i*c:c*(i + 1)])
for i in range(c):
    mensagem= ""
    for j in range(l):
        mensagem+= grid[j][i]
    sys.stdout.write(mensagem.strip() + " ")
