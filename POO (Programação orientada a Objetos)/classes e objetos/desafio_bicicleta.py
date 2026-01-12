# Definição de uma classe chamada 'Bicicleta'.
# Em programação orientada a objetos, uma "classe" é como um molde (ou blueprint) para criar objetos.
# Essa classe define como será o comportamento e as características (atributos e métodos) de cada bicicleta criada.
class Bicicleta:
    
    # Este é o método especial chamado __init__, também conhecido como "construtor".
    # Ele é chamado automaticamente sempre que um novo objeto da classe é criado.
    # Aqui, ele está recebendo quatro parâmetros além do 'self': cor, modelo, ano e valor.
    # O 'self' representa a instância atual do objeto, permitindo acessar atributos e métodos dentro da própria classe.
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor          # Define o atributo 'cor' da bicicleta com o valor recebido no parâmetro.
        self.modelo = modelo    # Define o atributo 'modelo'.
        self.ano = ano          # Define o atributo 'ano'.
        self.valor = valor      # Define o atributo 'valor'.

    # Método da classe chamado 'buzinar'.
    # Esse método simula o som da buzina da bicicleta e apenas imprime um texto.
    def buzinar(self):
        print("Plim plim...")

    # Método que simula a ação de parar a bicicleta.
    # Ele imprime duas mensagens em sequência para representar esse comportamento.
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    # Método que simula a ação de correr com a bicicleta.
    # Assim como os outros métodos, é apenas uma simulação textual do comportamento.
    def correr(self):
        print("Vrummmmm...")

    # Método especial __str__, que define a representação em forma de string de um objeto da classe.
    # Quando usamos a função 'print' em um objeto, o Python chama automaticamente esse método para saber o que mostrar.
    # Aqui, ele está retornando o nome da classe seguido de todos os atributos e seus valores em formato de texto.
    def __str__(self):
        # Utiliza uma compreensão de lista para iterar sobre os pares chave-valor do dicionário interno __dict__,
        # que armazena todos os atributos da instância do objeto.
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


# Agora começamos a utilizar a classe criada acima.

# Criamos uma nova instância (objeto) da classe Bicicleta, chamada 'b1'.
# Passamos os valores correspondentes aos atributos: cor = "vermelha", modelo = "caloi", ano = 2022, valor = 600.
b1 = Bicicleta("vermelha", "caloi", 2022, 600)

# Chamamos o método 'buzinar' no objeto 'b1'.
# Isso faz com que a bicicleta simule um som de buzina.
b1.buzinar()

# Chamamos o método 'correr' no objeto 'b1', que simula a bicicleta em movimento.
b1.correr()

# Chamamos o método 'parar', que mostra a bicicleta parando.
b1.parar()

# Imprimimos diretamente os atributos individuais do objeto 'b1'.
# Isso mostra os valores de cor, modelo, ano e valor diretamente.
print(b1.cor, b1.modelo, b1.ano, b1.valor)

# Criamos um segundo objeto da classe Bicicleta, chamado 'b2', com valores diferentes.
# A cor é "verde", o modelo é "monark", o ano é 2000, e o valor é 189.
b2 = Bicicleta("verde", "monark", 2000, 189)

# Usamos a função 'print' diretamente no objeto 'b2'.
# Como implementamos o método __str__, ele irá retornar uma string com todos os dados do objeto de forma formatada.
print(b2)

# Chamamos o método 'correr' no objeto 'b2', simulando ele andando.
b2.correr()
