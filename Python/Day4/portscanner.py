#!/usr/bin/python3

import socket, argparse


parser=argparse.ArgumentParser(description = "This Is a Port Scanner" )
parser.add_argument("-host",type=str,help="Provide command", required=True)
parser.add_argument("-p",type=str,help="Provide port", required=True)

a=parser.parse_args()
def run (port):
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((a.host, port))
        #sock.timeout(8)
        sock.close()
        #print("Port {}.{} is open".format(host,port))
        return True
    except:
        return False
       
def fun1():
    for i in range(int(port1[0]),int(port1[1])+1):
        if run(int(i)):
            print("port {} is running".format(i))
        else:
            print("port {} is closed".format(i))

def fun2():
    for i in port1:
        if run(int(i)):
            print("open", ":  ",i)
        else:
            print("closed", ": ",i)


if "-" in a.p:
    port1 = a.p.split('-')
    fun1()
elif "," in a.p:
    port1 = a.p.split(',')
    fun2()
else:
    port1 = a.p.split(',')
    fun1()
