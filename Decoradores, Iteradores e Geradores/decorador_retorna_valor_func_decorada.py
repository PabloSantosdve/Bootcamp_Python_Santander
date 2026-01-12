# Decorador que recebe uma função e retorna uma função "embrulhada" com comportamento extra
def meu_decorador(funcao):
    # Essa função interna vai substituir a original e aceitar qualquer argumento
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")  # Ação antes da função original
        funcao(*args, **kwargs)  # Chama a função original com os argumentos recebidos
        print("faz algo depois de executar")  # Ação depois da função original

    return envelope  # Retorna a função decorada

# Função que será decorada, aceita dois argumentos
@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá mundo {nome}!")  # Só imprime uma saudação com o nome passado

# Chamando a função decorada com dois argumentos
ola_mundo("João", 1000)

"""
O decorador “embrulha” a função original, adicionando prints antes e depois.

A função decorada aceita e passa qualquer número de argumentos (*args, **kwargs), então é flexível.

Quando você chama ola_mundo("João", 1000), na verdade tá executando o envelope que chama ola_mundo dentro.
"""