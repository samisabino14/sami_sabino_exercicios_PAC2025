lista = ["banana", "uva", "abacaxi", "laranja"]

print(lista)

for i in range(len(lista) - 1):
    print()
    print(f"Linha {i}: {lista[i]}")
    for j in range(len(lista[i])):    
        #print(lista[j])
        print(f"[Linha {i}][Coluna {j}]: {lista[i][j]}")
        #print(f"[Linha {i + 1}][Coluna {j + 1}]: {lista[i][j]}")
   
        
        #print(f"Lista posição {i}-{j + 1}: {lista[i][j + 1]}")
        #print(j)
    