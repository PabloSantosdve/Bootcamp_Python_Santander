from datetime import date, datetime, timedelta

tipo_carro = "M"  # P (pequeno), M (médio), G (grande)
tempo_pequeno = 30  # aqui você usa *dias* como unidade, mas pelo nome parece que quer minutos, então cuidado!
tempo_medio = 45
tempo_grande = 60

data_atual = datetime.now()  # pega data e hora atuais

# Se você quer estimar quando o carro fica pronto, tem que somar o tempo ao horário atual,
# não subtrair (porque se subtrair, vai pra trás no tempo, tipo carro já pronto antes de chegar)
if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)  # soma 30 minutos
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)  # soma 45 minutos
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)  # soma 60 minutos
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")

# Aqui tá certo: subtrai 1 dia da data atual (ontem)
print(date.today() - timedelta(days=1))

# Subtrai 1 hora de um datetime específico e imprime só a hora resultante
resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

# Imprime a data de hoje, sem hora
print(datetime.now().date())

"""
timedelta aceita days, seconds, microseconds, milliseconds, minutes, hours, weeks.

Usar unidades erradas (ex: days=30 pra tempo que é em minutos) dá ruim.

Pra somar tempo, use + timedelta(...). Pra subtrair, - timedelta(...).

Se o tempo é curto, tipo minutos, melhor usar minutes=... e não days=....
"""