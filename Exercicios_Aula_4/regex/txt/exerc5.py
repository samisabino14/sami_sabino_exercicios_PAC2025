import re as regex

with open("dados.txt", 'r', encoding='utf-8') as file:
    texto = file.read()

padrao = r"Nome:\s*([^,]+),\s*Email:\s*([^,]+),\s*Telemóvel:\s*([\d\- ]+)"

dados = regex.findall(padrao, texto)

with open("informacoes.txt", 'w', encoding='utf-8') as file:
    for nome, email, telemovel in dados:
        file.write(f"{nome.strip()} | {email.strip()} | {telemovel.strip()}\n")