dicionário = input("\nIntroduz um dicionário com os dados: ")

try:
    entrada = eval(dicionário)
except:
    entrada = dicionário
    
print("")

match entrada:
    case dict():
        match entrada['metodo'].upper():
            case _ if entrada['metodo'].upper() == "GET":
                print("Requisição GET recebida")
            case _ if entrada['metodo'].upper() == "POST" and len(entrada['conteudo']) > 0:
                print("Requisição POST com dados válidos")
            case _ if entrada['metodo'].upper() == "POST" and len(entrada['conteudo']) == 0:
                print("Requisição POST sem dados")
            case _:
                print("Método não suportado.")            
    case _:
        print("Entrada inválida. Espera-se um dicionário")
