import functions

def read_numbers():
    
    i = 1
    while i < 11:
        number = int(input(f"Introduza o {i}º número: "))
        
        if number > 0:
            numbers.append(number)
            i+=1
        else:
            print("Informe o número positivo.")    

numbers = []
pares = []
impares = []

read_numbers()

functions.getParImpar(pares, impares, numbers)

functions.show_message("Números pares", pares)
functions.show_message("Números ímpares", impares)
