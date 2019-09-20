# tutorial
# https://realpython.com/python-sockets/
import socket
import json
host = '127.0.0.1'
port = 5000
print('Server listening: '+ host +' '+ str(port))
# socket.AF_INET: means protocol IPv4
# socket.SOCK_STREAM: used for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    #connection to download a file
    print('connected by', addr)
    data = conn.recv(1024)
    #convert the response in string; then concat the path and the filename(name)
    filename = str(repr(data))
    name = filename[2:len(filename)-1]
    filepath = 'server-file/' + name
    f = open(filepath, 'rb')
    value = f.read(1024)
    while (value):
        #conn.send(value)
        print('sent file')
        value = f.read(1024)
    f.close()
print('Done sending')
conn.close() 