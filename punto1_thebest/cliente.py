import socket
import sys
serverName = 'localhost'
serverPort = 12000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cantidad = 4
numeros = ""

for n in range(0,cantidad):
    numeros+=raw_input("Ingrese el numero "+str(n+1)+":")
    if n < cantidad-1:
        numeros+=","

client_socket.sendto(str(numeros),(serverName, serverPort))

perfectos, serverAddress = client_socket.recvfrom(2048)
print ("Hay "+perfectos+" numeros perfecto")

primos, serverAddress = client_socket.recvfrom(2048)
print ("Hay "+primos+" numeros primos")

client_socket.close()
