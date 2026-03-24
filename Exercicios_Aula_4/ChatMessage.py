def chatMessage(msg, status, time, clientSocket, isChat):
    
    #print(f"\nResposta do {emissor}: {msg}. \n")
    clientSocket.send(msg.encode())


    if "fechar" in msg.lower():
        isChat = False
    
    # -------------------------------
    # 8. ESPERA (SIMULA PROCESSAMENTO)
    # -------------------------------
    time.sleep(2)
    
    return isChat
    