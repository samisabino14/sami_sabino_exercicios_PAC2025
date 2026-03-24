import json

with open("validos.json", "r", encoding="utf-8") as file:
    dados = json.load(file)

with open("resumo_emails.txt", "w", encoding="utf-8") as out:
    for reg in dados:
        nome = reg.get("nome", "").strip()
        email = reg.get("email", "").strip()
        out.write(f"{nome} | {email}\n")
