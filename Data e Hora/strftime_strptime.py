from datetime import datetime

data_hora_atual = datetime.now()  # pega a data e hora atual do sistema

data_hora_str = "2023-10-20 10:20"  # string representando data e hora

# Máscara pra formatar data no padrão BR com dia, mês, ano e abreviação do dia da semana
mascara_ptbr = "%d/%m/%Y %a"

# Máscara pra converter string pro formato datetime (ano, mês, dia, hora, minuto)
mascara_en = "%Y-%m-%d %H:%M"

# Converte data_hora_atual para string usando a máscara brasileira (printa algo tipo "16/07/2025 Wed")
print(data_hora_atual.strftime(mascara_ptbr))

# Converte a string data_hora_str para um objeto datetime usando a máscara em inglês
data_convertida = datetime.strptime(data_hora_str, mascara_en)

print(data_convertida)  # imprime o objeto datetime convertido (2023-10-20 10:20:00)
print(type(data_convertida))  # confirma que é do tipo datetime.datetime

"""
strftime() transforma objeto datetime em string formatada do jeito que quiser.

strptime() transforma string em objeto datetime, pra tu poder fazer contas e operações com datas.

As máscaras (%d, %m, %Y, %H, %M, %a) são códigos que representam pedaços da data/hora — tipo receita de bolo pra formatar ou interpretar.

Usar máscara errada vai dar erro ou conversão esquisita, então presta atenção.
"""