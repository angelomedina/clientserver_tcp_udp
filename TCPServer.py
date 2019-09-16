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
    #conn.send('Thanks you for connecting')
    conn.close()
    