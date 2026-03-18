# ==========================================
# CLIENTE TCP EM PYTHON
# Ligação a um servidor usando SOCKET
# ==========================================

import socket     # biblioteca para comunicação em rede
import time       # biblioteca para controlo de tempo (opcional)
from SendMessage import sendMessage


# -------------------------------
# 1. CRIAR A SOCKET
# -------------------------------
# AF_INET  -> usa IPv4
# SOCK_STREAM -> usa protocolo TCP

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# -------------------------------
# 2. DEFINIR DADOS DO SERVIDOR
# -------------------------------

host = "127.0.0.1"   # endereço do servidor (localhost)
porta = 12340        # porta do servidor


# -------------------------------
# 3. CONECTAR AO SERVIDOR
# -------------------------------

clientSocket.connect((host, porta))
print("Ligado ao servidor!")


isChat = True

while isChat:

    # -------------------------------
    # 4. ENVIAR MENSAGEM AO SERVIDOR
    # -------------------------------
    # encode() converte string para bytes
    mensagem = input("Nova mensagem: ")
    clientSocket.send(mensagem.encode())
    #sendMessage(mensagem, 'Cliente', time, clientSocket)

    if "Fechar" in mensagem:
        isChat = False
        break
    
    # -------------------------------
    # 5. RECEBER RESPOSTA DO SERVIDOR
    # -------------------------------
    # recv(1024) -> recebe até 1024 bytes
    # decode() -> converte bytes para string
    resposta = clientSocket.recv(1024).decode()
    print("\nResposta do servidor:", resposta)
    
    if "Fechar" in resposta:
        isChat = False
        break

# -------------------------------
# 6. ESPERA (opcional)
# -------------------------------
time.sleep(2)

# -------------------------------
# 7. FECHAR A CONEXÃO
# -------------------------------

clientSocket.close()
print("\n\nConexão fechada.")