# Função simples que recebe um nome e retorna uma saudação
def mensagem(nome):
    print("executando mensagem")  # Mostra que essa função foi chamada
    return f"Oi {nome}"  # Retorna uma saudação com o nome

# Função um pouco mais "formal" que também recebe um nome
def mensagem_longa(nome):
    print("executando mensagem longa")  # Mostra que essa função foi chamada
    return f"Olá tudo bem com você {nome}?"  # Retorna uma saudação mais longa

# Função que recebe outra função como parâmetro
# Isso é uma característica de linguagens que suportam "funções de primeira classe"
# Aqui começa o conceito que dá base pros decoradores!
def executar(funcao, nome):
    print("executando executar")  # Mostra que a função 'executar' foi chamada
    return funcao(nome)  # Executa a função passada como argumento

# Exemplo de uso: chamando 'mensagem' através da função 'executar'
print(executar(mensagem, "Joao"))

# Outro exemplo: chamando 'mensagem_longa' através da função 'executar'
print(executar(mensagem_longa, "Djonga"))

# ---------------------------
# O que é um DECORADOR?
# ---------------------------
# Um decorador é basicamente uma função que recebe outra função como argumento,
# faz alguma coisa com ela (tipo adicionar um comportamento), e retorna uma nova função.

# Exemplo de decorador:
def meu_decorador(func):
    def wrapper(nome):
        print("Antes de executar a função")
        resultado = func(nome)  # Chama a função original
        print("Depois de executar a função")
        return resultado
    return wrapper

# Aqui aplicamos o decorador usando a sintaxe com @ (é açúcar sintático do Python)
@meu_decorador
def saudacao(nome):
    return f"Fala aí {nome}!"

# Quando chamamos saudacao, o decorador é ativado:
print(saudacao("Pablo"))

# Resultado:
# Antes de executar a função
# Depois de executar a função
# Fala aí Pablo!
