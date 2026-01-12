"""
A instrução continue é usada dentro de loops (for ou while) para pular o restante do código naquela iteração e voltar para o início do loop. Ela é útil quando queremos ignorar certos casos sem interromper o loop completamente.

"""
# Exemplo: imprimir apenas números ímpares de 1 a 10

numero = 0

while numero < 10:
    numero += 1

    if numero % 2 == 0:
        continue  # pula os números pares

    print("Número ímpar:", numero)

