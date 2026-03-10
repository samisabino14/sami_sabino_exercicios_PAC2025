def read_notas():
    
    i = 1
    while i < 11:
        nota = int(input(f"Introduza o {i}º número: "))
        
        if 0 <= nota <= 20:
            notas_alunos.append(nota)
            i+=1
        else:
            print("\nInforme um número igual ou maior que zero e menor ou igual a 20.")

notas_alunos = []

read_notas()

media = sum(notas_alunos) / len(notas_alunos)

print("Média de notas de alunos: ",media)