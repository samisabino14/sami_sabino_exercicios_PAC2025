dicionário = input("\nIntroduz um dicionário com os dados: ")

try:
    entrada = eval(dicionário)
except:
    entrada = dicionário
    
match entrada:
    case dict():
        match entrada['tipo'].lower():
            case "compra":
                print(f"\nCompra de {entrada['valor']}€")
            case "venda":
                print(f"Venda de {entrada['valor']}€")
            case _:
                print("Entrada inválida.")            
    case _:
        print("\nEntrada inválida. Espera-se um dicionário")
