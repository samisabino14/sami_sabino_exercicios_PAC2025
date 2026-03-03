num1 = int(input("Introduz o número 1: "))
num2 = int(input("Introduz o número 2: "))
num3 = int(input("Introduz o número 3: "))

if num1 < num2 < num3:
    crescente1 = num1
    crescente2 = num2
    crescente3 = num3
elif num2 < num1 < num3:
    crescente1 = num2
    crescente2 = num1
    crescente3 = num3
else:    
    crescente1 = num3
    crescente2 = num1
    crescente3 = num2

print(f'Crescente {crescente1}, {crescente2}, {crescente3}')
print(f'Decrescente: {crescente3}, {crescente2}, {crescente1}')
    