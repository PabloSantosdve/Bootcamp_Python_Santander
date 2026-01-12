"""
Exemplo de estrutura de repetição FOR em Python

O que é?
O `for` é usado para repetir um bloco de código para cada item de uma sequência (como listas, strings ou intervalos de números).

Quando usar?
Use quando quiser executar algo várias vezes, especialmente ao percorrer coleções de dados.
"""

# Exemplo: imprimir os números de 1 a 5
for numero in range(1, 6):  # range(1, 6) gera os números 1, 2, 3, 4, 5
    print(f"Número atual: {numero}")

# O comando 'for numero in range(1, 6)' significa:
# "Para cada número na sequência de 1 até 5, execute o bloco abaixo."
# 
# A função 'range(início, fim)' gera uma sequência de números inteiros,
# começando pelo valor de 'início' e indo até 'fim - 1'.
# 
# No exemplo abaixo, o 'range(1, 6)' gera os números: 1, 2, 3, 4, 5

for numero in range(1, 6):
    print(numero)


# Solicita ao usuário que digite um texto
text = input("Informe um texto: ")

# Define uma string com as vogais maiúsculas
VOGAIS = "AEIOU"

# Percorre cada letra do texto digitado
for letra in text:
    # Verifica se a letra (convertida para maiúscula) está na string de vogais
    if letra.upper() in VOGAIS:
        # Se for vogal, imprime a letra na mesma linha (sem quebra de linha)
        print(letra, end="")

# Após o laço, imprime uma quebra de linha para finalizar a saída
print()  # adiciona uma quebra de linha


# A função range() é usada para gerar uma sequência de números.
# Ela é frequentemente usada com loops for para repetir uma ação várias vezes.

# Sintaxe básica: range(início, fim, passo)
# - início: número onde a sequência começa (opcional, padrão é 0)
# - fim: número onde a sequência termina (não incluído)
# - passo: intervalo entre os números (opcional, padrão é 1)

# Exemplo: imprimir os números de 0 a 4
for i in range(5):
    print("Número:", i)

# Exemplo: imprimir os números de 1 a 10
for i in range(1, 11):
    print("Contando de 1 a 10:", i)

# Exemplo: imprimir números pares de 0 a 10
for i in range(0, 11, 2):
    print("Número par:", i)


