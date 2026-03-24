# ==========================================
# SERVIDOR TCP EM PYTHON
# SOCKET SERVER
# ==========================================

import socket     # biblioteca para comunicação em rede
import time       # biblioteca para controlo de tempo
import re as regex
from ChatMessage import chatMessage

# -------------------------------
# 1. CRIAR SOCKET DO SERVIDOR
# -------------------------------
# AF_INET  -> usa IPv4
# SOCK_STREAM -> usa protocolo TCP

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# -------------------------------
# 2. DEFINIR IP E PORTA
# -------------------------------

host = "127.0.0.1"   # localhost
porta = 12340        # porta do servidor


# -------------------------------
# 3. BIND (VÍNCULO)
# -------------------------------
# Associa a socket ao IP e à porta

serverSocket.bind((host, porta))


# -------------------------------
# 4. LISTEN (ESPERAR CONEXÕES)
# -------------------------------
# listen(1) -> permite 1 cliente em espera

serverSocket.listen(1)

print(f"Servidor ligado em {host}:{porta}")
print("A aguardar conexão de cliente...")


# -------------------------------
# 5. ACEITAR CONEXÃO DO CLIENTE
# -------------------------------
# accept() devolve:
# clientsocket -> socket do cliente
# enderecoCliente -> IP e porta do cliente

clientSocket, enderecoCliente = serverSocket.accept()

print(f"Conexão estabelecida com {enderecoCliente}")

isChat = True

while isChat:
    
        # -------------------------------
    # 6. RECEBER MENSAGEM DO CLIENTE
    # -------------------------------
    # recv(1024) -> recebe até 1024 bytes
    # decode() -> converte bytes para string
    mensagem = clientSocket.recv(1024).decode()
    print("Mensagem do cliente:", mensagem)
    
    """ 
    padrao_nome=r"nome"
    padrao_email=r"^[\w\.]+@[\w\.]+\.\w+$"
    pegar_email = regex.search('samisabino@gmail.com', mensagem)
    pegar_nome = regex.findall(padrao_nome, mensagem)
    #resultado = pegar_email.span()
    
    print(f"Possível email: {pegar_email}")
    print(f"Possível nome: {pegar_nome}")
    print()
    
    """
    
    if "fechar" in mensagem.lower():
        isChat = False
        break
    
    
    # -------------------------------
    # 7. ENVIAR RESPOSTA AO CLIENTE
    # -------------------------------
    # encode() -> converte string para bytes
    resposta = input("\nNova mensagem: ")
    isChat = chatMessage(resposta, 'Cliente', time, clientSocket, isChat)
    
    if not isChat:
        break

time.sleep(2)

# -------------------------------
# 9. FECHAR CONEXÕES
# -------------------------------
clientSocket.close()
serverSocket.close()

print("\n\nConexões fechadas.")