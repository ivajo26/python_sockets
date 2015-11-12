from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ("The server is ready to receive")
while 1:
    numeros, clientAddress = serverSocket.recvfrom(2048)
    perfectos = 0
    primos = 0
    numeros_enteros = numeros.split(',')
    for n in numeros_enteros:
        total = 0
        totalP = 0
        # Evaluamos si el numero es perfecto
        for y in range(1,int(n)):
            if int(n)%y==0:
                total += y
        if total == int(n):
            perfectos += 1
        # Evaluamos si el numero es primo
        for y in range(1,int(n)+1):
            if int(n)%y==0:
                totalP += 1
        if totalP == 2:
            primos+=1

    serverSocket.sendto(str(perfectos), clientAddress)
    serverSocket.sendto(str(primos), clientAddress)
