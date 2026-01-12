from datetime import datetime, timedelta, timezone

# Cria um datetime com timezone fixo de +2 horas (tipo horário de verão Europa/Oslo)
data_oslo = datetime.now(timezone(timedelta(hours=2)))

# Cria um datetime com timezone fixo de -3 horas (horário de São Paulo, Brasil)
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

print(data_oslo)     # imprime data/hora atual com offset +02:00
print(data_sao_paulo)  # imprime data/hora atual com offset -03:00

"""
timezone(timedelta(...)) cria um fuso horário fixo com o deslocamento especificado (sem DST).

Diferente do pytz, não leva em conta horário de verão — é só deslocamento fixo.

Bom pra casos simples, logs, testes ou onde não precisa de ajuste fino.
"""