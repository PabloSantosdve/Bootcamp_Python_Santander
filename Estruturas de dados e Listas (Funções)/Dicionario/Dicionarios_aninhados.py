# DICIONÁRIOS ANINHADOS EM PYTHON

# Um dicionário aninhado é um dicionário que contém outros dicionários como valores.
# Isso permite representar dados mais complexos, como registros de pessoas, produtos, alunos, etc.

# Exemplo: agenda de contatos onde cada e-mail é uma chave,
# e o valor é outro dicionário com nome e telefone da pessoa.
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# ACESSANDO DADOS
# Para acessar o telefone da Giovanna, usamos duas chaves:
telefone_gi = contatos["giovanna@gmail.com"]["telefone"]
print("Telefone da Giovanna:", telefone_gi)

# MODIFICANDO DADOS
# Podemos alterar qualquer valor dentro do dicionário aninhado:
contatos["chappie@gmail.com"]["nome"] = "Chaplin"

# ADICIONANDO UM NOVO CONTATO
contatos["novo@email.com"] = {"nome": "Novo Contato", "telefone": "9999-0000"}

# REMOVENDO UM CONTATO
del contatos["melaine@gmail.com"]

# PERCORRENDO O DICIONÁRIO
# Podemos percorrer todos os contatos e exibir suas informações:
print("\nLista de contatos:")
for email, info in contatos.items():
    print(f"Email: {email}")
    print(f"Nome: {info['nome']}")
    print(f"Telefone: {info['telefone']}")
    print("-" * 20)

# OUTRO EXEMPLO: DICIONÁRIO COM LISTAS COMO VALORES
# Aqui usamos dicionários aninhados para armazenar notas de alunos
alunos = {
    "Ana": {"notas": [8.5, 9.0, 7.5]},
    "Bruno": {"notas": [6.0, 7.0, 8.0]},
}

# Calculando a média das notas da Ana
media_ana = sum(alunos["Ana"]["notas"]) / len(alunos["Ana"]["notas"])
print(f"\nMédia das notas da Ana: {media_ana:.2f}")

# Verificando se um aluno está cadastrado
if "Bruno" in alunos:
    print("Bruno está cadastrado no sistema.")
