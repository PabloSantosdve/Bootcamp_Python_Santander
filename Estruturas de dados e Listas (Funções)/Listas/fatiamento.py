#Fatiamento em python, é uma forma super útil de pegar partes de listas (ou strings, tuplas, etc)
lista = [10, 20, 30, 40, 50, 60, 70]
fatia = lista[1:4] # começa no índice 1, vai até o 3 (4 não incluído)
print(fatia)  # saída: [20, 30, 40]

""" 
lista[início:fim:passo]
início: índice onde começa (padrão é 0)

fim: índice onde para (não inclui esse índice)

passo: quanto pula a cada elemento (padrão é 1)
"""
print(lista[:3])    # primeiros 3 elementos: [10, 20, 30]
print(lista[2:])    # do índice 2 até o final: [30, 40, 50, 60]
print(lista[::2])   # pega elementos pulando de 2 em 2: [10, 30, 50]
print(lista[::-1])  # lista invertida: [60, 50, 40, 30, 20, 10]

#Com listas aninhadas
matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(matriz[1][1:3])  # da segunda linha, elementos índice 1 até 2: [6, 7]

lista1 = ["p", "y", "t", "h", "o", "n"]

print(lista1[2:])  # ["t", "h", "o", "n"]
print(lista1[:2])  # ["p", "y"]
print(lista1[1:3])  # ["y", "t"]
print(lista1[0:3:2])  # ["p", "t"]
print(lista1[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista1[::-1])  # ["n", "o", "h", "t", "y", "p"]