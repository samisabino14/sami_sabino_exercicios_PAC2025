import re as regex

with open("registos.txt", 'r', encoding='utf-8') as file:
    texto = file.read()

padrao_site = r"\b(?:www\.)?[\w\-]+\.\w+\b"

sites = regex.findall(padrao_site, texto)

for site in sites:
    print(site)