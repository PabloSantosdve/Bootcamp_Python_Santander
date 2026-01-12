# Criamos uma lista com três elementos:
# - um número inteiro (1)
# - uma string ("Python")
# - outra lista aninhada ([40, 30, 20])
lista = [1, "Python", [40, 30, 20]]

# O método .copy() cria uma cópia rasa (shallow copy) da lista.
# Isso significa que ele copia os elementos da lista principal,
# mas se algum elemento for uma lista (ou outro objeto mutável), ele NÃO copia seu conteúdo,
# apenas referencia a mesma sublista na memória.
lista.copy()  # Aqui, a cópia foi feita, mas não foi armazenada em nenhuma variável.

# Como a cópia não foi guardada, esse comando apenas imprime a lista original.
print(lista)  # Saída: [1, "Python", [40, 30, 20]]


"""
Nota importante:
O método .copy() por si só não altera a lista original — ele retorna uma nova lista copiada. Como você não armazenou essa cópia em uma variável, ela foi criada e imediatamente descartada.
"""