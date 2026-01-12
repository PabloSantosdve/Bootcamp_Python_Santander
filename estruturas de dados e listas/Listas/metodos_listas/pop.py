# O método .pop() remove e retorna o último elemento da lista por padrão.
# Também é possível informar o índice do elemento que se deseja remover.
# Cada vez que um item é removido, a lista se atualiza automaticamente.

linguagens = ["python", "js", "c", "java", "csharp"]

# Remove e retorna o último elemento: "csharp"
print(linguagens.pop())  # Saída: csharp

# Agora a lista é ["python", "js", "c", "java"]
# Remove e retorna o novo último elemento: "java"
print(linguagens.pop())  # Saída: java

# Agora a lista é ["python", "js", "c"]
# Remove e retorna "c"
print(linguagens.pop())  # Saída: c

# Agora a lista é ["python", "js"]
# Remove e retorna o elemento no índice 0: "python"
print(linguagens.pop(0))  # Saída: python
