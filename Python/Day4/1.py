#!/usr/bin/python3
import socket

file = input ("Enter Filename: ")
f = open(file, "r")
for i in f:
    print(i.strip(),":",socket.gethostbyname(i.strip()))
