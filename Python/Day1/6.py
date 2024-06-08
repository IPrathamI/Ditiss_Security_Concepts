#!/usr/bin/python3
import os, sys, subprocess
os.system(sys.argv[1])

a = os.system ("pwd")
print(a)


print("----------------------")
b = subprocess.call("ls",shell=True)
print(b)

print("---------------")

c = subprocess.getoutput("ls")
print(c)

