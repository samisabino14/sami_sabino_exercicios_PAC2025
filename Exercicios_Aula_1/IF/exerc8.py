notas_alunos = []

for i in range(10):
    while True:
        nota = int(input(f"Introduz a nota aluno {i + 1}: "))
        if 0 <= nota <= 20:
            notas_alunos.append(nota)
            break
        else:
            print(f"A nota {nota} não é permitida. \nSó são permitidos notas de 0 a 20.")

media = sum(notas_alunos) / len(notas_alunos)
print("Média: ",media)

contador = 0

for nota in notas_alunos:
    if nota >= media:
        contador += 1
        
print("Alunos acima d média: ",contador)
