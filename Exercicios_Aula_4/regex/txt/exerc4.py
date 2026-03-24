import re as regex

with open("dados.txt", 'r', encoding='utf-8') as file:
    texto = file.read()

padrao_nome = r"Nome:\s*([^,]+)"

nomes = regex.findall(padrao_nome, texto)

for nome in nomes:
    print(nome)