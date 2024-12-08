#Video assistido: https://www.youtube.com/watch?v=rfscVS0vtbw&t=2298s
#"Building a basic calculator"

num1 = input("Informe o segundo número: ")
num2 = input("Informe o primeiro número: ")
#recebe os números no tipo string
#então para realizar calculos se precisa
#transformar em int ou float

# result =  int(num1) + int(num2)
# o problema desse é que só aceita números inteiros

result = float(num1) + float(num2)
#

print("O resultado da soma foi: " + str(result))
#você precisa re-transformar em string para mostrar
#junto a uma mensagem