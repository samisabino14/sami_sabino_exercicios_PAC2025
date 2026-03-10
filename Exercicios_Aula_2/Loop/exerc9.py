def read_numero():
    while True:
        numero = int(input(f"Introduza o número no intervalo (1-100): "))
        
        if 0 < numero <= 100:
            print("\nO número satisfaz o intervalo (1-100)")
            return False
        else:
            print("\nInforme um número maior que zero e menor ou igual a 100.")

read_numero()