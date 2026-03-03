saldo = int(input("Qual é o saldo da conta?: "))
cheque = int(input("Qual é o valor do cheque?: "))

if saldo > cheque:
    print(f"Cheque descontado, saldo {saldo - cheque}")
else:
    print("O cheque não puder ser descontado. O saldo do cliente é inferior ao valor do cheque.")