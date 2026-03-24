filename = R'dados.txt'

with open(filename, 'r', encoding='utf-8') as fl:
    texto = fl.read()
    
    print(texto)