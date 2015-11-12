import socket
import sys
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ('localhost', 10002)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
try:
    # Send data
    cedula = raw_input('Ingrese su numero de cedula: ')
    print >>sys.stderr, 'Consultando su cedula: "%s"' % cedula
    sock.sendall(cedula)
    # Look for the response
    amount_received = 0
    amount_expected = len(cedula)
    while amount_received < amount_expected:
        data = sock.recv(1100)
        amount_received += len(data)
        data = data.split(',')
        if data[0]=="0":
            print >>sys.stderr, 'Cedula no encontrada'
            break
        else:
            print >>sys.stderr, 'Cedula: "%s"' % data[0]
            print >>sys.stderr, 'Nombre: "%s"' % data[1]
            print >>sys.stderr, 'Mesa de Votacion: "%s"' % data[2]
            if data[3]=="1":
                print >>sys.stderr, 'Si es jurado de Votacion'
                print >>sys.stderr, 'Mesa de Jurado: "%s"' % data[4]
            else:
                print >>sys.stderr, 'No es jurado de Votacion'

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
