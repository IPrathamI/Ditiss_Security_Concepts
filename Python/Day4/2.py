#!/usr/bin/python3

import socket

    #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.43.89"

def run (port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        sock.close()
        return True
    except:
        return False
        
    #finally:
        

for i in range(21,28):
    if run(i):
        print("Port {} is open".format(i))
    else:
        print("Port {} is Closed".format(i))
