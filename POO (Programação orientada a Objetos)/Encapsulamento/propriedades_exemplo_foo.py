# Classe Foo – usada pra demonstrar o uso de propriedades (@property)
class Foo:

    # Construtor da classe. Recebe um valor opcional e guarda em _x (atributo "protegido")
    # Conceito: ENCAPSULAMENTO – _x é tratado como interno/privado
    def __init__(self, x=None):
        self._x = x

    # Getter personalizado para acessar 'x' como se fosse um atributo comum
    # Conceito: PROPRIEDADE (@property) – permite acessar método como atributo
    @property
    def x(self):
        # Se _x estiver com valor None ou "false", retorna 0
        return self._x or 0

    # Setter – chamado quando fazemos foo.x = valor
    # Conceito: ENCAPSULAMENTO + VALIDAÇÃO/CONTROLE DE ESCRITA
    @x.setter
    def x(self, value):
        # Em vez de sobrescrever _x, aqui ele soma o valor recebido (+=)
        # Ou seja, foo.x = 10 na real tá adicionando 10 ao _x
        self._x += value

    # Deleter – chamado quando usamos del foo.x
    # Conceito: CONTROLE DE DELEÇÃO
    @x.deleter
    def x(self):
        # Em vez de remover o atributo, reseta ele pra 0
        self._x = 0


# Criando objeto da classe Foo com valor inicial 10
foo = Foo(10)

# Chama o getter @property, retorna 10
print(foo.x)  # Saída: 10

# Chama o deleter @x.deleter, que reseta _x pra 0
del foo.x

# Chama o getter de novo. Como _x agora é 0, retorna 0
print(foo.x)  # Saída: 0

# Chama o setter: em vez de substituir, ele soma 10 ao _x (0 + 10)
foo.x = 10

# Mostra o novo valor de _x (agora 10 novamente)
print(foo.x)  # Saída: 10

# Chama o setter de novo, soma 5 ao _x (10 + 5)
foo.x = 5

# Mostra o valor atualizado de _x (agora 15)
print(foo.x)  # Saída: 15