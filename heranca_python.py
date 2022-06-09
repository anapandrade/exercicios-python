from abc import abstractmethod

# EXERCÍCIOS HERANÇA

# EXERCÍCIO 1
# Informe abaixo uma classe chamada Gato, que sobrescreva o método getEspecie da superclasse e retorne nome + " é um Gato".
# Entrada de dados
# Felix
# Saída esperada
# Felix é um Gato
# Obs: Devido a limitações do Java, a classe definida não pode ser pública.
class Gato:
    nome = ""
    @property
    def especie(self):
        return self.nome + "é um Gato"


# EXERCÍCIO 2
# Informe abaixo uma classe chamada Programador, que respeite as regras abaixo:
# Contenha uma propriedade privada linguagem textual;
# A proprieade deve ser iniciada no construtor da classe;
# Sobrescreva o método showInfo() da superclasse;
# Exiba os dados do "Programador".
# Entrada de dados
# Carlos Silva
# 33
# Java
# Saída esperada
# Carlos Silva
# 33
# Java
# Dica: Utilize a cláusula super para acessar membros da classe herdada.
# Obs: Devido a limitações do Java, a classe definida não pode ser pública.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Programador(Pessoa):
    def __init__(self, nome, idade, linguagem):
        super().__init__(nome, idade)
        self.linguagem = linguagem

    def show_info(self):
        return self.nome + self.idade + self.linguagem

# EXERCÍCIO 3
#
# Dada a classe abstrada abaixo:
# abstract class Livro
# {
#     String titulo;
#
#     abstract void setTitulo(String s);
#
#     String getTitulo(){
#         return titulo;
#     }
# }
# Defina uma classe chamada MeuLivro que a herde e implemente o método abstrado dela.
# Entrada de dados
# Senhor dos Anéis
# Saída esperada
# Senhor dos Anéis
# Obs: Devido a limitações do Java, a classe definida não pode ser pública.

class Livro:
    abstract = True

    def __init__(self, titulo):
        self.__titulo = titulo

    @property
    def titulo(self):
        return self.__titulo

    @abstractmethod
    def set_titulo(self, titulo):
        ...

class MeuLivro(Livro):
    def set_titulo(self, titulo):
        super().__titulo = titulo