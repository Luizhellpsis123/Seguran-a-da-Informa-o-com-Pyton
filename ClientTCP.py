from re import S
import socket
import sys

from zmq import Socket

def main():
    try:
        S = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
      
    except Socket.error as e:
      print("A conexão falhou!!!")
    print("Erro: {} " .format(e))
    sys.exit()

    print("Socket criado com sucesso")

HostAlvo = input("Digite o Host ou IP a sser conectado")
PortaAlvo = input("Digite a Porta a ser conectada")

try:
    S.connect((HostAlvo, int(PortaAlvo)))
    print("Cliente TCP conectado com sucesso no Host: ")
    S.shutdown(2)
except socket.error as e:
    print("Não foi possível conectar no Host: ")
    print("Erro: {} " .format(e))
    sys.exit
if __name__ == "__main__":
    main()
