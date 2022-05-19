# Exercício 1:
# Declare uma variável a com valor igual a 10 e uma variável b com valor igual a 20. Usando uma variável de nome c, troque os valores de a e b.

a = 10
b = 20
c = a
a = b
b = c
print(a)
print(b)

# Exercício 2:
# Declare uma variável com o nome raio e calcule a área de um círculo. Sabendo que a fórmula de cálculo da área é igual a pi*(raio*raio).
raio = 10
print(3.14 * (raio * raio))

# Exercício 3:
# A nave espacial mais rápida já construída pelo homem é a Voyager 1, ela alcança uma velocidade de 278 280 km/h.
# Em 27/07/2018 o planeta Marte chegou a ficar a 570.000.000km da Terra, essa foi a distância mais próxima dos ultimos 15 anos. Levando em conta esses dados, calcule em dias o tempo necessário para a nave chegar em Marte.
distancia = 570000000
velocidade = 278280
distancia_dia = velocidade * 24
print(distancia / distancia_dia)

# Exercício 4:
# Escreva um algoritmo para ler as dimensões de um retângulo (base e altura), calcular e escrever a área do retângulo.
base = int(input("Digite a área do retangulo: "))
altura = int(input("Digite a altura do retangulo: "))
print(base * altura)

# Exercício 5:
# Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e exibir o valor do novo salário.

salario_atual = int(input("Digite o salario atual: "))
percentual = int(input("Digite o percentual: "))
desconto = (percentual*salario_atual)/100
print(salario_atual + desconto)

# Exercício 6:
# O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor.

custo = float(input("Digite o custo: "))
imposto = (45*custo) / 100
distribuidor = (28*custo)/100

print(custo+imposto+distribuidor)


# Exercício 1:
# ler dois valores e exibir o maior deles.
numero_1 = int(input("Digite n1: "))
numero_2 = int(input("Digite n2: "))
if numero_1 > numero_2:
    print(numero_1)
else:
    print(numero_2)

# Exercício 2:
# Ler dois valores e escrever o menor deles ou se são iguais.
numero_1 = int(input("Digite n1: "))
numero_2 = int(input("Digite n2: "))
if numero_1 < numero_2:
    print(numero_1)
elif numero_1 == numero_2:
    print("iguais")
else:
    print(numero_2)

# Exercício 3:
# Ler as notas de 1a. e 2a. avaliações de um aluni. Calcular a média aritmética simpes e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que a nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.
nota_1 = float(input("Digite n1: "))
nota_2 = float(input("Digite n1: "))
media = (nota_1 + nota_2)/2
if media >= 6:
    print("aprovado")
else:
    print("reprovado")
print(media)


# Exercício 4:
# Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e quantidade mínima em estoque de um produto.
# Calcular e escrever a quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2). Se a quantidade em estoque for maior ou igual a quantidade média escrever a mensagem'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.

estoque_atual = int(input("Digite estoque: "))
quantidade_maxima = int(input("Digite a quantidade máxima: "))
quantidade_minima = int(input("Digite a quantidade máxima: "))

media = (quantidade_maxima + quantidade_minima)/2
if estoque_atual >= media:
    print("Não efetuar compra")
else:
    print("efetuar compra")

# Exercício 5:
# No Brasil pessoas entre 16 e 18 anos e acima de 60 não são obrigadas a votar. Crie um algoritmo que leia a idade de uma pessoa e iforme se ela ainda não pode votar, o voto é opcional ou obrigatório.

idade = int(input("Digite a idade: "))

if idade > 16 and idade < 18:
    print("Voto opcional")
elif idade > 60:
    print("Voto opcional")
elif idade >= 18 and idade < 60:
    print("Voto obrigatório")
else:
    print("Nao pode votar")