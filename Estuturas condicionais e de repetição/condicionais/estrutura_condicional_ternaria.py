"""
Exemplo simples de operador ternário em Python

O que é?
É uma forma compacta de escrever uma estrutura condicional `if-else` em uma única linha.

Sintaxe:
resultado = valor_se_verdadeiro if condição else valor_se_falso

Quando usar?
Quando você precisa tomar uma decisão simples e atribuir um valor com base em uma condição.
"""

# Exemplo: Verificar se um número é par ou ímpar
numero = 7

# Usando operador ternário para decidir a mensagem
mensagem = "O número é par." if numero % 2 == 0 else "O número é ímpar."

print(mensagem)

#Outro exemplo mais simples

saldo = 2000
saque = 2500
# Verifica se o saldo é suficiente para realizar o saque
status = "Sucesso" if saldo >= saque else "Falha"

# Exibe o resultado da operação
print(f"{status} ao realizar o saque!")
