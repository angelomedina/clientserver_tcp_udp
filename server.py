import threading
import socket
import json
import os


def applist_tcp():
    
    #python main.py 127.0.0.1 5000 -l writeenyone tcp

    host = '127.0.0.1'
    port = 5000

    print('server -l listening tcp: '+ host +' '+str(port))

    # socket.AF_INET: means protocol IPv4
    # socket.SOCK_STREAM: used for TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host,port))
        s.listen()
        conn, addr = s.accept()
        print('connected by ',addr)
        #connection to send the file list in server-file directory
        print('enviando lista del archivos del directorio server-file:')
        for value in os.listdir('server-file'):
            data = str.encode(value)
            print(data)
            conn.send(data) 
    conn.close()


def appupload_tcp():

    #python main.py 127.0.0.1 5001 -u server.png tcp

    host = '127.0.0.1'
    port = 5001

    print('server -u listening tcp: '+ host +' '+str(port))

    # socket.AF_INET: means protocol IPv4
    # socket.SOCK_STREAM: used for TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host,port))
        s.listen()
        conn, addr = s.accept()

        #recived the file name
        value = conn.recv(1024)
        #convert this file to string the make a file path 
        filename = str(repr(value))
        name = filename[2:len(filename)-1]
        filepath = 'server-file/'+name
        
        #connetion to wite a file
        filetodown = open(filepath,'wb')

        print('connected by ',addr)
        while True:
            print('receiving...')
            data = conn.recv(1024)
            filetodown.write(data)

            if len(data) < 1024:
                print('done reciving')
                break
            
        filetodown.close()
        conn.send(str.encode('file saved in server-file'))
        conn.shutdown(2)
        conn.close()



def appdownload_tcp():

    #python main.py 127.0.0.1 5002 -d test2.js tcp
   
    host = '127.0.0.1'
    port = 5002

    print('server -d listening tcp: '+ host +' '+str(port))

    # socket.AF_INET: means protocol IPv4
    # socket.SOCK_STREAM: used for TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host,port))
        s.listen()
        conn, addr = s.accept()

        #connection to download a file
        print('connected by ',addr)
        data = conn.recv(1024)

        #convert the response to string; then concat the path and the filename(name)
        filename = str(repr(data))
        name = filename[2:len(filename)-1]
        filepath = 'server-file/'+name
        f = open(filepath, 'rb')
        value = f.read(1024)

        while (value):
            #esta linea no me esta enviando
            conn.send(value)
            print('sent file')
            value = f.read(1024)
        f.close()

    print('done sending')
    conn.close()
    
def applist_udp():
    
    port = 5003
    host = '127.0.0.1'

    print('server -l listening udp: '+ host +' '+str(port))

    # socket.AF_INET: means protocol IPv4
    # socket.SOCK_DGRAM: used for UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host,port))

        while True:

            # received data and addres of any connection
            data, address = s.recvfrom(1024)
            print(data) 
            print('connected by ',address)
                
            # connection to send the file list in server-file directory
            print('enviando lista del archivos del directorio server-file:')

            for value in os.listdir('server-file'):
                filename = str.encode(value)
                print(filename)
                s.sendto(filename, address)
    
    
    

if __name__=='__main__':
    t1 = threading.Thread(target = applist_tcp)
    t2 = threading.Thread(target = appupload_tcp)
    t3 = threading.Thread(target = appdownload_tcp)
    t4 = threading.Thread(target = applist_udp)

    t1.start()
    t2.start()
    t3.start()
    t4.start()



