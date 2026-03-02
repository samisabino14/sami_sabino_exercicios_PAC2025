nota = int(input("\nInforma a tua nota?: "))

match nota:
    case _ if 90 <= nota <= 100:
        print("Excelente")
    case _ if 70 <= nota <= 89:
        print("Bom")
    case _ if 50 <= nota <= 69:
        print("Suficiente")
    case _ if 50 > nota >= 0:
        print("Abaixo de 50")
    case _:
        print("Escolha inválida.")
        