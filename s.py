import socket
import os

port = 5003
host = '127.0.0.1'

print('server -l listening: '+ host +' '+str(port))

# socket.AF_INET: means protocol IPv4
# socket.SOCK_DGRAM: used for UDP

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((host,port))

    while True:

        # received data and addres of any connection
        data, address = s.recvfrom(1024)
            
        print('connected by ',address)
            
        # connection to send the file list in server-file directory
        print('enviando lista del archivos del directorio server-file:')

        for value in os.listdir('server-file'):
            filename = str.encode(value)
            print(filename)
            s.sendto(filename, address)
   

    




"""
port = 5000
host = '127.0.0.1'

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host,port))
print('server -l listening: '+ host +' '+str(port))

while True:

    data, address = server.recvfrom(1024)

    print(data)

    if data:
        server.sendto(b'ha llegado un sms tuyo', address)

"""