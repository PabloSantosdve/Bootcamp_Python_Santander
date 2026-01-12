"""
Este código demonstra o uso de estruturas condicionais aninhadas em Python.

O que são?
São estruturas onde um bloco `if`, `elif` ou `else` contém outro `if` dentro dele. Isso permite decisões mais detalhadas e específicas.

Quando usar?
Use estruturas aninhadas quando precisar verificar uma condição **dentro de outra**, como por exemplo: "Se a pessoa for adulta, verificar se ela é jovem ou idosa".

"""

# Exemplo: Verificar a faixa etária e o turno de trabalho de uma pessoa

idade = 30
turno = "noite"  # Pode ser: manhã, tarde ou noite

if idade >= 18:
    print("Você é maior de idade.")

    if turno == "manhã":
        print("Você trabalha no turno da manhã.")
    elif turno == "tarde":
        print("Você trabalha no turno da tarde.")
    else:
        print("Você trabalha no turno da noite.")
else:
    print("Você é menor de idade.")



"""
Sistema Bancário Simples com Condicionais Aninhadas

O que o código faz?
Simula um sistema bancário com três operações: saque, depósito e consulta de saldo.
Utiliza estruturas condicionais aninhadas (`if` dentro de `if`) para verificar a operação e validar os dados.

Quando usar condicionais aninhadas?
Quando você precisa tomar decisões dentro de outras decisões, como validar saldo antes de sacar.
"""

saldo = 1000  # Define o saldo inicial da conta bancária

operacao = "saque"  # Define a operação que o usuário deseja realizar: 'saque', 'deposito' ou 'saldo'
valor = 200  # Valor que será usado na operação (saque ou depósito)

# Verifica qual operação o usuário deseja
if operacao == "saque":  # Se a operação for 'saque'
    print("Operação: Saque")

    # Verifica se há saldo suficiente para realizar o saque
    if valor <= saldo:
        saldo -= valor  # Subtrai o valor do saldo
        print(f"Saque de R${valor:.2f} realizado com sucesso.")  # Confirma o saque
        print(f"Saldo atual: R${saldo:.2f}")  # Mostra o saldo restante
    else:
        print("Saldo insuficiente para saque.")  # Informa que não há saldo suficiente

elif operacao == "deposito":  # Se a operação for 'deposito'
    print("Operação: Depósito")

    # Verifica se o valor do depósito é válido (maior que zero)
    if valor > 0:
        saldo += valor  # Adiciona o valor ao saldo
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")  # Confirma o depósito
        print(f"Saldo atual: R${saldo:.2f}")  # Mostra o novo saldo
    else:
        print("Valor de depósito inválido.")  # Informa que o valor é inválido

elif operacao == "saldo":  # Se a operação for 'saldo'
    print(f"Seu saldo atual é: R${saldo:.2f}")  # Mostra o saldo atual

else:
    print("Operação inválida.")  # Caso a operação não seja reconhecida
