import re as regex

with open("registos.txt", 'r', encoding='utf-8') as file:
    texto = file.read()

padrao_codigo = r"\b\d{4}-\d{3}\b"

codigos = regex.findall(padrao_codigo, texto)

for codigo in codigos:
    print(codigo)