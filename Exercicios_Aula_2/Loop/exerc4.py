from functions import read_numero

def calcular_primo():
    if numero < 2:
        return f"{numero} não é um número primo."
    
    for i in range(2, numero):        
        if numero % i == 0:
            return f"{numero} não é um número primo."
            
    return f"{numero} é um número primo."

numero = read_numero()
resultado = calcular_primo()

print(resultado)