#!/usr/bin/python3

import socket, argparse

    #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = "192.168.43.89"

parser=argparse.ArgumentParser(description = "This Is a Port Scanner" )
parser.add_argument("-host",type=str,help="Provide command", required=True)
parser.add_argument("-p",type=int,help="Provide port", required=True)

a=parser.parse_args()
def run (port):
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((a.host, port))
        sock.timeout(8)
        sock.close()
        #print("Port {}.{} is open".format(host,port))
        return True
    except:
        return False
        
    #finally:
        

if run(a.p):
    print("Port {} is open".format(a.p))
else:
    print("Port {} is Closed".format(a.p))

