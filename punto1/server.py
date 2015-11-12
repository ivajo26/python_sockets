from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ("The server is ready to receive")
while 1:
    lados, clientAddress = serverSocket.recvfrom(2048)
    tipo = ""
    lados = lados.split(',')
    if int(lados[0])==int(lados[1]) and int(lados[0])== int(lados[2]) and int(lados[1])==int(lados[2]):
        tipo = "Equilatero"
    elif int(lados[0])==int(lados[1]) or int(lados[0])== int(lados[2]) or int(lados[1])==int(lados[2]):
        tipo = "Isosceles"
    elif int(lados[0])!=int(lados[1]) and int(lados[0])!= int(lados[2]) and int(lados[1])!=int(lados[2]):
        tipo = "Escaleno"
    else:
        tipo = "Desconocido"
    serverSocket.sendto(str(tipo), clientAddress)
