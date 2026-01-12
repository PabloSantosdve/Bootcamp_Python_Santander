contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

# .update() atualiza o dicionário com os pares chave:valor do dicionário passado como argumento
# Se a chave já existir, ela **sobrescreve** o valor antigo pelo novo
contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})

# Agora a entrada do "guilherme@gmail.com" foi atualizada, o telefone sumiu porque você sobrescreveu o dicionário inteiro
print(contatos)  # {'guilherme@gmail.com': {'nome': 'Gui'}}

# Se a chave NÃO existir, .update() adiciona ela normalmente
contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})

# Agora o dicionário tem os dois contatos: Guilherme (atualizado) e Giovanna (novo)
print(contatos)
# {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
