# Classe que cria um iterador customizado pra uma lista de números
class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros  # recebe a lista de números
        self.contador = 0       # contador interno pra controlar o índice atual

    def __iter__(self):
        # Retorna o próprio objeto iterador
        # Isso permite usar 'for' diretamente nesse objeto
        return self

    def __next__(self):
        # Método que retorna o próximo valor da iteração
        try:
            numero = self.numeros[self.contador]  # pega o número atual
            self.contador += 1                    # incrementa o contador pro próximo
            return numero * 2                     # retorna o número * 2 (lógica extra sua)
        except IndexError:
            # Quando acabar a lista, lança StopIteration pra terminar o loop for
            raise StopIteration

# Usando o iterador customizado no for
for i in MeuIterador(numeros=[38, 13, 11]):
    print(i)  # imprime cada número da lista multiplicado por 2

"""
Explicação maneiríssima:
__iter__ precisa retornar um objeto iterador (aqui é ele mesmo).

__next__ entrega o próximo valor a cada chamada, ou lança StopIteration pra avisar que acabou.

Isso faz o for saber quando parar.

No teu caso, além de iterar, tu ainda tá multiplicando o número por 2, ou seja, tá decorando a iteração com uma transformação.
"""
