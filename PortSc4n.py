import socket

def scan():
    Banner()
    #ip = "0"
    portaI = int(input("Digite a porta Inicial:"))
    portaF = int(input("Digite a porta Final:"))
    ip = input("Digite o Ip Alvo:")
    
    for porta in range(portaI,portaF):
        #print("Scaneando IP: {} na porta {}" .format(ip,porta))
        conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        resp = conexao.connect_ex((ip,porta))
        conexao.close()
        

        if (resp == 0):
            print("Porta {} Aberta" .format(porta))
            #bgrapper = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conexao.connect((ip,porta))
            bannergrapper = conexao.recv(1024)
            conexao.close()
            print(bannergrapper)
        else:
	        print("Porta {} Fechada" .format(porta))
            

def Banner():
    print("Port Scan v 0.1 - Bl4dsc4n")


if(__name__ == "__main__"):
    scan()
    
