"""
Este código demonstra o uso de estruturas condicionais em Python: if, elif e else.

➡️ O que são?
São comandos que permitem ao programa tomar decisões com base em condições.

- `if` (se): executa um bloco de código se a condição for verdadeira.
- `elif` (senão se): testa uma nova condição se a anterior for falsa.
- `else` (senão): executa um bloco de código se todas as condições anteriores forem falsas.

➡️ Quando usar?
Use essas estruturas quando quiser que seu programa siga caminhos diferentes dependendo de valores ou situações específicas.
"""

# Exemplo: Verificar a faixa etária de uma pessoa com base na idade


idade = 25  # Definimos a idade da pessoa

if idade < 12:
    print("Você é uma criança.")  # Executa se a idade for menor que 12
elif idade < 18:
    print("Você é um adolescente.")  # Executa se a idade for entre 12 e 17
elif idade < 60:
    print("Você é um adulto.")  # Executa se a idade for entre 18 e 59
else:
    print("Você é um idoso.")  # Executa se a idade for 60 ou mais



#Exemplo da aula

MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer as aulas tóricas, mas não pode fazer as aulas praticas")
else:
    print("Ainda não pode tirar a CNH")




