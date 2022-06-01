# Exercício 1:
# Agora que estamos iniciando o nosso estudo de um código real, teremos alguns desafios mais práticos.
# Para este inicial, defina no trecho indicado uma classe chamada PrimeiraClasse().
# Entrada de dados
# Não há nenhuma entrada
# Saída esperada
# PrimeiraClasse
# Obs: Devido a limitações do Java, a classe definida não pode ser pública.

class PrimeiraClasse():
    pass

# Exercício 2:
# Desafio de Código
# Como funciona?
# Defina uma classe chamada Pessoa e que contenha os atributos nome, textual, e idade, número inteiro.
# Entrada de dados
# Não há nenhuma entrada
# Saída esperada
# nome
# idade
# Obs: Devido a limitações do Java, a classe definida não pode ser pública.

class Pessoa():
    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade

# Exercício 3:
# Desafio de Código
# Como funciona?
# Defina uma classe chamada Pessoa e que contenha os atributos públicos nome, textual, e idade, número inteiro.
# Entrada de dados
# Carlos Silva
# 33
# Saída esperada
# nome
# idade
# Carlos Silva
# 33
# Obs: Devido a limitações do Java, a classe definida não pode ser pública.

class Pessoa():
    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade

    def __str__(self):
        print(self.nome)
        print(self.idade)


# Exercício 4:
# Desafio de Código
# Como funciona?
# Defina uma classe chamada Pessoa e que contenha os atributos privados nome, textual, e idade, número inteiro.
# Entrada de dados
# Não há nenhuma entrada
# Saída esperada
# nome
# idade
# Obs: Devido a limitações do Java, a classe definida não pode ser pública.


class Pessoa():
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def __str__(self):
        print(self._nome)
        print(self._idade)

# Exercício 5:
# Desafio de Código
# Como funciona?
# Defina uma classe chamada Pessoa e que contenha os atributos ecapsulados nome e idade, sendo que nome é textual e idade um número inteiro.
# Entrada de dados
# Carlos Silva
# 33
# Saída esperada
# nome
# idade
# Carlos Silva
# 33
# Obs: Devido a limitações do Java, a classe definida não pode ser pública.
    class Pessoa():
        def __init__(self, nome, idade):
            self._nome = nome
            self._idade = idade

        @property
        def nome(self):
            return self._nome

        @property
        def idade(self):
            return self._idade

# Exercício 6:
# Desafio de Código
# Como funciona?
# Defina uma classe chamada Pessoa, que contenha os atributos ecapsulados nome e idade, sendo que nome é textual e idade um número inteiro. Sendo que o atributo nome deva ser somente leitura e receber um valor passado no construtor da classe.
# Entrada de dados
# Carlos Silva
# 33
# Saída esperada
# nome
# idade
# Carlos Silva
# 33
# Obs: Devido a limitações do Java, a classe definida não pode ser pública.

    class Pessoa():
        def __init__(self, idade, nome="Carlos"):
            self._nome = nome
            self._idade = idade

        @property
        def nome(self):
            return self._nome

        @property
        def idade(self):
            return self._idade