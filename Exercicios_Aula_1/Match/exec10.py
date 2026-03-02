jogadas = ("pedra", "papel", "tesoura")

print("\nJogadas válidas:\n")
for jg in jogadas:
    print(jg.lower())
    
jogador1 = input("\nIntroduza a jogada (jogador 1): ")
jogador2 = input("Introduza a jogada (jogador 2): ")

print()

match (jogador1, jogador2):
    case ('pedra', 'tesoura') | ('tesoura', 'papel') | ('papel', 'pedra') :
        print("Jogador 1 venceu")
    case ('tesoura', 'pedra') | ('papel', 'tesoura') | ('pedra', 'papel') :
        print("Jogador 2 venceu")
    case (jogador1, jogador2) if jogador2 == jogador1:
        print("Há um Empate")
