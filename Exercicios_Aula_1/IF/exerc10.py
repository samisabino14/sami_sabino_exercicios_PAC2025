numeros = []

pares = 0
impares = 0

for i in range(10):
    numero = int(input(f"Introduz o {i + 1}º número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
        
print("Pares:", pares)
print("Ímpares:", impares)