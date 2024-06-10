#!/usr/bin/python3

import sys, re

for i in sys.stdin.readlines():
    collect = re.findall("\W",i)
    if collect:
        print(collect)
