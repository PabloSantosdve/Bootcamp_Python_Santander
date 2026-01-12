# O método .remove(valor) remove a primeira ocorrência do valor especificado na lista.
# Se o valor não estiver na lista, ocorre um erro (ValueError).
# Diferente de .pop(), que remove por índice, .remove() remove pelo conteúdo.

linguagens = ["python", "js", "c", "java", "csharp"]

# Remove o elemento "c" da lista.
linguagens.remove("c")

# Exibe a lista atualizada, sem o "c".
print(linguagens)  # Saída: ["python", "js", "java", "csharp"]
