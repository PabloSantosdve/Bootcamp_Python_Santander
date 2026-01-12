contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

# .items() retorna uma "visão" do dicionário em forma de pares (chave, valor)
# O resultado é um tipo especial chamado dict_items, que se comporta como uma lista de tuplas
# Cada tupla tem: (chave, valor)

resultado = contatos.items()

# Aqui vai imprimir algo assim:
# dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])
print(resultado)
# Se você quiser ver os pares de chave e valor, pode fazer um loop
for chave, valor in resultado:
    print(f"Chave: {chave}, Valor: {valor}")    
# Isso vai imprimir:
# Chave: