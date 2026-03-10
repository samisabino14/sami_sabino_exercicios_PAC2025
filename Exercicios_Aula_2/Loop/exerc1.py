import Exercicios_Aula_2.Loop.functions as functions
    

numeros_pares = []
numeros_impares = []

functions.getParImpar(numeros_pares, numeros_impares, range(1, 31))

functions.show_message("Números pares", numeros_pares)
functions.show_message("Números ímpares", numeros_impares)