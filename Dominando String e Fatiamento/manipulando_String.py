# Manipulação de Strings em Python

# O que é manipulação de string?
# É o processo de acessar, modificar, analisar ou transformar textos (strings).
# Isso pode incluir operações como cortar pedaços do texto, substituir palavras,
# alterar maiúsculas/minúsculas, contar caracteres, dividir frases, entre outros.

# Exemplo de uma string

texto = "Python é uma linguagem poderosa e divertida!"

# Em Python, podemos acessar caracteres de uma string usando índices.
# O índice 0 representa o primeiro caractere, o índice 1 o segundo, e assim por diante.
# Porém, se usarmos índices negativos, acessamos os caracteres do final para o início.
# Ou seja:
# -1 representa o último caractere
# -2 representa o penúltimo
# -3 representa o antepenúltimo, etc.
# Acessar caracteres (indexação)
print("Primeiro caractere:", texto[0])  # P
print("Último caractere:", texto[-1])   # !

# Fatiamento (slice)
print("Primeiras 6 letras:", texto[:6])  # Python
print("Palavra 'linguagem':", texto[13:22])  # linguagem

# Tamanho da string
print("Quantidade de caracteres:", len(texto))  # Conta todos os caracteres, incluindo espaços

# Converter para maiúsculas e minúsculas
print("Maiúsculas:", texto.upper())
print("Minúsculas:", texto.lower())

# Substituir palavras
novo_texto = texto.replace("poderosa", "incrível")
print("Texto modificado:", novo_texto)

# Verificar se uma palavra está na string
print("Existe 'divertida' no texto?", "divertida" in texto)

# Contar quantas vezes uma palavra aparece
print("Quantas vezes 'uma' aparece:", texto.count("uma"))

# Dividir o texto em uma lista de palavras
palavras = texto.split()
print("Lista de palavras:", palavras)

# Juntar uma lista de palavras em uma string
nova_frase = " ".join(palavras)
print("Frase unida novamente:", nova_frase)


curso = "Python"

print(curso.upper())


#Exemplos da aula

# Exemplos da aula sobre manipulação de strings

nome = "Pablo"

# Converte todos os caracteres para MAIÚSCULAS
print(nome.upper())  # Saída: PABLO

# Converte todos os caracteres para minúsculas
print(nome.lower())  # Saída: pablo

# Converte a primeira letra de cada palavra para maiúscula (como em títulos)
print(nome.title())  # Saída: Pablo

# ------------------------------

texto = "   Ola mundo"  # Observe os espaços antes da palavra

# Imprime o texto original com espaços e um ponto no final
print(texto + ".")  # Saída:    Ola mundo.

# Remove os espaços do início e do fim da string (função strip)
print(texto.strip() + ".")  # Saída: Ola mundo.

# Remove apenas os espaços da direita (final da string)
print(texto.rstrip() + ".")  # Saída:    Ola mundo.

# Remove apenas os espaços da esquerda (início da string)
print(texto.lstrip() + ".")  # Saída: Ola mundo.

# ------------------------------

menu = "Python"

# Imprime a palavra com "####" antes e depois, sem espaços
print("####" + menu + "####")  # Saída: ####Python####

# Centraliza o texto em 14 espaços, preenchendo com espaços em branco
print(menu.center(14))  # Saída: '    Python    '

# Centraliza o texto em 14 espaços, preenchendo com o caractere "#"
print(menu.center(14, "#"))  # Saída: '####Python####'

# Insere um hífen entre cada letra da string
print("-".join(menu))  # Saída: P-y-t-h-o-n
