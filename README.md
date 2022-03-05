# Desafio 2
## Nome: Sarah da Cunha Costa 🌸
#### Questão 01
##### A mediana de uma lista de números é basicamente o elemento que se encontra no meio da lista após a ordenação. Dada uma lista de números com um número ímpar de elementos, desenvolva um algoritmo que encontre a mediana.
> Como a questão trata-se de uma mediana, foi necessário ordenar a lista contida na entrada. Dessa forma, utilizou-se o método "list.sort()" para organizar a lista em ordem crescente. Após isso, é importante ressaltar que a mediana é uma medida de tendência central, logo, foi preciso saber se a lista possui um número par ou ímpar de elementos. Mediante a isso, foi criada uma condição, usando a instrução "if": Se for par e seu "else" caso não for par (ou seja, ímpar).
* ##### [**Resolução da Questão 1**](https://replit.com/join/nhldiglpzo-sarahcosta2)
#### Questão 02
Dado um vetor de inteiros n e um inteiro qualquer x. Construa um algoritmo que determine o número de elementos pares do vetor que tem uma diferença igual ao valor de x.
> Foi preciso estabelecer uma lista e o valor x (a diferença dos pares) e aplicando "if (j - i == x)", contando e imprimindo a quantidade de pares tendo o resultado esperado.
* ##### [**Resolução da Questão 2**](https://replit.com/join/zpbdxmzkxu-sarahcosta2)
#### Questão 03 
##### Um texto precisa ser encriptado usando o seguinte esquema. Primeiro, os espaços são removidos do texto. Então, os caracteres são escritos em um grid, no qual as linhas e colunas tem as seguintes regras:
![image](https://user-images.githubusercontent.com/100108863/156894404-122bf2bd-63be-46e6-845e-0cd2da7877bc.png)
Considere T, como o tamanho do texto.
Se certifique de que linhas x colunas >= .
Se múltiplos grids satisfazem as condições, escolha aquele com a menor área.
Escreva um algoritmo que ao receber uma string s, mostre a mensagem encriptada de acordo com as regras descritas.
