# Dicionário com um único contato
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

# .copy() faz uma CÓPIA RASA do dicionário
# Ou seja: ele copia só o nível de fora (as chaves principais),
# mas os valores internos (os dicionários com nome e telefone) ainda são os MESMOS objetos na memória.
copia = contatos.copy()

# Aqui, a gente sobrescreve o valor da chave "guilherme@gmail.com" na cópia
# Mas a gente tá trocando o valor TODO, então não afeta o original
copia["guilherme@gmail.com"] = {"nome": "Gui"}

# O original permanece intacto, porque trocamos o valor por completo na cópia
print(contatos["guilherme@gmail.com"])  # {"nome": "Guilherme", "telefone": "3333-2221"}

# A cópia agora tem um novo valor, diferente do original
print(copia["guilherme@gmail.com"])  # {"nome": "Gui"}
