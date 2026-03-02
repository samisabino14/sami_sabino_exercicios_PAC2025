mensagem = input("\nIntroduza uma mensagem: ")

print(mensagem.lower().strip())

match mensagem.lower().strip():
    case 'olá' | 'bom dia':
        print("Saudação")
    case _ if mensagem.endswith("?"):
        print("Pergunta")
    case _ if "tchau" in mensagem.lower() or "adeus" in mensagem.lower():
        print("Despedida")
    case _:
        print("Mensagem genérica")
        