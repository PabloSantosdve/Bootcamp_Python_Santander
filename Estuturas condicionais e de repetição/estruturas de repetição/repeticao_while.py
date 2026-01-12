# A estrutura while repete um bloco de código enquanto uma condição for verdadeira.
# É útil quando não sabemos exatamente quantas vezes a repetição deve ocorrer.

# Exemplo: contar de 1 a 5 usando while
contador = 1  # inicializamos a variável
while contador <= 5:  # enquanto a condição for verdadeira, o loop continua
    print("Contador:", contador)
    contador += 1  # incrementamos para evitar loop infinito

# Outro exemplo: somar números até que o total ultrapasse 20
soma = 0
numero = 1
while soma <= 20:
    soma += numero
    print(f"Somando {numero}, total agora é {soma}")
    numero += 1
    
    
    

# Exemplo: verificar se um número é primo usando while/else
numero = 17
divisor = 2

# Um número é primo se não for divisível por nenhum número entre 2 e ele mesmo (exclusivo)
while divisor < numero:
    if numero % divisor == 0:
        print(f"{numero} não é primo. É divisível por {divisor}.")
        break  # Se acharmos um divisor, saímos do loop
    divisor += 1
else:
    # Esse bloco só será executado se o while terminar sem encontrar um divisor (sem break)
    print(f"{numero} é um número primo!")
