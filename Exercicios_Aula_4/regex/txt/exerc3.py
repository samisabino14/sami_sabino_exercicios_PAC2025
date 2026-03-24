import re as regex

with open("dados.txt", 'r', encoding='utf-8') as file:
    texto = file.read()

padrao_telefone = r"\b\d{3}[- ]?\d{3}[- ]?\d{3}\b"

telefones = regex.findall(padrao_telefone, texto)

for telefone in telefones:
    print(telefone)