#Video assistido: https://www.youtube.com/watch?v=rfscVS0vtbw&t=2298s
#"Try/Except"

try:
    num = int(input("Insira um número: "))
    print(num)
except:
    #caso aconteça um erro
    #no bloco de comando dentro do try
    #o python vem direto para o except
    print("Inserção inválida")

#no caso acima ele irá para o except independente
#de qual erro aconteça mas você pode
#especificiar qual erro você quer pegar
try:
    value = 10/0
    num = int(input("Insira um número: "))
    print(num)
except ZeroDivisionError as err:
    #você pode armazenar o erro em uma varaivel
    #para poder mostra no console
    print(err)
except ValueError:
    print("Inserção inválida")