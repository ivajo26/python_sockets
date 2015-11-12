import socket
import sys
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ('192.168.43.182', 10001)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
sock.sendall("apuesta")
try:
    print("Opciones\n1.- Lunes\n2.- Martes\n3.- Miercoles\n4.- Jueves\n5.- Viernes")

    dia = {'1':'Lunes','2':'Martes','3':'Miercoles','4':'Jueves','5':'Viernes'}
    while True:
        select_dia = raw_input('Escoja una opcion: ')
        if dia[select_dia]:
            print >>sys.stderr, 'Consultando loterias disponibles el dia: "%s"' % dia[select_dia]
            sock.sendall(dia[select_dia])
            break
        else:
            print >>sys.stderr, 'No escogio una opcion correcta'

    amount_received = 0
    amount_expected = len(dia[select_dia])
    while amount_received < amount_expected:
        loterias = sock.recv(1100)
        amount_received += len(loterias)
        loterias = loterias.split(',')
        disponibles = {}
        print >>sys.stderr, 'Las loteria disponibles son: '
        for n in range(1,len(loterias)):
            print >>sys.stderr, '%s.%s' % (n,loterias[n])
            disponibles[str(n)]=loterias[n]
        select_lot = raw_input('Escoja una opcion: ')
        while True:
            if 1<=int(select_lot) and int(select_lot)<=len(loterias):
                loteria = disponibles[select_lot]
                print >>sys.stderr, 'La loteria seleccionada fue: "%s"' % loteria
                break
            else:
                print >>sys.stderr, 'No escogio una opcion correcta'
                select_lot = raw_input('Escoja una opcion: ')

        while True:
            numero = raw_input('Ingrese su numero a jugar: ')
            if 100 <=int(numero) and int(numero) <= 9999:
                break
            else:
                print >>sys.stderr, 'Error: Ingrese un numero de 3 o 4 digitos'
        print >>sys.stderr, 'Su numero a jugar es: "%s"' % numero

        while True:
            apuesta = raw_input('Ingrese su apuesta a jugar: ')
            sock.sendall(apuesta)
            tope = sock.recv(1100)
            if int(tope)==0:
                break
            else:
                print >>sys.stderr, 'Error: Excedio el tope'
        print >>sys.stderr, 'Su apuesta a jugar es: "%s"' % apuesta
        jugar = "%s,%s,%s," % (numero,loteria,apuesta)
        sock.sendall(jugar)
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
