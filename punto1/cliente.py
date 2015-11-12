import socket
import sys
serverName = 'localhost'
serverPort = 12000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cantidad = 3
lados = ""

for n in range(0,cantidad):
    lados+=raw_input("Ingrese el numero "+str(n+1)+":")
    if n < cantidad-1:
        lados+=","

client_socket.sendto(str(lados),(serverName, serverPort))

tipo, serverAddress = client_socket.recvfrom(2048)
print ("EL triangulo es: "+tipo)

client_socket.close()
