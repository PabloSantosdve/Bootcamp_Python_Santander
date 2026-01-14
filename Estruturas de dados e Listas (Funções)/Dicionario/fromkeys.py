# dict.fromkeys() cria um novo dicionário a partir de uma lista de chaves

# Neste exemplo, criamos um dicionário com as chaves "nome" e "telefone"
# Como não passamos valor padrão, o Python coloca None por padrão
# Isso é útil quando você quer preparar um dicionário "vazio", mas com as chaves já definidas
resultado = dict.fromkeys(["nome", "telefone"])
print(resultado)  # {'nome': None, 'telefone': None}

# Agora passamos o valor "vazio" como padrão
# Todas as chaves receberão esse valor
# Excelente pra inicializar algo com um estado padrão (tipo um formulário em branco, ou uma config inicial)
resultado = dict.fromkeys(["nome", "telefone"], "vazio")
print(resultado)  # {'nome': 'vazio', 'telefone': 'vazio'}

# Imagine que você tá montando um formulário onde cada campo começa vazio
campos = ["nome", "idade", "cidade"]
formulario = dict.fromkeys(campos, "")

print(formulario)
# Saída: {'nome': '', 'idade': '', 'cidade': ''}
