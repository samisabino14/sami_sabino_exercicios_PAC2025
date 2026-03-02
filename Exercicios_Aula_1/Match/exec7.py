dicionário = input("\nIntroduz um dicionário com os dados: ")

try:
    entrada = eval(dicionário)
except:
    entrada = dicionário
    
print("\n")

match entrada:
    case dict():
        match entrada['categoria'].lower():
            case _ if entrada['categoria'].lower() == "eletrônico" and int(entrada['preco']) > 1000:
                print("Produto de luxo")
            case _ if entrada['categoria'].lower() == "eletrônico" and int(entrada['preco']) <= 1000:
                print("Produto comum")
            case _ if entrada['categoria'].lower() == "alimento":
                print("Produto alimentar")
            case _:
                print("Categoria desconhecida.")            
    case _:
        print("Entrada inválida. Espera-se um dicionário")
