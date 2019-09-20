import socket 

server = socket.socket()
server.connect(("localhost", 5000))

filetosend = open("client-file/client.png", "rb")
data = filetosend.read(1024)
while data:
    print("Sending...")
    server.send(data)
    data = filetosend.read(1024)
filetosend.close()
server.send(b"DONE")
print("Done Sending.")
print(server.recv(1024))
server.shutdown(2)
server.close()

"""
import socket
import json

host = '127.0.0.1'
port = 5000

message = {'type':'-h'}

# socket.AF_INET: means protocol IPv4
# socket.SOCK_STREAM: used for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((host, port))
    s.send(bytes(json.dumps(message), 'UTF-8'))
    data = json.loads(s.recv(1024))

print(data)
s.close()

#print('client recived', repr(data))
"""
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
