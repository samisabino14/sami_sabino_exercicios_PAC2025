dado = input("\nIntroduz um tipo de dado: ")

try:
    valor = eval(dado)
except:
    valor = dado
    
match valor:
    case int():
        print('Número inteiro')
    case float():
        print('Número decimal')
    case str():
        try:
            float(dado)
            print('String numérica')
        except ValueError:
            print('String textual')
    case list():
        print('Lista')
    case _:
        print('Tipo desconhecido')