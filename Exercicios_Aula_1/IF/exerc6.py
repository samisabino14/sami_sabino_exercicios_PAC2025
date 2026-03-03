cliente = input("Introduz o nome do cliente: ")
valor_compra = float(input("Introduz o valor da compra: "))

desconto = 0

if valor_compra <= 0:
    print("\nO valor da compra deve ser maior que zero.")
    exit()
    
if valor_compra <= 200:
    desconto = valor_compra * .10
elif 200 < valor_compra <= 500:
    desconto = valor_compra * .15
else:
    desconto = valor_compra * .20
    
print(f"Nome cliente: {cliente}")
print(f"Valor da compra: {valor_compra:.2f}€")
print(f"Desconto: {desconto:.2f}€")
print(f"Total a pagar: {(valor_compra - desconto):.2f}€")
