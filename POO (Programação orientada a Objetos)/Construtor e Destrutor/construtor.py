class Cachorro:
    # Método construtor: é chamado automaticamente quando a classe é instanciada
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando o cachorro...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def falar(self):
        print("auau")


# Criando um objeto da classe Cachorro (vai disparar o __init__)
cachorro1 = Cachorro("Bolt", "branco")

# Chamando um método da instância
cachorro1.falar()

# Imprimindo atributos
print(cachorro1.nome, cachorro1.cor, cachorro1.acordado)

#__init__: sempre é chamado ao criar um objeto.

# Ele é usado para inicializar os atributos do objeto.
# Você pode passar parâmetros para o __init__ para definir valores iniciais.    
# Se você não definir um __init__, o Python cria um padrão que não faz nada.
# É uma boa prática definir o __init__ para garantir que seus objetos comecem com
# valores válidos e esperados.
# Se você quiser que o __init__ faça algo mais complexo, como abrir um arquivo ou conectar a um banco de dados,
# você pode fazer isso lá dentro. Mas lembre-se de que o __init__ deve ser rápido e não deve fazer operações demoradas,
# porque ele é chamado toda vez que você cria um novo objeto.
