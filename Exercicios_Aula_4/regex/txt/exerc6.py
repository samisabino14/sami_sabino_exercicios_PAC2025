import re as regex

with open("dados.txt", 'r', encoding='utf-8') as file:
    texto = file.read()

padrao_email = r"\b[\w\.-]+@[\w\.-]+\.pt\b"

emails = regex.findall(padrao_email, texto)

for email in emails:
    print(email)