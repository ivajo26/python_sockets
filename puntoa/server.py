import socket
import sys
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('127.0.0.1', 10001)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
# Listen for incoming connections
tope = 1000
def buscar_loterias(dia):
    db=open('loterias.txt','r')
    linea=db.readline()
    while linea!="":
        linea=linea.split(',')
        if linea[0]==dia:
            loterias = linea
            break
        linea=db.readline()
    db.close()
    return loterias

def enviar_data(data):
    datos = ""
    count = 0
    for n in data:
        if count < len(data)-1:
            datos += n
        if count < len(data)-2:
            datos += ","
        count += 1
    return datos

def guardar(jugar):
    archi=open('apuestas.txt','a')
    archi.write(jugar)
    archi.write('\n')
    archi.close()

def masjugado():
    db=open('apuestas.txt','r')
    numeros = {}
    linea=db.readline()
    while linea!="":
        linea=linea.split(',')
        if not numeros.has_key(linea[0]):
            numeros[linea[0]]=1
        else:
            numeros[linea[0]]+=1
        linea=db.readline()
    mayor = 0
    for n in numeros.values():
        if n >=mayor:
            mayor = n
    for clave, valor in numeros.iteritems():
        if valor==mayor:
            db.close()
            return "El numero que mas jugo fue "+clave

def total():
    db=open('apuestas.txt','r')
    total = 0
    linea=db.readline()
    while linea!="":
        linea=linea.split(',')
        total += int(linea[2])
        linea=db.readline()
    db.close()
    return "Se Recaudo un total de "+str(total)

def porloteria():
    db=open('apuestas.txt','r')
    loterias = {}
    linea=db.readline()
    while linea!="":
        linea=linea.split(',')
        if not loterias.has_key(linea[1]):
            loterias[linea[1]]=int(linea[2])
        else:
            loterias[linea[1]]+=int(linea[2])
        linea=db.readline()
    data = ""
    for clave, valor in loterias.iteritems():
        data += clave+" = "+str(valor)+"\n"
    db.close()
    return data

def menosjugado():
    db=open('apuestas.txt','r')
    numeros = {}
    linea=db.readline()
    while linea!="":
        linea=linea.split(',')
        if not numeros.has_key(linea[0]):
            numeros[linea[0]]=1
        else:
            numeros[linea[0]]+=1
        linea=db.readline()
    menor = 0
    for n in numeros.values():
        if menor==0:
            menor=n
        if n <=menor:
            menor = n
    for clave, valor in numeros.iteritems():
        if valor==menor:
            db.close()
            return "El numero que menos jugo fue "+clave
def salir():
    return "True"
sock.listen(1)
while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address
        # Receive the data in small chunks and retransmit it
        cliente = connection.recv(1100)
        if cliente=="consulta":
            while True:
                funcion = connection.recv(1100)
                print (funcion)
                if globals()[funcion]()=="True":
                    break
                resultado = globals()[funcion]()
                print (resultado)
                connection.sendall(resultado)
        else:
            while True:
                dia = connection.recv(1100)
                loterias = buscar_loterias(dia)
                connection.sendall(enviar_data(loterias))

                print >>sys.stderr, 'Esperando apuesta'
                while True:
                    apuesta = connection.recv(1100)
                    if int(apuesta)<=tope:
                        connection.sendall("0")
                        break
                    else:
                        connection.sendall("1")
                while True:
                    jugar = connection.recv(1100)
                    print (apuesta)
                    if jugar:
                        guardar(jugar)
                        break
                break
    finally:
        # Clean up the connection
        connection.close()
