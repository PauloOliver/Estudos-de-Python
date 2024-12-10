#Video assistido: https://www.youtube.com/watch?v=rfscVS0vtbw&t=2298s
#"Reading Files"

arquivo_BD = open("banco de dados.txt", "r")
# Existem vários modos                  ^^^
#r = read, você só lê o arquivo
#w = write, você pode modificar(adicionar, apagar, mudar) o arquivo
#a = append, você pode apenas adicionar informação no final do arquivo
#r+ = read & write, a junção dos dois

print(arquivo_BD.readable())
#Retorna um boolean, se é possivel ler ou não

print(arquivo_BD.read())
#Lê o que tem no arquivo

print(arquivo_BD.readlines()[1])
#Lê o arquivo e armazena as informações dentro de uma lista
#Além de te permitir especificar qual linha você quer ler

#Um erro acontece se você executar o programa
#Provavelmente porque o .read lê o arquivo inteiro
#e quando o .readlines tenta ler também o arquivo
#"já acabou" pois chegou na ultima linha

arquivo_BD.close()
#SEMPRE feche o arquivo no final