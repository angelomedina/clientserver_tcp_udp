import socket,time,traceback

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('lista del archivos del directorio server-file:')

#send data:
client.sendto(b'test', ('127.0.0.1',5003))
data, server = client.recvfrom(1024)

while True:
        
    #recivied the bytes from the server
    data, server = client.recvfrom(1024)

    #convert bytes to strig then print whitout format the string
    directory = str(repr(data))
    filename = directory[2:len(directory)-1]
    print(filename)    
    
#client.close()
        
    


        





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