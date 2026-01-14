contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Apaga a chave "telefone" do dicionário interno do contato "guilherme@gmail.com"
del contatos["guilherme@gmail.com"]["telefone"]

# Apaga todo o contato "chappie@gmail.com" do dicionário contatos
del contatos["chappie@gmail.com"]

# Agora, contatos ficou assim:
# {
#   'guilherme@gmail.com': {'nome': 'Guilherme'},
#   'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'},
#   'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}
# }
print(contatos)
# Se você tentar acessar uma chave que foi deletada, vai dar KeyError