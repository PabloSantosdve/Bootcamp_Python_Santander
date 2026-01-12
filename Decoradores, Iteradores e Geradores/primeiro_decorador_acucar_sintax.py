# Aqui a gente tá criando um DECORADOR
# Ele é uma função que recebe outra função e devolve uma nova função com comportamento extra
def meu_decorador(funcao):
    # Essa função interna vai embrulhar (decorar) a função original
    def envelope():
        print("faz algo antes de executar")  # Coisa extra ANTES
        funcao()  # Aqui executa a função original
        print("faz algo depois de executar")  # Coisa extra DEPOIS

    return envelope  # Retorna o "envelope" que agora virou a nova versão da função original

# Esse @ é açúcar sintático (syntactic sugar)
# É a mesma coisa que fazer: ola_mundo = meu_decorador(ola_mundo)
@meu_decorador
def ola_mundo():
    print("Olá mundo!")  # Essa é a função que vai ser decorada

# Quando a gente chama ola_mundo(), não chama direto.
# Chama o "envelope", que tem o antes, o original, e o depois
ola_mundo()


"""
O que rolou aqui:
@meu_decorador intercepta a função ola_mundo e dá uma tunada nela.
Tu envolveu o comportamento original com extras antes e depois — tipo colocar uma função dentro de um pacote.

Exemplo de onde isso brilha:

- Logar quem chamou a função.
- Verificar permissão de acesso.
- Medir tempo de execução.
- Validar parâmetros.
"""