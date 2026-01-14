# O método .sort() ordena os elementos da lista em ordem crescente (padrão).
# Essa ordenação é feita diretamente na lista original (modifica a lista in-place).

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # Ordena em ordem alfabética
print(linguagens)  # Saída: ["c", "csharp", "java", "js", "python"]

# Podemos também ordenar em ordem decrescente usando o argumento reverse=True
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)
print(linguagens)  # Saída: ["python", "js", "java", "csharp", "c"]

# Agora usamos a opção 'key' para personalizar a forma como os itens são comparados.
# Usamos uma função lambda como critério de ordenação.

# O que é lambda?
# 'lambda' define uma função anônima (sem nome) de forma rápida e simples.
# Neste caso: lambda x: len(x) é uma função que recebe 'x' e retorna o comprimento de x.
# Isso significa que a lista será ordenada com base no tamanho de cada string.

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # Ordena da menor string para a maior
print(linguagens)  # Saída: ["c", "js", "java", "python", "csharp"]

# Podemos combinar a função lambda com reverse=True para ordenar do maior para o menor comprimento
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # Do mais longo para o mais curto
print(linguagens)  # Saída: ["python", "csharp", "java", "js", "c"]


#def func(x):
    #return len(x)