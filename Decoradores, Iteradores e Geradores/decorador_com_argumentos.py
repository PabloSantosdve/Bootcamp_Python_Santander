# Decorador que aceita funções com qualquer número de argumentos e retorna o resultado
def meu_decorador(funcao):
    def envelope(*args, **kwargs):  # aceita argumentos posicionais e nomeados
        print("faz algo antes de executar")
        resultado = funcao(*args, **kwargs)  # executa a função original com os argumentos recebidos
        print("faz algo depois de executar")
        return resultado  # retorna o que a função original retornaria

    return envelope  # retorna o "embrulho decorado"

# Função decorada, agora com parâmetros
@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá mundo {nome}!")  # só pra mostrar o nome recebido
    return nome.upper()  # devolve o nome em CAPS LOCK só pra zoar

# Chamada da função decorada
resultado = ola_mundo("João", 1000)
print(resultado)  # imprime o retorno da função original (JOÃO)
print(ola_mundo)  # mostra que ola_mundo agora é a função envelope

"""
Explicação:
*args: pega qualquer quantidade de argumentos posicionais.

**kwargs: pega qualquer quantidade de argumentos nomeados.

resultado = funcao(*args, **kwargs): repassa os argumentos pra função original.

O decorador agora é flexível, aceita qualquer tipo de função.
"""