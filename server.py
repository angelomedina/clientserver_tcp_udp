
# tutorial
# https://realpython.com/python-sockets/

import socket
import json

host = '127.0.0.1'
port = 5000

print('Server listening: '+ host +' '+ str(port))

# socket.AF_INET: means protocol IPv4
# socket.SOCK_STREAM: used for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()

    #connection to write a file
    filetodown = open("server-file/server.png", "wb")

    #with conn:
    print('connected by', addr)

    while True:

        print("Receiving....")
        data = conn.recv(1024)

        filetodown.write(data)
        
        if len(data) < 1024:
            print("Done Receiving.")
            break

    filetodown.close()
    conn.sendall(bytes(json.dumps("thanks"), 'UTF-8'))
    conn.shutdown(2)
    conn.close()


"""
server = socket.socket()
server.bind((host,port))
server.listen(1)

conn,addr = server.accept()
print('Server listening: '+ host +' '+ str(port))

filetodown = open("img.png", "wb")
while True:
   print("Receiving....")
   data = conn.recv(1024)
   if data == b"DONE":
           print("Done Receiving.")
           break
   filetodown.write(data)
filetodown.close()
conn.send("Thank you for connecting.")
conn.shutdown(2)
conn.close()
"""

"""
host = '127.0.0.1'
port = 5000
print('Server listening: '+ host +' '+ str(port))

# socket.AF_INET: means protocol IPv4
# socket.SOCK_STREAM: used for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('connected by', addr)
        while True:
                    
            
            data = conn.recv(1024)
            
            test = data.decode("utf-8")
            
            print(json.loads(test))
            
            if not data:
                break
            
            #conn.sendall(bytes(json.dumps({'return':'ok'}), 'UTF-8'))
            #conn.sendall(bytes(json.dumps({'return':'ok'}), 'UTF-8'))
            #conn.sendall(bytes(json.dumps({'return':'ok'}), 'UTF-8'))

            conn.sendall(bytes(json.dumps({'return':'ok'}), 'UTF-8'))

"""

"""
import socket 

port = 5000
server = socket.socket()
hots = ''
server.bind((hots,port))
server.listen(5)

print('Server listening: '+ hots +' '+ str(port))

while True:
    conn, addr = server.accept()
    print('Got connection from', addr)
    data = conn.recv(1024)
    print('Server recived', repr(data))
    
    filename = 'TCPSERVER.py'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
        conn.send(l)
        print('Sent', repr(l))
        l = f.read(1024)
    f.close()
 
    print('Done sending')
    conn.send('Thanks you for connecting')
    conn.close()
"""