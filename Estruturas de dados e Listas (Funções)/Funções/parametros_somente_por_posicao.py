# Definindo a função com controle total sobre como os argumentos devem ser passados
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

"""
ENTENDENDO O '/' 

Esse símbolo '/' diz o seguinte:
"Tudo o que vem ANTES de mim só pode ser passado POR POSIÇÃO."

Ou seja:
- modelo, ano, placa ➜ só podem ser passados na ordem certa, sem usar nome (ex: criar_carro("Palio", 1999, "ABC-1234"))
- marca, motor, combustivel ➜ podem ser passados por nome normalmente (ex: marca="Fiat")

É como se o Python dissesse: “os primeiros valores vêm na sequência obrigatória, os outros você pode nomear pra deixar claro quem é quem.”
"""

# Chamada correta:
# Os três primeiros argumentos são passados por posição, como mandado pelo '/'
# Os últimos três são passados por nome (isso ajuda na clareza)
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

"""
Chamada inválida (vai dar erro):
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

Isso dá erro porque 'modelo', 'ano' e 'placa' estão sendo passados por nome.
Mas o '/' exige que eles sejam passados por posição (sem nomear).
"""

"""
RESUMÃO DAS IDEIAS:

- Antes do '/' → só pode usar argumentos posicionais (ordem importa, nomes proibidos)
- Depois do '/' → pode usar argumentos nomeados normalmente
- Útil pra evitar confusões e garantir que funções sejam chamadas corretamente
- Muito usado em bibliotecas públicas, APIs, ou onde ordem importa MUITO

Quer deixar tudo mais rígido ainda? Dá pra usar o '*' também, pra forçar o contrário:
Exemplo:
def exemplo(a, /, b, *, c):
    - a: só por posição
    - b: pode ser por posição ou nome
    - c: só por nome
"""

# Se quiser testar diferentes chamadas e ver onde quebra ou funciona, troca os parâmetros e roda!
