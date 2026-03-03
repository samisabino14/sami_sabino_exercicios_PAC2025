nota1 = int(input("Introduz a nota 1: "))
nota2 = int(input("Introduz a nota 2: "))
nota3 = int(input("Introduz a nota 3: "))

peso_nota1 = nota1 * .2
peso_nota2 = nota2 * .3
peso_nota3 = nota3 * .5

media = peso_nota1 + peso_nota2 + peso_nota3

if media >= 6:
    print(f"Aprovado: \n{media}")
else:
    print(f"Reprovado: \n{media}")
