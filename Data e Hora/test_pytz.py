from datetime import datetime
import pytz  # lib top pra lidar com timezone, porque o datetime padrão não tem fuso completo

# Pega data e hora atual no fuso da Europa, Oslo
data = datetime.now(pytz.timezone("Europe/Oslo"))

# Pega data e hora atual no fuso de São Paulo (Brasil)
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

# Imprime os dois datetimes com seus fusos horários explícitos
print(data)   # ex: 2025-07-16 18:43:12.123456+02:00
print(data2)  # ex: 2025-07-16 13:43:12.123456-03:00

"""
datetime.now() normal pega a hora local do seu computador, sem fuso fixo.

Com pytz.timezone(...) você força a hora de um fuso específico, tipo Oslo ou São Paulo.

O resultado tem o offset do fuso (o +02:00 ou -03:00) junto — essencial pra apps que precisam lidar com horário global (ex: chat, eventos, logs).

pytz é meio padrão ouro pra timezone em Python, apesar do módulo zoneinfo do Python 3.9+ ser oficial agora.
"""