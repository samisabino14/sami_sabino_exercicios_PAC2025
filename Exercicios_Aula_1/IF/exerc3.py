num1 = int(input("Introduz o número 1: "))
num2 = int(input("Introduz o número 2: "))

if num1 < num2:
    crescente1 = num1
    crescente2 = num2
else:    
    crescente1 = num2
    crescente2 = num1
    
print(f'Crescente {crescente1}, {crescente2}')
print(f'Decrescente: {crescente2}, {crescente1}')
    