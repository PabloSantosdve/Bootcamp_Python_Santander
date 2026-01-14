robotica = {"Ana", "Bruno", "Carlos", "Daniela", "Fernanda", "Pablo"}
leitura = {"Carlos", "Daniela", "Eduarda", "Fernanda"}

# Alunos que participam das duas atividades
resultado1 = robotica.intersection(leitura)
print("Participam das duas atividades:", resultado1)

# Alunos que participam apenas da Oficina de Robótica
resultado2 = robotica.difference(leitura)
print("Somente na Oficina de Robótica:", resultado2)

# Alunos que participam de pelo menos uma das atividades
uniao = robotica.union(leitura)
print("Participam de pelo menos uma atividade:", uniao)
