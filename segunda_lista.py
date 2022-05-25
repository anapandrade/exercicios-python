# Exercício 1:
# Leia 5 números inteiros positivos e armazena em um vetor. Em seguida, exiba o valor de cada posição.
lista_numeros = []
for i in range(5):
    lista_numeros.append(int(input("Digite um número: ")))
print(lista_numeros)

# Exercício 2:
# Leia 5 números positivos e armazena em um vetor. Exiba o maior, o menor e a média em relação aos números armazenados.
lista_numeros = []
for i in range(5):
    lista_numeros.append(int(input("Digite um número: ")))
print(max(lista_numeros))
print(min(lista_numeros))
soma = 0
for num in lista_numeros:
    soma += num
print(soma/5)

# Exercício 3:
# Leia 5 números positivos e armazene em um vetor. Exiba a moda em relação aos números armazenados.
lista_numeros = []
for i in range(5):
    lista_numeros.append(int(input("Digite um número: ")))
# Exercício 4:
# Leia 5 números inteiros e armazene em um vetor, ordene e exiba em ordem crescente.

numeros = []
for i in range(5):
    numero = int(input("Digite um número: "))
    for chave, valor in enumerate(numeros):
        if numero < valor:
            numeros.insert(chave, numero)
            break
    else:
        numeros.append(numero)
print("Lista ordenada:", numeros)
# Exercício 5:
# Escrever um programa que leia duas matrizes 2x2 e gere uma terceira matriz com a soma dos elementos correspondentes
import random
matriz1 = []
n = int(input("Informe a quantidade de linhas da matriz 1:" ))
m = int(input("Informe a quantidade de colunas da matriz 1:" ))
for i in range(n):
     matriz1.append([])
     for j in range(m):
        matriz1[i].append(random.randint(0,100))

for i in range(len(matriz1)):
    for j in range(len(matriz1[i])):
        print(matriz1[i][j])

matriz2 = []
n = int(input("Informe a quantidade de linhas da matriz 2:" ))
m = int(input("Informe a quantidade de colunas da matriz 2:" ))

for i in range(n):
     matriz2.append([])
     for j in range(m):
        matriz2[i].append(random.randint(0,100))

for i in range(len(matriz2)):
    for j in range(len(matriz2[i])):
        print(matriz2[i][j])

result = []
for i in range(len(matriz1)):
    result.append([])
    for j in range(len(matriz1[0])):
        result[i].append(matriz1[i][j] + matriz2[i][j])
print(result)
# Exercício 1:
# Crie um programa que imprima 11 vezes a classe "TreinaWeb!".
# Dica: Resolva o problema duas vezes, uma usando "for" e outra usando "while".
for i in range(11):
    print("Treinaweb")

contador = 0
while contador <= 11:
    print("Treinaweb")
    contador += 1

# Exercício 2:
# Escreva um programa que receba um número qualquer do usuário e informe se ele é primo.
numero = int(input("Digite o número: "))
cont = 0
for i in range(2, numero):
    if numero % i == 0:
        cont += 1
if cont == 0:
    print("primo")
else:
    print("não é primo")
# Exercício 3:
# Faça um programa que peça ao usuário um número entre 12 e 20. Se a pessoa digitar um número diferente, mostrar a mensagem "entrada inválida" e solicitar o número novamente. Se digitar correto mostrar o número digitado.
resposta = 0
while resposta == 0:
    numero = int(input("Digite um número entre 12 e 20: "))
    if numero > 12 and numero < 20:
        print(numero)
        resposta = 1
    else:
        print("número inválido")

# Exercício 4:
# Escreva um algoritmo para ler as notas da primeira e da segunda avaliação de um aluno, calcule e imprima a média (simples) desse aluno. Só devem ser aceitos valores válidos durante a leitura (0 a 10) para cada nota. Acrescente uma mensagem NOVO CÁLCULO (S/N)?' ao final do exercicio. Se for respondido 'S' deve retornar e executar um novo cálculo, caso contrário deverá encerrar o algoritmo. Dica: Use do-while
resposta = "S"
while resposta == "S":
    nota1 = int(input("Digite a nota 1: "))
    if nota1 < 0 or nota1 > 10:
        print("nota inválida")
        break
    nota2 = int(input("Digite a nota 2: "))
    if nota2 < 0 or nota2 > 10:
        print("nota inválida")
        break
    media = (nota1 + nota2) / 2
    print(media)
    resposta = input("Quer continuar? S/N ")
