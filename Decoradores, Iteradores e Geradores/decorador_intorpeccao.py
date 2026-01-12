import functools  # importa o módulo que tem a mágica pra manter os metadados da função original

# Decorador com suporte a wraps
def meu_decorador(funcao):
    @functools.wraps(funcao)  # isso aqui garante que os metadados da função original (como __name__) não sejam perdidos
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs)  # executa a função normalmente (podia ter mais coisa antes/depois se quisesse)

    return envelope  # retorna a função decorada

# Função decorada
@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá mundo {nome}!")  # só imprime a mensagem com o nome

# Aqui a gente quer ver o nome real da função
print(ola_mundo.__name__)  # graças ao @wraps, vai imprimir "ola_mundo" e não "envelope"

