from datetime import datetime, date, time  # importando as classes que vão manipular datas e horas

# Criando uma data específica
data = date(2027, 7, 17) # criando uma data específica (ano, mês, dia)
print(data)  # imprime 2027-07-17

# Data e hora atual
print(date.today())  # imprime algo como 2025-07-17 16:42:10.123456, imprime a data atual do sistema (hoje)

# Criando data e hora (hora padrão: 00:00:00)
data_hora = datetime(2023, 7, 10)
print(data_hora)  # imprime 2023-07-10 00:00:00

# Criando hora isolada
hora = time(10, 20, 0) #Hora = (Hora, minutos e segundos)
print(hora)  # imprime 10:20:00

"""
date é só data (ano, mês, dia).

time é só hora (hora, minuto, segundo).

datetime junta os dois (data + hora).

today() é um método que pega o tempo atual do sistema (pra data ou datetime).
"""