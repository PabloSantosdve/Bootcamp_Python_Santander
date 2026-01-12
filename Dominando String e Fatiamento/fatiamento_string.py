"""
# FATIAMENTO DE STRINGS EM PYTHON
# -------------------------------
# Em Python, strings são sequências de caracteres indexadas, o que significa que cada caractere
# em uma string pode ser acessado por sua posição (índice). O primeiro caractere tem índice 0,
# o segundo índice 1, e assim por diante. Também é possível usar índices negativos para contar
# a partir do final da string (por exemplo, -1 representa o último caractere).
#
# O fatiamento (ou slicing) permite extrair partes específicas de uma string utilizando a sintaxe:
#     string[início:fim:passo]
#
# - 'início' é o índice onde o fatiamento começa (inclusivo).
# - 'fim' é o índice onde o fatiamento termina (exclusivo).
# - 'passo' é opcional e define o intervalo entre os caracteres selecionados.
#
# Se algum dos parâmetros for omitido, Python assume valores padrão:
# - início = 0
# - fim = tamanho da string
# - passo = 1
#
# O fatiamento é uma ferramenta poderosa para manipular textos, extrair informações específicas,
# inverter strings, pular caracteres, entre outras aplicações úteis no dia a dia da programação.

"""

texto = "Programação em Python"

# Fatiando os primeiros 12 caracteres
print(texto[0:12])  # Saída: Programação

# Fatiando do índice 14 até o final
print(texto[14:])   # Saída: Python

# Fatiando com passo (pegando um caractere a cada 2)
print(texto[0:12:2])  # Saída: Pormçã

nome_completo = "Carlos Eduardo da Silva"

"""
Exemplo 2: Fatiamento com reordenação (como fizemos com índices no .format)
"""
# Extraindo partes do nome
primeiro_nome = nome_completo[0:6]     # Carlos
sobrenome = nome_completo[-5:]         # Silva
espelhado = nome_completo[::-1]        # Truque para deixar o nome espelhado

print(f"Primeiro nome: {primeiro_nome}")
print(f"Sobrenome: {sobrenome}")
print(f"Espelhado: {espelhado}")


"""
Exemplo 3: Fatiamento com dicionário (simulando acesso por índice)
"""
dados = {
    "mensagem": "Desenvolvimento de Software"
}

# Fatiando a string dentro do dicionário
print(dados["mensagem"][0:14])  # Saída: Desenvolvimento
print(dados["mensagem"][-8:])   # Saída: Software

