#Video assistido: https://www.youtube.com/watch?v=rfscVS0vtbw&t=2298s
#"Inheritance"

class Chefe:
    def prato_basico(self):
        print("Arroz, feijão, batata e carne")
    def prato_vegetariano(self):
        print("Arroz, feijão, salada e carne de soja")
    def prato_especial(self):
        print("Arroz, feijão, lasanha e macarrão")

class Chefe_Gourmet(Chefe):
    def prato_especial(self):
        print("Prate a la cozinhe")

chefeGourmet = Chefe_Gourmet()
chefeGourmet.prato_especial()