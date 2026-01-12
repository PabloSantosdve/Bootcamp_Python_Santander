curso = "Curso de Python"      # Atribui a string "Curso de Python" à variável 'curso'
nome_curso = curso             # A variável 'nome_curso' recebe a mesma referência de 'curso' (apontam para o mesmo objeto na memória)

saldo, limite = 300, 251       # Atribui 300 para 'saldo' e 251 para 'limite' (dupla atribuição)

print(curso is nome_curso)            # Verifica se 'curso' e 'nome_curso' referenciam o mesmo objeto (retorna True, pois ambos apontam para a mesma string)

print(curso is not nome_curso)        # Verifica se 'curso' e 'nome_curso' não referenciam o mesmo objeto (retorna False, pois eles são o mesmo objeto)

print(saldo is limite)      # Verifica se 'saldo' e 'limite' referenciam o mesmo objeto (retorna False, pois são dois números diferentes)


a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)   # True, porque b aponta para o mesmo objeto que a
print(a is c)   # False, porque c é um objeto diferente, embora tenha o mesmo conteúdo