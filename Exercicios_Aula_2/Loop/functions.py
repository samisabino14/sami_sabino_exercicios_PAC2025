def getParImpar(par, impar, loop):
    for i in loop:
        if i % 2 == 0:
            par.append(i)
        else:
            impar.append(i)
            
def show_message(msg, list):
    print(f"{msg}: ",list)

def imprimir_numeros(inicio, fim, intervalo):
    for i in range(inicio, fim, intervalo):
        print(i)
        
def read_numero():
    while True:
        try:
            numero = int(input(f"Introduza um número inteiro: "))
            return numero

        except ValueError:
            print("\nInforme um número inteiro.")