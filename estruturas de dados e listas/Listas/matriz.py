#Matrizes em Python são representadas como listas de listas. Cada sublista representa uma linha da matriz, e os elementos dentro dessas sublistas representam as colunas. Você pode acessar os elementos da matriz usando dois índices: o primeiro para a linha e o segundo para a coluna.
# Exemplo de matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Acessando elementos da matriz
print(matriz[0][0])  # 1 (primeira linha, primeira coluna)
print(matriz[1][2])  # 6 (segunda linha, terceira coluna)
print(matriz[2][1])  # 8 (terceira linha, segunda coluna)
# Modificando um elemento da matriz
matriz[0][1] = 10  # Modifica o elemento na primeira linha, segunda coluna
print(matriz)  # [[1, 10, 3], [4, 5, 6], [7, 8, 9]]
# Adicionando uma nova linha à matriz
matriz.append([10, 11, 12])  # Adiciona uma nova linha
print(matriz)  # [[1, 10, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# Adicionando uma nova coluna à matriz
for linha in matriz:
    linha.append(0)  # Adiciona um novo elemento (0) a cada linha
print(matriz)  # [[1, 10, 3, 0], [4, 5, 6, 0], [7, 8, 9, 0], [10, 11, 12, 0]]
# Iterando sobre a matriz
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"Elemento na posição ({i}, {j}): {matriz[i][j]}")
# Exemplo de matriz 2x3
matriz2 = [
    [1, 2, 3],
    [4, 5, 6]
]

matriz_aula = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz_aula[0])  # [1, "a", 2]
print(matriz_aula[0][0])  # 1
print(matriz_aula[0][-1])  # 2
print(matriz_aula[-1][-1])  # "c"