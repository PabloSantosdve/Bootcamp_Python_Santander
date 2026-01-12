# Recebe a quantidade de pacientes
n = int(input().strip())

# Lista para guardar os pacientes como tuplas: (nome, idade, status)
pacientes = []

# Coleta os dados de cada paciente
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)  # transforma idade em número
    pacientes.append((nome, idade, status))

# Função que define a "prioridade" de cada paciente
def prioridade(paciente):
    nome, idade, status = paciente

    # Casos urgentes têm a prioridade máxima (0), e entre eles o mais velho vem primeiro
    if status == "urgente":
        return (0, -idade)  # quanto mais velho, maior a prioridade
    # Idosos normais vêm depois dos urgentes
    elif idade >= 60:
        return (1, 0)
    # O restante vem por último
    else:
        return (2, 0)

# Ordena a lista de pacientes com base na prioridade definida
pacientes_ordenados = sorted(pacientes, key=prioridade)

# Extrai só os nomes dos pacientes ordenados
nomes_ordenados = [paciente[0] for paciente in pacientes_ordenados]

# Exibe o resultado formatado
print("Ordem de Atendimento:", ", ".join(nomes_ordenados))



#Desafio 2
def processar_reservas():
    # Lê os quartos disponíveis e transforma em um set pra busca rápida
    quartos_disponiveis = set(map(int, input().split()))
    
    # Lê os quartos solicitados pelos clientes
    reservas_solicitadas = list(map(int, input().split()))

    # Listas para guardar os resultados
    confirmadas = []
    recusadas = []

    # Verifica cada reserva solicitada
    for reserva in reservas_solicitadas:
        if reserva in quartos_disponiveis:
            confirmadas.append(reserva)            # Confirma a reserva
            quartos_disponiveis.remove(reserva)    # Remove o quarto da lista (já foi reservado)
        else:
            recusadas.append(reserva)              # Reserva recusada (quarto não existe ou já foi reservado)

    # Exibe os resultados conforme especificação
    print("Reservas confirmadas:", " ".join(map(str, confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, recusadas)))

# Chamada da função para rodar o sistema
processar_reservas()
