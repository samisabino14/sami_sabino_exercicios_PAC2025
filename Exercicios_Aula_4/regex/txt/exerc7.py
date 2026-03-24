import re as regex

with open("registos.txt", 'r', encoding='utf-8') as file:
    texto = file.read()

padrao_nif = r"\bNIF\b:\n*([^|]+)"

nifs = regex.findall(padrao_nif, texto)

for nif in nifs:
    print(nif)