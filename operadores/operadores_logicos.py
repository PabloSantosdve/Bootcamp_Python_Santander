#Operadores lógicos

# and (E)
print(True and True)    # True
print(True and False)   # False
#para ser TRUE tudo precisa ser TRUE


# or (O)
print(True or False)    # True  
print(False or False)   # False
#para ser TRUE apenas um precisa ser TRUE


#not (Não)
print(not True)         # False
print(not False)        # True

# Exemplo com variáveis:
idade = 20
tem_carteira = True
# Verifica se a pessoa pode dirigir
print(idade >= 18 and tem_carteira)  # True

saldo = 1000
saque = 250
limite = 200
conta_especial = True


# Verifica se o saque pode ser realizado:
# - Para contas comuns: saldo suficiente E saque dentro do limite
# - Para contas especiais: apenas saldo suficiente
exemplo = saldo >= saque and saque <- limite or conta_especial and saldo >= saque 


exemplo_2 = (saldo >= saque and saque <- limite) or (conta_especial and saldo >= saque) 
