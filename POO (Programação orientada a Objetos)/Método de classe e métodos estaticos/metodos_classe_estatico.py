# Definindo a classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        # Atributos de instância, guardam dados únicos de cada objeto Pessoa
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        # Método de classe: recebe a classe (cls) em vez da instância (self)
        # Aqui ele calcula a idade com base no ano de nascimento
        idade = 2022 - ano
        # Retorna uma nova instância da classe usando cls (boa prática p/ herança)
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        # Método estático: não recebe nem self nem cls
        # Apenas executa uma lógica genérica — aqui verifica se a idade é >= 18
        return idade >= 18


# Criando uma pessoa usando o método de classe, passando ano de nascimento
p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")

# Imprimindo o nome e idade da pessoa criada
print(p.nome, p.idade)

# Verificando se alguém com 18 anos é maior de idade (esperado: True)
print(Pessoa.e_maior_idade(18))

# Verificando se alguém com 8 anos é maior de idade (esperado: False)
print(Pessoa.e_maior_idade(8))
