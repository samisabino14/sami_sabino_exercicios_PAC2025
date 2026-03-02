dicionário = input("\nIntroduz um dicionário com os dados: ")

try:
    entrada = eval(dicionário)
except:
    entrada = dicionário
    
print("\n")
    
match entrada:
    case dict():
        match entrada['status'].lower():
            case _ if entrada['status'].lower() == "ok" and int(entrada['tempo_resposta']) <= 200:
                print("Servidor ativo")
            case _ if entrada['status'].lower() == "ok" and int(entrada['tempo_resposta']) > 200:
                print("Servidor lento")
            case _ if entrada['status'].lower() == 'erro':
                print("Servidor indisponível")
            case _:
                print("Estado desconhecido.")            
    case _:
        print("Entrada inválida. Espera-se um dicionário")
