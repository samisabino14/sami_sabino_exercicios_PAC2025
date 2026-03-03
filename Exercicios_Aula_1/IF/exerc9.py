meses = ("1- Janeiro", "2- Fevereiro", "3- Março", "4- Abril", "5- Maio", "6- Junho", "7- Julho", "8- Agosto", "9- Setembro", "10- Outubro", "11- Novembro", "12- Dezembro")


print("\nDias de semana:\n")
for mes in meses:
    print(mes)
    
mes_escolha = int(input("\nIntroduza um mês: "))

match mes_escolha:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7:
        print("Julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:
        print("Novembro")
    case 12:
        print("Dezembro")

