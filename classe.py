class pessoa:
    def __init__(self, nome, idade): #init utilizado quando se usa um objeto
        self.nome = nome #nomeia o objeto
        self.idade = idade #nomeia o objeto

    def apresentar(self):
        print("ola meu nome é ", self.nome)
pessoa1 = pessoa("Gabriel", 21)
pessoa1.apresentar()


class animal:
    def latir(self):
        return "au"
      
class cachorro(animal):
    def latir(self):
        return "auuu"


teste1 = animal()
teste2 = cachorro()


print(teste1.latir())
print(teste2.latir())

class pc:
    def notfic(self):
        print("dandan")
class placa(pc):
    def notfic(self):
        super().notfic()
        print("blanblan")

usuario = placa()
usuario.notfic()

class calculadora:
    def somar(self, a, b, c=0):
        return a + b + c
soma1 = calculadora()
soma2 = calculadora()
print(soma1.somar(10,20))
print(soma2.somar(10, 20, 30))