#sintaxe basica herança multipla
#class A:
    #pass
#class B(A):
    #pass
#class C(A, B):
    #pass



# Classe base Animal
class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas  # Atributo comum a todos os animais

    def __str__(self):
        # Método especial que retorna uma string com o nome da classe e seus atributos
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


# Classe Mamifero herda de Animal (herança simples)
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo  # Atributo exclusivo dos mamíferos
        super().__init__(**kw)    # Chama o construtor da superclasse (Animal), passando os demais argumentos


# Classe Ave herda de Animal (herança simples)
class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico  # Atributo exclusivo das aves
        super().__init__(**kw)    # Chama o construtor da superclasse (Animal), passando os demais argumentos


# Classe Gato herda de Mamifero (herança simples em cadeia: Gato -> Mamifero -> Animal)
class Gato(Mamifero):
    pass  # Não adiciona nada novo, apenas herda os comportamentos e atributos


# Classe Ornitorrinco herda de Mamifero e Ave (herança múltipla)
class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        # super() segue a ordem da MRO (Method Resolution Order): Mamifero -> Ave -> Animal
        # Os argumentos são passados como palavras-chave para que cada classe receba o que precisa
        super().__init__(cor_bico=cor_bico, cor_pelo=cor_pelo, nro_patas=nro_patas)


# Criando um objeto da classe Gato
gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)  # Saída esperada: Gato: cor_pelo=Preto, nro_patas=4

# Criando um objeto da classe Ornitorrinco (que herda de Mamifero e Ave)
ornitorrinco = Ornitorrinco(nro_patas=4, cor_pelo="verde", cor_bico="laranja")
print(ornitorrinco)  # Saída esperada: Ornitorrinco: cor_pelo=vermelho, cor_bico=laranja, nro_patas=2
