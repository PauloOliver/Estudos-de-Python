#Video assistido: https://www.youtube.com/watch?v=rfscVS0vtbw&t=2298s
#"Writing to Files"

arquivo_BD = open("banco de dados.txt", "a")

arquivo_BD.write("\nPhilip- Empregado")
#Adiciona no final do arquivo
#\n serve pra quebrar a linha
arquivo_BD.close()

arquivo_BD1 = open("banco de dados1.html", "w")
#nesse caso como o arquivo não existe o python vai criar ele

arquivo_BD1.write("<h1>The return of them<h1>")
#e irá escrever o que está aqui
arquivo_BD1.close()