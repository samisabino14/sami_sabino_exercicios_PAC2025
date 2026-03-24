import json
import re

with open("dados.json", "r", encoding="utf-8") as file:
    dados = json.load(file)

padrao_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"
padrao_nif = r"^[123568]\d{8}$"

registos_validos = []

for reg in dados:
    email = reg.get("email", "").strip()
    nif = reg.get("nif", "").strip()
    telemovel = reg.get("telemovel", "")

    digitos_tel = re.findall(r"\d", telemovel)
    total_digitos = len(digitos_tel)

    email_ok = re.match(padrao_email, email)
    nif_ok = re.match(padrao_nif, nif)
    tel_ok = total_digitos == 9

    if email_ok and nif_ok and tel_ok:
        registos_validos.append(reg)

with open("validos.json", "w", encoding="utf-8") as out:
    json.dump(registos_validos, out, indent=2, ensure_ascii=False)
