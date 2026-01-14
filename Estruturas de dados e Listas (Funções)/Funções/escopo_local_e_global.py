salario = 2000  # Variável global, tá fora da função

def salario_bonus(bonus):
    global salario  # Diz pra função usar a variável global 'salario', não criar uma nova local
    salario += bonus  # Soma o bônus no salário global
    return salario

salario_bonus(500)  # Agora salario virou 2500, porque foi atualizado globalmente
print(salario)  # Imprime 2500, que é o novo valor do salário global