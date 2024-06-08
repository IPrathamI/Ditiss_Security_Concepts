#!/usr/bin/python3
import os, sys, subprocess

a=sys.argv[1]
if a== "-c":
    if sys.argv[2]:
        print(subprocess.getoutput(sys.argv[2]))
      
elif a== "-h":
    print ("-c cmd: Enter a command, ")
else:
    print ("Invalid argument")
    



