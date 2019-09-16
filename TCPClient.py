import socket

server = socket.socket()
host = 'localhost'
port = 5000


server.connect((host, port))
#server.send('Hello world')

with open('recived_file', 'wb') as f:
    print ('file opened')
    while True:
        print('reciving data...')
        data = server.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        f.write(data)
f.close()
print('Successfully get the file')
server.close()
print('Connection closed')

