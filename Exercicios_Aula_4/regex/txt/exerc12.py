import re

with open("registos.txt", "r", encoding="utf-8") as file:
    texto = file.read()
    print(texto)
# Captura cada bloco completo de registo
padrao = (
    r"Nome:\s*([^\n|]+).*?"
    r"NIF:\s*([0-9]{9}).*?"
    r"Data:\s*([0-9]{2}/[0-9]{2}/[0-9]{4}).*?"
    r"Código Postal:\s*([0-9]{4}-[0-9]{3}).*?"
    r"Website:\s*([^\s|]+)"
)

registos = re.findall(padrao, texto)

with open("resumo.txt", "w", encoding="utf-8") as out:
    for nome, nif, data, cp, site in registos:
        out.write(f"{nome.strip()} | {nif.strip()} | {data.strip()} | {cp.strip()} | {site.strip()}\n")
