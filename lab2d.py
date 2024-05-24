#!/usr/bin/env python3

# Raein Nobakht
#OPS445

#Imports

import sys

#variables

name = str(sys.argv[1])
age = int(sys.argv[2])

#script
if len(sys.argv) != 3:
    print('Usage: ./lab2d.py name age')
    sys.exit()
else:
    print('Hi ' + str(sys.argv[1]) + ', you are ' + str(int(sys.argv[2])) + ' years old.')
