#Video assistido: https://www.youtube.com/watch?v=rfscVS0vtbw&t=2298s
#"Lists functions"

friends = ["Patrick","Jotas","Vitão","Bernas","Leo","Gustas","Erick"]
lucky_numbers = [78, 24, 47, 934, 52, 14, 63]

# friends.extend(lucky_numbers)
# print(friends)
#"Soma" as listas

friends.append("Them")
print(friends)
#Adiciona um valor no final da lista

friends.insert(1,"Them")
print(friends)
#Adiciona um valor na posição informada
#e empurra todos os outros valores
#para a direita

friends.remove("Them")
print(friends)
#Remove o primeiro valor informado

# friends.clear()
# limpa toda a lista

friends.pop()
print(friends)
#Elimina o ultimo elemento da lista

print(friends.index("Vitão"))
#Retorna a posição do valor informado

friends.count("Erick")
print(friends)
#Retorna quantas vezes o valor informado aparece

friends.sort()
print(friends)
#Ordena a lista em ordem alfabetica
#ou do maior pro menor

friends.reverse()
print(friends)
#Inverte a lista

friends2 = friends.copy()
print(friends2)