# Função que soma dois números e retorna o resultado
def somar(a, b):
    return a + b

# Função que recebe dois números e uma função como parâmetro
# Ela chama a função recebida, passando os dois números
# Depois imprime o resultado retornado por essa função
def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

# Chamada da função exibir_resultado
# Passa os números 10 e 10, e a função somar
# A função somar será executada com os valores 10 e 10
exibir_resultado(10, 10, somar)  # Saída: O resultado da operação 10 + 10 = 20

# Função que recebe uma lista de números e retorna a soma total
# Utiliza a função sum(), que soma todos os elementos de um iterável
def calcular_total(numeros):
    return sum(numeros)

# Função que recebe um número e retorna uma tupla com:
# - o antecessor (número - 1)
# - o sucessor (número + 1)
# A tupla agrupa os dois valores como um único retorno
def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

#Quando usar ? Exemplo real
"""
Imagina que você tem uma função que aplica diferentes tipos de desconto sobre o valor de um pedido.
Cada tipo de cliente (normal, VIP, black friday, etc.) pode ter uma lógica diferente de desconto.

Você quer uma função genérica que:
receba o valor do pedido e aplique a lógica de desconto que você passar (como função)

"""
print("Exemplo de uso de funções de primeira classe com descontos:")
# Funções de desconto
def desconto_padrao(valor):
    return valor * 0.95  # 5% de desconto

def desconto_vip(valor):
    return valor * 0.90  # 10% de desconto

def desconto_black_friday(valor):
    return valor * 0.80  # 20% de desconto

# Função genérica que recebe o valor e uma função de desconto
def aplicar_desconto(valor, funcao_desconto):
    valor_final = funcao_desconto(valor)
    print(f"Valor original: R${valor:.2f}")
    print(f"Valor com desconto: R${valor_final:.2f}")

# Exemplo de uso:
aplicar_desconto(100.00, desconto_padrao)        # Cliente comum
aplicar_desconto(100.00, desconto_vip)           # Cliente VIP
aplicar_desconto(100.00, desconto_black_friday)  # Promoção especial
