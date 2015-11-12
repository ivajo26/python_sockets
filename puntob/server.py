import socket
import sys
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 10002)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
# Listen for incoming connections

def buscar(search):
    db=open('datos.txt','r')
    user = ["0","0"]
    linea=db.readline()
    while linea!="":
        linea=linea.split(',')
        if linea[0]==search:
            user = linea
            break
        linea=db.readline()
    db.close()
    return user
sock.listen(1)
while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address
        # Receive the data in small chunks and retransmit it
        while True:
            cedula = connection.recv(1100)
            print (cedula)
            data = ""
            if cedula:
                print >>sys.stderr, 'Enviando datos de usuario'
                datos = buscar(cedula)
                for n in datos:
                    data += n
                    data += ","
                print (data)
                connection.sendall(data)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
    finally:
        # Clean up the connection
        connection.close()
