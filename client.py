import socket

host = '127.0.0.1'
port = 5000

# socket.AF_INET: means protocol IPv4
# socket.SOCK_STREAM: used for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((host, port))
    s.sendall(b'Hello, word')
    data = s.recv(1024)

print('client recived', repr(data))

"""
import socket
server = socket.socket()
host = 'localhost'
port = 5000


server.connect((host, port))
server.send('Hello world')


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

"""
