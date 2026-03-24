import re as regex

with open("registos.txt", 'r', encoding='utf-8') as file:
    texto = file.read()

padrao_nif = r"\bNIF\b:\n*([^|]+)"
padrao_validacao = r"^[123568]\d{8}$"

nifs = regex.findall(padrao_nif, texto)

for nif in nifs:
    
    if regex.match(padrao_validacao, nif.strip()):
        print(f"{nif} válido.")
    else:
        print(f"{nif} inválido.")