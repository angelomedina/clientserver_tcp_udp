import sys
import socket


def main():
    
    try:
        
        print('Argument list: '+ str(sys.argv))

        #Funtion: arguments of cli file
        _program  = str(sys.argv[0])  # name of the program for default is client.py
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
    
    print('TCP funtions')

    # open the connection 
    server = socket.socket()
    server.connect((_ip, _port))    

    #while True:
        #print('connected')

    server.close()
    print('connection closed')

if __name__ == '__main__':
    main()


