import json
import re

with open("dados.json", "r", encoding="utf-8") as file:
    dados = json.load(file)

padrao_nif = r"^[123568]\d{8}$"

for registo in dados:
    nif = registo.get("nif", "").strip()

    if re.match(padrao_nif, nif):
        print(f"{nif} é válido")
    else:
        print(f"{nif} é inválido")
