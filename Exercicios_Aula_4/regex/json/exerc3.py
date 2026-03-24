import json
import re

with open("dados.json", "r", encoding="utf-8") as file:
    dados = json.load(file)

padrao = r"https?://(?:www\.)?([^/]+)"

dominios = []

for registo in dados:
    site = registo.get("site", "")
    match = re.search(padrao, site)
    if match:
        dominios.append(match.group(1))

for d in dominios:
    print(d)
