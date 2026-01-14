# Definindo a função com controle total sobre como os argumentos são passados
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

"""
O QUE TÁ ROLANDO AQUI?

Essa função usa **duas “barreiras” especiais** nos parâmetros:

1. `/` → Tudo que vem **antes** dele só pode ser passado **por posição**
2. `*` → Tudo que vem **depois** dele só pode ser passado **por nome**

--- 

Então nesse caso:

- `modelo`, `ano`, `placa` → só podem ser passados na ordem, **sem nomear**
- `marca`, `motor`, `combustivel` → **obrigatoriamente nomeados** (tem que escrever `marca="Fiat"` etc.)

Essa é uma forma avançada de forçar um padrão de chamada: o início é posicional (pra evitar confusão), o resto é nomeado (pra clareza).
"""

# CHAMADA VÁLIDA:
# os 3 primeiros são passados por posição (como o '/' exige)
# os 3 últimos são nomeados (como o '*' exige)
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

# CHAMADA INVÁLIDA:
# Aqui estamos passando TUDO por nome, mas os 3 primeiros não podem
# Vai dar TypeError
# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

"""
RESUMO MENTAL:

| Parte da função   | Pode nomear? | Pode passar por posição? |
|-------------------|--------------|---------------------------|
| Antes do `/`      |  NÃO       |  SIM                    |
| Depois do `*`     |  SIM       |  NÃO                    |

---

PRA QUE SERVE ISSO?

- Evita chamadas confusas com parâmetros trocados
- Garante legibilidade e ordem onde for importante
- Muito usado em bibliotecas públicas, onde o autor quer **evitar mal uso da função**

---
ANALOGIA:

Imagina que tu tá fazendo uma compra:
- Primeiro tu precisa dizer o produto, a quantidade e o código — isso precisa vir na ordem certa (modelo, ano, placa).
- Depois, tu preenche as opções adicionais (marca, motor, combustível) por nome — como se estivesse preenchendo um formulário.

Assim o Python **te obriga a respeitar esse fluxo** e evita bagunça na chamada da função.
"""
