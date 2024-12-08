#Video assistido: https://www.youtube.com/watch?v=rfscVS0vtbw&t=2298s
#"If Statement & comparisons"

def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

#== iguais
#!= diferente
#> maior que
#< menor que

print("O maior número: " + str(max_num(200,150, 300)))