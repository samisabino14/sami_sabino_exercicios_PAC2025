import re as regex

with open("dados.json", 'r', encoding='utf-8') as file:
    texto = file.read()

padrao_email = r"[\w\.-]+@[\w\.-]+\.\w+"
        
emails = regex.findall(padrao_email, texto)

for email in emails:
    if regex.match(padrao_email, email.strip()):
        print(f"{email} é válido")
    else:
        print(f"{email} é inválido")