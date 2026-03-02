operacoes = ("soma", "subtrai", "multiplica", "divide")

print("\nOperações válidas:\n")
for op in operacoes:
    print(op.lower())
    
operacao = input("\nIntroduza uma operação: ")
numero1 = int(input("Introduza o primeiro número: "))
numero2 = int(input("Introduza o segundo número: "))

match operacao.lower():
    case 'soma':
        print(numero1 + numero2)
    case 'subtrai':
        print(numero1 - numero2)
    case 'multiplica':
        print(numero1 * numero2)
    case 'divide':
        print(numero1 // numero2) # Por ser divisão de inteiros
