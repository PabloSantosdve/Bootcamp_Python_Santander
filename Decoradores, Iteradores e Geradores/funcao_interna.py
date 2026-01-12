# Função principal, é tipo o chefão do código aqui
def principal():
    print("executando a funcao principal")  # Essa linha aparece assim que a função principal é chamada

    # Função interna definida DENTRO da principal (função dentro de função = função aninhada)
    def funcao_interna():
        print("executando a funcao interna")  # Só vai rodar se for chamada DENTRO da principal

    # Outra função interna, também só existe dentro da principal
    def funcao_2():
        print("executando a funcao 2")  # Mesma lógica da de cima

    # Aqui a gente tá chamando as funções internas
    funcao_interna()  # Executa a função interna
    funcao_2()        # Executa a função 2

# Chamando a função principal de fato
principal()


"""
As funções funcao_interna e funcao_2 só existem dentro da principal.
Fora dali, elas nem existem. Se tu tentar chamar fora, vai dar erro.
Isso é usado pra encapsular lógica que só faz sentido dentro de um contexto específico.

Exemplo da vida real:
Imagina que principal() é uma cozinha, e dentro dela tu tem os utensílios (funcao_interna, funcao_2). Esses utensílios não existem fora da cozinha, são exclusivos dali.
"""