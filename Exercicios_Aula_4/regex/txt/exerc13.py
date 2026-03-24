import re
from datetime import datetime

with open("registos.txt", "r", encoding="utf-8") as file:
    texto = file.read()

# 1. Extrair todas as datas no formato DD/MM/AAAA
padrao_data = r"\b(\d{2}/\d{2}/\d{4})\b"
datas = re.findall(padrao_data, texto)

# 2. Converter para datetime e filtrar datas < 2025
datas_anteriores = []

for d in datas:
    data_obj = datetime.strptime(d, "%d/%m/%Y")
    if data_obj.year < 2025:
        datas_anteriores.append(d)

# 3. Mostrar resultados
print("Datas anteriores a 2025:")
for d in datas_anteriores:
    print(d)
