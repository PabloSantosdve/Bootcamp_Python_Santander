# Função geradora que recebe uma lista de números
def meu_gerador(numeros: list[int]):
    # Para cada número na lista...
    for numero in numeros:
        # "yield" devolve o valor multiplicado por 2 e pausa a função
        yield numero * 2

# Usando o gerador num loop for
for i in meu_gerador(numeros=[1, 2, 3]):
    print(i)  # Imprime cada número da lista * 2

"""
yield é tipo um return que lembra onde parou.
Toda vez que o for chama o gerador, ele "volta" na última linha e continua dali.
Gerador é uma forma compacta e eficiente de criar iteradores sem ter que definir toda a classe com __iter__ e __next__.
Tu economiza memória porque ele só gera o próximo valor quando precisa, não tudo de uma vez.

Se quiser ir além:
Dá pra usar yield em funções mais complexas, até pra processar streams gigantes.

"""