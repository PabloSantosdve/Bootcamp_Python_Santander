# RETURN EM FUNÇÕES PYTHON

# O comando 'return' é usado dentro de uma função para devolver um valor como resultado da execução.
# Quando a função encontra um 'return', ela finaliza sua execução e retorna o valor especificado.
# Esse valor pode ser armazenado em uma variável, usado em cálculos ou exibido diretamente.

# Exemplo 1: Função que retorna a soma de dois números
def somar(a, b):
    return a + b  # Retorna o resultado da soma

# Podemos armazenar o retorno em uma variável
resultado = somar(5, 3)
print("Resultado da soma:", resultado)  # Saída: 8

# Exemplo 2: Função que verifica se um número é par
def eh_par(numero):
    return numero % 2 == 0  # Retorna True se for par, False se for ímpar

print(eh_par(4))  # Saída: True
print(eh_par(7))  # Saída: False

# Exemplo 3: Função com múltiplos retornos
def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

print(dividir(10, 2))  # Saída: 5.0
print(dividir(10, 0))  # Saída: Erro: divisão por zero

# DICA: Após o 'return', nada mais dentro da função será executado.
# Ele encerra a função imediatamente.


# Função que recebe uma lista de números e retorna a soma total
def calcular_total(numeros):
    return sum(numeros)  # sum() soma todos os elementos da lista

# Função que recebe um número e retorna uma tupla com o antecessor e sucessor
def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    # Retorna os dois valores juntos, como uma tupla (antes, depois)
    return antecessor, sucessor

# Chamando a função que soma a lista [10, 20, 34]
print(calcular_total([10, 20, 34]))  # Saída: 64

# Chamando a função que retorna antecessor e sucessor de 10
print(retorna_antecessor_e_sucessor(10))  # Saída: (9, 11)
# Chamando a função que retorna antecessor e sucessor de 100
print(retorna_antecessor_e_sucessor(100))  # Saída: (99, 101)