import socket
import json
import os

host = '127.0.0.1'
port = 5000

print('server listening: '+host+' '+str(port))
# socket.AF_INET: means protocol IPv4
# socket.SOCK_STREAM: used for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen()
    conn, addr = s.accept()
    #connection to download a file
    print('connected by ',addr)

    print('enviando lista del archivos del directorio server-file:')
    for value in os.listdir('server-file'):
        data = str.encode(value)
        print(data)
        conn.send(data) 
conn.close()
