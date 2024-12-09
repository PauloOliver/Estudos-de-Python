#Video assistido: https://www.youtube.com/watch?v=rfscVS0vtbw&t=2298s
#"Dictionaries"

conversao_mes = {
    "Jan": "Janeiro",
    "Fev": "Fevereiro",
    "Mar": "Março",
    "Abr": "Abril",
    "Maio": "Maio",
    "Jun": "Junho",
    "Jul": "Julho",
    "Ago": "Agosto",
    "Set": "Setembro",
    "Out": "Outubro",
    "Nov": "Novembro",
    "Dez": "Dezembro"
}

print(conversao_mes["Dez"])
print(conversao_mes.get("out", "Erro!")) 
#Com o .get você consegue botar uma mensagem de erro
#e funciona igual a primeira opção

