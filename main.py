import sys
import socket


def main():
    
    try:
        
        if len(sys.argv) != 6:
            print("usage:", sys.argv[0], "<ip> <port> <type(-d, -u, -l)> <file_name> <protocol(udp or tcp)>")
            sys.exit(1)

        #print('Argument list: '+ str(sys.argv))

        #Funtion: arguments of cli file
        _program  = str(sys.argv[0])  # name of the program for default is main.py
        _ip       =  str(sys.argv[1]) # ip tha I want to connect 
        _port     = int(sys.argv[2])  # port than I want to connect 
        _type     = str(sys.argv[3])  # type of proccess than I want to do: -d(download a file), -u(upload a file) and -l(list of files)
        _file     = str(sys.argv[4])  # name of the file
        _protocol = str(sys.argv[5])  # name of the protocol than I want to use: UPD and TCP

        if  _protocol == 'udp':
            UDP()
        elif _protocol == 'tcp':
            TCP(_ip,_port,_type,_file)
        else:
            print('plase choise the protocol and try again')


    except:
        print('Sonthing was wrong with the arguments')
    
def UDP():
    print('UDP funtions')

def TCP(_ip, _port,_type,_file):
    
    if _type == '-d':
        dowloadTCP(_ip,_port, _file)

    elif _type == '-u':
        uploadTCP(_ip,_port, _file)
        
    elif _type == '-l':
        listTCP(_ip,_port, _file)


def uploadTCP(_ip,_port, _file):
    print('upload file')

def dowloadTCP(_ip,_port, _file):
    print('dowload file')

def listTCP(_ip,_port, _file):
    print('list file')

if __name__ == '__main__':
    main()


