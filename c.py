import socket
import os

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#convert the _file a b'text' that why I need to send a format without b''
filename = str.encode('server.png', 'utf-8')
client.sendto(filename, ('127.0.0.1', 5004))

#save the file in this directory
with open(os.path.join('client-file/','server.png'),'wb') as f:

    while True:

        data, server = client.recvfrom(1024)

        if not data:
            break
        f.write(data)
        print('file saved in: client-file/your-file-name')

f.write()
socket.close()


"""
port = 5000
host = '127.0.0.1'

clinet = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('enviando datos')

#send data
address = (host, port)
clinet.sendto(b'test', address)

#receive data
data, server = clinet.recvfrom(1024)
print(data)

#print(server.recvfrom(1024))
"""