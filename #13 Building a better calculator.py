#Video assistido: https://www.youtube.com/watch?v=rfscVS0vtbw&t=2298s
#"Building a better calculator"
#Versão bem diferente do curso
#Queria usar mais ferramentas do que o que foi mostrado

num1 = float(input("Informe o primeiro valor: "))
op = input("Informe o operador (Soma: +, Subtração: -, Multiplicação: *, Divisão: /): ")
num2 = float(input("Informe o segundo valor: "))

def calcular(num1,num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1/num2

print(calcular(num1,num2))