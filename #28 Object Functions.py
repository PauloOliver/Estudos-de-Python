#Video assistido: https://www.youtube.com/watch?v=rfscVS0vtbw&t=2298s
#"Object Functions"

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    #Você pode adicionar funções dentro das classes
    #para realizar calculos para você
    #nessa caso, toda "Pessoa" tem inbutido
    #o calculo se ela é maior de idade ou não

    def maior_idade(self):
        if self.idade >= 18:
            return True
        else:
            return False

pessoa1 = Pessoa("Carlos",18)
pessoa2 = Pessoa("Jasmine", 15)

print(Pessoa.maior_idade(pessoa2))