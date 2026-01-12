contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# .values() retorna todos os valores do dicionário
# Ou seja, só as infos dos contatos, sem os e-mails (que são as chaves)
# O resultado é um objeto dict_values, parecido com uma lista, mas mais leve e dinâmico
resultado = contatos.values()

print(resultado)
# Saída vai ser parecida com isso:
# dict_values([
#   {'nome': 'Guilherme', 'telefone': '3333-2221'}, 
#   {'nome': 'Giovanna', 'telefone': '3443-2121'}, 
#   {'nome': 'Chappie', 'telefone': '3344-9871'}, 
#   {'nome': 'Melaine', 'telefone': '3333-7766'}
# ])
# Se você adicionar ou remover um contato, esse objeto reflete automaticamente a mudança
# Por exemplo, se você adicionar um novo contato, o resultado vai incluir ele também
# Se você quiser ver os valores como uma lista, pode converter assim:
valores_lista = list(resultado)
# Isso transforma o dict_values em uma lista normal
print(valores_lista)
# Saída vai ser uma lista de dicionários:
# [
#   {'nome': 'Guilherme', 'telefone': '3333-2221'},
#   {'nome': 'Giovanna', 'telefone': '3443-2121},
#   {'nome': 'Chappie', 'telefone': '3344-9871},
#   {'nome': 'Melaine', 'telefone': '3333-7766}
# ]
