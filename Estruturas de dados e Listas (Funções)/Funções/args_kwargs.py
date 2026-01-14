# DEFINIÇÃO DE FUNÇÃO COM *ARGS E **KWARGS

# FUNÇÃO COM *ARGS — VÁRIOS BRINQUEDOS NA CAIXA

# Definimos uma função que pode receber vários brinquedos como argumentos posicionais.
# Esses brinquedos são armazenados em uma tupla chamada 'brinquedos'.
def brincar_com_brinquedos(*brinquedos):
    print("Hoje vamos brincar com:")
    # Percorremos cada brinquedo e mostramos na tela
    for brinquedo in brinquedos:
        print(f"- {brinquedo}")

# Chamamos a função com vários brinquedos diferentes
brincar_com_brinquedos("carrinho", "boneca", "dinossauro", "bola")

# FUNÇÃO COM **KWARGS — MOCHILA COM BOLSOS NOMEADOS

# Definimos uma função que recebe vários brinquedos guardados em bolsos com nome.
# Esses pares nome-valor são armazenados em um dicionário chamado 'bolsos'.
def mochila_de_brinquedos(**bolsos):
    print("O que tem na mochila?")
    # Percorremos cada bolso e mostramos o que tem dentro
    for nome_do_bolso, brinquedo in bolsos.items():
        print(f"No bolso '{nome_do_bolso}' tem: {brinquedo}")

# Chamamos a função passando brinquedos em bolsos com nomes diferentes
mochila_de_brinquedos(
    frente="pião",
    lateral="corda de pular",
    secreto="super-herói",
    garrafa="bolinhas de gude"
)

# FUNÇÃO COM ARGUMENTO FIXO, *ARGS E **KWARGS

# Esta função recebe:
# - Um argumento obrigatório (dia)
# - Vários brinquedos soltos (args)
# - E brinquedos guardados em bolsos nomeados (kwargs)
def dia_de_brincar(dia, *brinquedos, **mochila):
    print(f"Hoje é {dia} e vamos brincar com:")

    # Mostra os brinquedos soltos
    for brinquedo in brinquedos:
        print(f"- {brinquedo}")

    print("\nE na mochila temos:")
    # Mostra os brinquedos guardados nos bolsos
    for bolso, item in mochila.items():
        print(f"No bolso '{bolso}': {item}")

# Chamamos a função com tudo misturado!
dia_de_brincar(
    "sábado",  # argumento obrigatório

    # brinquedos soltos (args)
    "lego", "avião", "boneco do Hulk",

    # brinquedos nos bolsos (kwargs)
    lanche="biscoito",
    surpresa="slime",
    garrafa="suco"
)





# Esta função exibe um poema formatado com título, corpo e metadados.
# Ela usa:
# - 'data_extenso' como argumento obrigatório (ex: título ou data)
# - '*args' para receber várias linhas do poema como argumentos posicionais
# - '**kwargs' para receber informações adicionais como argumentos nomeados (ex: autor, ano)

def exibir_poema(data_extenso, *args, **kwargs):
    # 'args' é uma tupla com todas as linhas do poema passadas como argumentos posicionais
    # Usamos "\n".join(args) para juntar todas as linhas em um único texto com quebras de linha
    texto = "\n".join(args)

    # 'kwargs' é um dicionário com os argumentos nomeados extras (ex: autor="Tim Peters", ano=1999)
    # Aqui usamos uma list comprehension para formatar cada par chave-valor como "Chave: Valor"
    # .title() deixa a primeira letra da chave em maiúscula (estilo título)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])

    # Montamos a mensagem final com o título, o poema e os metadados
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"

    # Exibimos a mensagem completa
    print(mensagem)


# CHAMADA DA FUNÇÃO

# Passamos:
# - O primeiro argumento obrigatório: o título do poema
# - Várias linhas do poema como argumentos posicionais (args)
# - Argumentos nomeados (kwargs) com metadados como autor e ano

exibir_poema(
    "Zen of Python",  # Título do poema

    # Linhas do poema (args)
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",

    # Metadados (kwargs)
    autor="Tim Peters",
    ano=1999,
)

# Saída esperada:
# Zen of Python 

"""
Resumo rápido:
*args: pega todos os argumentos posicionais extras e junta numa tupla.

**kwargs: pega todos os argumentos nomeados extras e junta num dicionário.

Use quando a função precisa ser flexível pra receber quantidade variável de dados.

Muito útil pra criar funções genéricas, tipo essa que monta poemas ou textos.
"""


