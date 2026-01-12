# Função principal que retorna outra função dependendo da operação passada
def calculadora(operacao):
    # Função interna que faz soma
    def soma(a, b):
        return a + b

    # Função interna que faz subtração
    def sub(a, b):
        return a - b

    # Função interna que faz multiplicação
    def mul(a, b):
        return a * b

    # Função interna que faz divisão
    def div(a, b):
        return a / b

    # Match-case é tipo um switch modernão (disponível desde Python 3.10)
    match operacao:
        case "+":  # Se o operador for "+"
            return soma  # Retorna a função soma (sem executar ainda)
        case "-":
            return sub
        case "*":
            return mul
        case "/":
            return div
        case _:
            return lambda a, b: "Operação inválida"

# Aqui a gente tá chamando a função `calculadora` com "+"
# Isso vai retornar a função `soma`, que fica guardada na variável `op`
op = calculadora("+")
print(op(2, 2))  # Agora a gente executa a função soma: 2 + 2 = 4

op = calculadora("-")  # Pega a função de subtração
print(op(2, 2))  # 2 - 2 = 0

op = calculadora("*")  # Multiplicação
print(op(2, 2))  # 2 * 2 = 4

op = calculadora("/")  # Divisão
print(op(2, 2))  # 2 / 2 = 1.0


"""
Ponto chave aqui:
Tu tá retornando uma função, e executando ela depois.
Isso é programação funcional, estilo mais limpo e modular.
Dá pra usar isso pra construir calculadoras, roteadores, comandos dinâmicos, e o que mais tua mente quiser.

"""