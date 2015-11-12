import socket
import sys
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 10001)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
sock.sendall("consulta")
opciones = {'1':'masjugado','2':'total','3':'porloteria','4':'menosjugado','5':'salir'}
while True:
    print("Opciones\n1.- Numero Mas jugado\n2.- Total Recaudado\n3.- Total Recaudado por loteria\n4.- Numero Menos Jugado\n5. - Salir")

    opcion = raw_input('Escoja una consulta: ')
    if opciones[opcion]:
        if opcion=='5':
            sock.close()
            break
        else:
            sock.sendall(opciones[opcion])
            amount_received = 0
            amount_expected = len(opciones[opcion])
            while amount_received < amount_expected:
                data = sock.recv(1100)
                amount_received += len(data)
                print >>sys.stderr, '%s' % data
    else:
        print >>sys.stderr, 'No escogio una opcion correcta'
        opcion = raw_input('Escoja una consulta: ')
