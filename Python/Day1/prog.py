#!/usr/bin/python3

import argparse, subprocess as ss 

parser = argparse.ArgumentParser(description="This is a Resolver Tool")
parser.add_argument("-s", type=str, help="Provide Command", required=True)
parser.add_argument("-d", type=str, help="Provide Command", required=True)
a = parser.parse_args()
print(ss.getoutput("host -t a {}.{}".format(a.s,a.d)))
