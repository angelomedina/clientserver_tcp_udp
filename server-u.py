# tutorial
# https://realpython.com/python-sockets/
import socket
import json
host = '127.0.0.1'
port = 5000

print('server listening: '+host+' '+str(port))
# socket.AF_INET: means protocol IPv4
# socket.SOCK_STREAM: used for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen()
    conn, addr = s.accept()

    #connetion to wite a file
    filetodown = open('server/server.png','wb')

    print('connected by ',addr)
    while True:
        print('receiving...')
        data = conn.recv(1024)
        filetodown.write(data)

        if len(data) < 1024:
            print('done reciving')
            break
    filetodown.close()
    conn.sendall(bytes(json.dumps('file saved in server-fle')),'UTF-8') 
    conn.shutdown(2)
    conn.close()