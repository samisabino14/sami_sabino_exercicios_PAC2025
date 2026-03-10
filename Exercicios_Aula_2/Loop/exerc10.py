from functions import read_numero

numero = read_numero()

count = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        count += 1
        
print(f"O número {numero} possui {count} divisores.")

