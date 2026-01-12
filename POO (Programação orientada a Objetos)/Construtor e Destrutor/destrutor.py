class Cachorro:
    # Apenas o destrutor aqui, que é chamado quando o objeto é destruído
    def __del__(self):
        print("Removendo o cachorro da memória.")

    def falar(self):
        print("auau")


# Criando uma instância
c = Cachorro()

# Usando o método
c.falar()

# Deletando explicitamente
del c

# Código continua rodando aqui
print("O programa continua depois do del.")
# O destrutor será chamado automaticamente quando o objeto for destruído
# (ou seja, quando não houver mais referências a ele)   
# ou quando o programa terminar.
# Se você quiser ver o destrutor em ação, pode usar o comando `del` para remover a referência ao objeto.
# Isso é útil para liberar recursos ou fazer limpeza quando o objeto não é mais necessário.

#__del__: pode ser chamado ao deletar o objeto manualmente com del, ou automaticamente se ele sair do escopo (tipo dentro de uma função).