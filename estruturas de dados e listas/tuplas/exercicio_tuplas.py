cores = (
    "vermelho",
    "azul",
    "verde",
    "amarelo",
    "roxo",
)

print(cores)
print(cores[1])

elemento = "verde"

if elemento in cores:
    print(f"A cor {elemento}, existe na tupla {cores}")
else:
    print("Não existe essa cor")

print(cores.count("azul"))
print(cores.index("amarelo"))


# Tupla com dados dos alunos: (nome, idade, nota final)
alunos = (
    ("Ana", 20, 8.5),
    ("Bruno", 22, 7.0),
    ("Carla", 19, 9.2),
    ("Diego", 21, 6.8),
    ("Elisa", 20, 8.9),
)

# 1. Imprimir todos os alunos com suas informações
print("Lista de alunos:")
for aluno in alunos:
    nome, idade, nota = aluno
    print(f"Nome: {nome}, Idade: {idade}, Nota: {nota}")

# 2. Calcular a média das notas finais
soma_notas = 0
for aluno in alunos:
    nota = aluno[2]
    soma_notas += nota

media = soma_notas / len(alunos)
print(f"\nMédia das notas finais: {media:.2f}")

# 3. Encontrar o aluno com a maior nota
maior_nota = 0
melhor_aluno = ""

for aluno in alunos:
    nome = aluno[0]
    nota = aluno[2]
    if nota > maior_nota:
        maior_nota = nota
        melhor_aluno = nome

print(f"\nAluno com a maior nota: {melhor_aluno} ({maior_nota})")

# 4. Criar uma lista com nomes dos alunos com nota acima de 8.0
aprovados = []

for aluno in alunos:
    nome = aluno[0]
    nota = aluno[2]
    if nota > 8.0:
        aprovados.append(nome)

print(f"\nAlunos com nota acima de 8.0: {aprovados}")
