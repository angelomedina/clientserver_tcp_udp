import socket
import os
import json

HOST = '127.0.0.1'    
PORT = 5000

filename = 'server.png'
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send(b'server.png')

with open(os.path.join('client-file/', filename), 'wb') as f:
    print('file opened')

    while True:
        print('reciving data')
        data = socket.recv(1024)

        if not data:
            break
        f.write(data)

f.close()
print('file save in: client-file/your-file-name')
socket.close()
