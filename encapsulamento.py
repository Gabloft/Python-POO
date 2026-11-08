class pessoa:
    def __init__ (self, nome, idade, cpf):
        self.nome = nome
        self._idade = idade
        self.__cpf = cpf

    def mostrar_idade(self):
        print(self._idade)
        
    def mostrar_cpf(self):
        print(self.__cpf)

   
pessoa1 = pessoa("gabriel", 18, 210600240)
pessoa1.mostrar_idade()
print(pessoa1.nome)
pessoa1.mostrar_cpf()

class animal:
    def __init__(self):
     self._idade = 0
    def get_idade(self):
        return self._idade
    def set_idade(self, idade):
        if idade >=0:
            self._idade = idade
bixo1 = animal()
bixo1.set_idade(20)
print(bixo1.get_idade())

class carro:
    def __init__(self, modelo, cor, ano):
          self.modelo = modelo
          self.cor = cor
          self.ano = ano
    def __str__(self):
        
        return f'{self.modelo} - {self.cor} - {self.ano}'
    def __repr__(self):
        return f'carro({self.modelo}, {self.cor}, {self.ano})'


carro1 = carro("fiat", "preto", 2007)
print(carro1)        
print(repr(carro1))

