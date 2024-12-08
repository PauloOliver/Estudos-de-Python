#Video assistido: https://www.youtube.com/watch?v=rfscVS0vtbw&t=2298s
#"Variables and data types" até "Working with strings"
variable_string = "them"
variable_number = 31.31
variable_boolean = True

print("the return of " + variable_string)

phrase_uppercase = "Very cool phrase"

#Nenhuma função altera a variavel original
#nos exemplos abaixo
#Para alterar se deve botar em uma variavel
#convertido_phrase = phrase_uppercase.upper()

print(phrase_uppercase.upper())

print(phrase_uppercase.isupper())
#Ele checa se TODOS os characteres estão em upper case

print(phrase_uppercase.upper().isupper())
#Você pode botar uma função atrás da outra

phrase = "The Return of Them"
print(len(phrase))
#Mostra o tamanho da variavel CONTANDO com os espaços

print(phrase[0])
#Imprime o charctere na posição definida (nesse caso 0)
#Lembrando que o primeiro charactere é a posição 0

print(phrase.index("T"))
#Ele procura a primeira posição onde
#aparece os characteres informados
#e retorna essa posição

print(phrase.index("Them"))
#Pode procurar por frases também

#Segundo o bot é melhor usar .find()
#faz a mesma coisa mas se não achar o character
#ele retorna -1 ao inves de dar erro

print(phrase.find("Them"))
print(phrase.find("Charlie"))

print(phrase.replace("Them", "Charlie"))
