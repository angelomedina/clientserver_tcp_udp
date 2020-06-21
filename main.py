import sys
import socket
import os

#commint: configure with Jenkins

def main():
    
    try:
        
        #Funtion: arguments of cli file
        _program  = str(sys.argv[0])  # name of the program for default is main.py
        _ip       =  str(sys.argv[1]) # ip tha I want to connect 
        _port     = int(sys.argv[2])  # port than I want to connect 
        _type     = str(sys.argv[3])  # type of proccess than I want to do: -d(download a file), -u(upload a file) and -l(list of files)
        _file     = str(sys.argv[4])  # name of the file
        _protocol = str(sys.argv[5])  # name of the protocol than I want to use: UPD and TCP

        if  _protocol == 'udp':
            UDP(_ip,_port,_type,_file)
        elif _protocol == 'tcp':
            TCP(_ip,_port,_type,_file)
        else:
            print('plase choise the protocol and try again')

    except:

        if len(sys.argv) != 6:
            print('Oops usage:', sys.argv[0], "<ip> <port> <type(-d, -u, -l)> <file_path/file_name> <protocol(udp or tcp)>")
            sys.exit(1)
    
def UDP(_ip, _port,_type,_file):

    if _type == '-l':
        listUDP(_ip,_port)
    
    if _type == '-u':
        uploadUDP(_ip,_port,_file)

    if _type == '-d':
        dowloadUDP(_ip,_port,_file)
    
def TCP(_ip, _port,_type,_file):
    
    if _type == '-d':
        dowloadTCP(_ip,_port, _file)

    if _type == '-u':
        uploadTCP(_ip,_port, _file)
        
    if _type == '-l':
        listTCP(_ip,_port)


def uploadTCP(_ip,_port, _file):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((_ip, _port))
   
    #sending file name to save this udload file with the same name
    filename = str.encode(_file, 'utf-8')
    server.send(filename)

    try:
        filetosend = open(os.path.join('client-file/',_file),'rb')

    except (OSError, IOError) as e:
        print(e)
    
    data = filetosend.read(1024)

    while data:
        print('uploading file')
        server.send(data)
        data = filetosend.read(1024)
    
    filetosend.close()
    print('done sending...')
    print(server.recv(1024))
    server.shutdown(2)
    server.close()


def dowloadTCP(_ip,_port, _file):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((_ip, _port))

    #convert the _file a b'text' that why I need to send a format without b''
    filename = str.encode(_file, 'utf-8')
    server.send(filename)

    #save the file in this directory
    with open(os.path.join('client-file/',_file),'wb') as f:

        while True:
            print('file openend')
            data = server.recv(1024)

            if not data:
                break
            f.write(data)
            print('file saved in: client-file/your-file-name')

    f.write()
    socket.close()


def listTCP(_ip,_port):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((_ip, _port))

    print('lista del archivos del directorio server-file:')
    while True:

        #recivied the bytes from the server
        data = server.recv(1024)

        #convert bytes to strig then print whitout format the string
        directory = str(repr(data))
        filename = directory[2:len(directory)-1]
        print(filename)
        
        if not data:
            break

    server.close()

def listUDP(_ip, _port):

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print('lista del archivos del directorio server-file:')

    #send data to establish the connection
    client.sendto(b'', (_ip,_port))

    while True:

        #recivied the bytes from the server
        data,_server = client.recvfrom(1024)

        #convert bytes to strig then print whitout format the string
        directory = str(repr(data))
        filename = directory[2:len(directory)-1]
        print(filename)
    
    client.close()

def dowloadUDP(_ip,_port, _file):

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #convert the _file a b'text' that why I need to send a format with b''
    filename = str.encode(_file, 'utf-8')
    client.sendto(filename, (_ip, _port))

    #save the file in this directory
    with open(os.path.join('client-file/',_file),'wb') as f:

        while True:

            data, _server = client.recvfrom(1024)

            if not data:
                break
            f.write(data)
            print('file saved in: client-file/your-file-name')

    f.write()
    socket.close()

def uploadUDP(_ip,_port,_file):
    
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #sending file name to save this udload file with the same name
    filename = str.encode('client.png', 'utf-8')
    client.sendto(filename,(_ip,_port))

    try:
        filetosend = open(os.path.join('client-file/','client.png'),'rb')

    except (OSError, IOError) as e:
        print(e)

    data = filetosend.read(1024)
    
    while (data):
        print('uploading file')
        client.sendto(data, ('127.0.0.1',5004))
        data = filetosend.read(1024)

    filetosend.close()
    print('done sending...')
    client.shutdown(2)
    client.close()




if __name__ == '__main__':
    main()


