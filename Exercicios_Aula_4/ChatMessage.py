import re as rg

def detectar_informacoes(msg):
    
    padroes = {
        "email": r"[\w\.-]+@[\w\.-]+\.\w+",
        "telefone": r"\b\d{9}\b",
        "nome_proprio": r"\b[A-ZÁÉÍÓÚÂÊÔÃÕ][a-záéíóúâêôãõç]+\b",
        "data": r"\b\d{1,2}/\d{1,2}/\d{4}\b",
        "iban": r"PT\d{2}[ \d]{21,}",
        "nif": r"\b\d{9}\b",
        "senha": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_\\-])[A-Za-z\d@$!%*?&_\\-]{8,}$"
    }
    
    encontrados = {}
    
    for tipo, padrao in padroes.items():
        achados = rg.findall(padrao, msg)
        if achados:
            encontrados[tipo] = achados
        
    return encontrados


def enviarMensagem(clientSocket, isChat):
            
    try:
        msg = input("Nova mensagem: ")    
        clientSocket.send(msg.encode())
            
        if "fechar" in msg.lower():
            isChat = False
        
        return isChat
    
    except Exception as e:
        print(f"Erro: ",e)
        

def receberMensagem(clientSocket):
    #print(f"{role.title()}:")
    try:
        resposta = clientSocket.recv(1024).decode()
            
        print("Mensagem recebida:", resposta)
        
        if "fechar" in resposta.lower():
            isChat = False
            return isChat
        
        return resposta
    
    except Exception as e:
        print(f"Erro: ",e)
        
