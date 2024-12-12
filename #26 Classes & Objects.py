#Video assistido: https://www.youtube.com/watch?v=rfscVS0vtbw&t=2298s
#"Classes & Objects"

#Classe é a mesma coisa do python (até onde eu entendi)
#Basicamente classe é um data type e é o que define os atributos
#e objeto é um data type já definido
#Exemplo:
#Uma classe "pessoa" pode ter nome e idade
#Quando você cria uma "pessoa" e adiciona o valor
#nome = joão e idade = 20
#isso é um objeto

class mago:
    def __init__(self, nome, idade, escola_de_magia, e_suporte):
        #Se você conhece constructor em JS
        #é basicamente a mesma ideia
        self.nome = nome
        self.idade = idade
        self.escola_de_magia = escola_de_magia
        self.e_suporte = e_suporte


mago_gelo = mago("Kalindor",253,"Gelo",False)

print(mago_gelo)