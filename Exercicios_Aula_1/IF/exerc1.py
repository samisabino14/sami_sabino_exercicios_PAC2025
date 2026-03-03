entrada = int(input("Introduz os segundos: "))

if entrada >= 0:
    horas = entrada // 3600
    minutos = entrada % 3600 // 60
    segundos = entrada % 3600 % 60

    print(f"{horas} hora, {minutos} minuto e {segundos} segundos.")