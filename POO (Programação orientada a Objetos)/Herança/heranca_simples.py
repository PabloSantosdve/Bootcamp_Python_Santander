#sintaxe basica herança simples
#class A:
    #pass
#class B(A):
    #pass

#herança multipla 
#class C(A, B):
    #pass

# Classe base chamada Veiculo
# Todas as outras vão herdar dessa aqui
class Veiculo:
    # Construtor da classe (chamado quando um objeto é criado)
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor                   # Cor do veículo
        self.placa = placa               # Placa do veículo
        self.numero_rodas = numero_rodas # Número de rodas

    # Método comum da classe
    def ligar_motor(self):
        print("Ligando o motor...")

    def desligar_motor(self):
        print("Desligando motor...")
    # Método especial que define a string que será exibida com print()
    def __str__(self):
        # Vai montar uma string com o nome da classe e os atributos
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


# Classe Motocicleta herda tudo de Veiculo
class Motocicleta(Veiculo):
    pass  # Não tem nada novo, só herdando


# Classe Carro herda tudo de Veiculo
class Carro(Veiculo):
    pass  # Também não muda nada, só herda


# Classe Caminhao herda de Veiculo, mas tem coisa a mais
class Caminhao(Veiculo):
    # Redefinimos o construtor pra incluir o atributo "carregado"
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)  # Chama o construtor da classe-pai
        self.carregado = carregado  # Atributo extra só do caminhão

    # Método próprio do caminhão
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

class Bicicleta(Veiculo):
    def __init__(self, cor, placa, numero_rodas):
        super().__init__(cor, placa, numero_rodas)
    def status(self):
        print("Essa bicicleta é chave!!! ")

# Criando os objetos (instâncias das classes)

# Motocicleta herda tudo da classe Veiculo
moto = Motocicleta("preta", "abc-1234", 2)

# Carro herda tudo de Veiculo também
carro = Carro("branco", "xde-0098", 4)

# Caminhão herda de Veiculo, mas tem um atributo a mais
caminhao = Caminhao("Roxo", "gfd-8712", 8, False)

bicicleta= Bicicleta("Prata", "Sem placa", 2)

# Imprimindo os objetos (vai chamar o __str__ automaticamente)
print(moto)      # Motocicleta: cor=preta, placa=abc-1234, numero_rodas=2
print(carro)     # Carro: cor=branco, placa=xde-0098, numero_rodas=4
print(caminhao)  # Caminhao: cor=roxo, placa=gfd-8712, numero_rodas=8, carregado=True
print(bicicleta)  


# Ligando o motor de todos os veículos
moto.ligar_motor()
carro.ligar_motor()
caminhao.ligar_motor()
bicicleta.ligar_motor()

bicicleta.status()
# Verificando se o caminhão está carregado (só ele tem esse método)
caminhao.esta_carregado()
bicicleta.desligar_motor()