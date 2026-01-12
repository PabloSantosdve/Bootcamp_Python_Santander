import datetime # Importa o módulo datetime para trabalhar com datas e horas

# Classe Pessoa – representa uma pessoa com nome e ano de nascimento
class Pessoa:

    # Construtor da classe, chamado ao criar um novo objeto
    def __init__(self, nome, ano_nascimento):
        self.nome = nome                        # Atributo público (sem underline)
        self._ano_nascimento = ano_nascimento   # Atributo "protegido" (com underline)

        # Conceito: ENCAPSULAMENTO
        # O underline (_) indica que esse atributo não deve ser acessado diretamente fora da classe

    # Getter calculado usando @property
    # Conceito: PROPRIEDADE COMPUTADA (atributo dinâmico)
    @property
    def idade(self):
        _ano_atual = datetime.datetime.now().year 
        # Obtém o ano atual usando datetime
        # Retorna a idade com base no ano atual menos o ano de nascimento
        return _ano_atual - self._ano_nascimento
        # Assim, não precisa armazenar a idade como atributo fixo (que envelheceria rs),
        # ela é sempre calculada na hora que for chamada.

# Criando uma instância da classe Pessoa
pessoa = Pessoa("Pablo", 2003)

# Imprimindo nome (atributo público) e idade (calculada via @property)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
# Saída: Nome: Guilherme     Idade: 28

"""Conceito: PROPRIEDADE
A propriedade permite acessar métodos como se fossem atributos, sem precisar chamar com parênteses.
Isso é útil para calcular valores dinamicamente, como a idade, sem precisar armazenar um atributo fixo.
Assim, sempre que acessar pessoa.idade, ele recalcula a idade com base no ano
atual e no ano de nascimento, garantindo que esteja sempre atualizado.
Além disso, o uso de @property permite encapsular a lógica de cálculo,
sem expor detalhes de implementação.
Isso é uma boa prática de encapsulamento, pois mantém a lógica interna da classe"""