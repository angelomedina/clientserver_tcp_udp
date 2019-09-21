import socket
import os

port = 5004
host = '127.0.0.1'

print('server -d listening udp: '+ host +' '+str(port))

# socket.AF_INET: means protocol IPv4
# socket.SOCK_DGRAM: used for UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((host,port))

    while True:

        data, address = s.recvfrom(1024)
        print('connected by ',address)

        #convert the response to string; then concat the path and the filename(name)
        filename = str(repr(data))
        name = filename[2:len(filename)-1]
        filepath = 'server-file/'+name
        f = open(filepath, 'rb')
        value = f.read(1024)

        while (value):
            s.sendto(value, address)
            print('sent file')
            value = f.read(1024)
        f.close()
        print('sent file finished')




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