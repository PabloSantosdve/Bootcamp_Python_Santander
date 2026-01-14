contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

# .keys() retorna todas as chaves do dicionário
# O retorno é um objeto do tipo dict_keys, que se parece com uma lista, mas é mais leve e dinâmico
# Se você adicionar ou remover uma chave do dicionário depois, esse objeto reflete automaticamente a mudança

resultado = contatos.keys()

# Vai imprimir: dict_keys(['guilherme@gmail.com'])
# Isso mostra que temos uma única chave no dicionário, que é o e-mail
print(resultado)
# Se você quiser ver as chaves como uma lista, pode converter assim:
chaves_lista = list(resultado)
# Isso transforma o dict_keys em uma lista normal
print(chaves_lista)  # Saída: ['