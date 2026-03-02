dias_semana = ("domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sábado")

print("\nDias de semana:\n")
for dia_semana in dias_semana:
    print(dia_semana.lower())
    
dia_escolha = input("\nQue dia de semana é hoje? ")

match dia_escolha.lower():
    case "domingo" | 'sábado':
        print("Fim de semana.")
    case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
        print("Dia útil.")      
    case _:
        print("Dia inexistente.")
    