def eh_primo(numero):
    if numero < 2:
        return False
    
    for i in range(2, numero):        
        if numero % i == 0:
            return False
            
    return True

numero = 2
count = 2

while count < 10:
    if eh_primo(numero):
        print(numero)
        count += 1

    numero += 1