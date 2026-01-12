"""
O que é o break em Python?
O break é uma instrução usada para interromper um loop antes que ele termine naturalmente. Ele é útil quando queremos sair de um for ou while assim que uma determinada condição for atendida.

Por exemplo, se estamos procurando um valor em uma lista e o encontramos, não faz sentido continuar procurando — então usamos break para sair do loop imediatamente.

"""

# Procurar um número específico em uma lista
numeros = [3, 7, 10, 15, 20, 25]
procurado = 15

for numero in numeros:
    print("Verificando número:", numero)
    if numero == procurado:
        print(f"Número {procurado} encontrado!")
        break  # Sai do loop assim que o número for encontrado


# Simulando uma tentativa de login com senha
senha_correta = "python123"
tentativas = 0

while True:
    entrada = input("Digite a senha: ")
    tentativas += 1

    if entrada == senha_correta:
        print("Acesso permitido!")
        break  # Sai do loop se a senha estiver correta
    else:
        print("Senha incorreta. Tente novamente.")

    if tentativas >= 3:
        print("Número máximo de tentativas atingido. Acesso bloqueado.")
        break  # Sai do loop após 3 tentativas


