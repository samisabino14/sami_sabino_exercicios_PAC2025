import re as regex

with open("registos.txt", 'r', encoding='utf-8') as file:
    texto = file.read()

padrao_data = r"\b\d{2}/\d{2}/\d{4}\b"

datas = regex.findall(padrao_data, texto)

for data in datas:
    print(data)