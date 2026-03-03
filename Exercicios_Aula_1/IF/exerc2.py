num1 = int(input("Introduz o número 1: "))
num2 = int(input("Introduz o número 2: "))
num3 = int(input("Introduz o número 3: "))

maior = num1
menor = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
    
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print("Maior: ",maior)
print("Menor: ",menor)
