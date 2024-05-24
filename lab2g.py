#!/usr/bin/env python3

# Author: Raein Nobakht
# AuthorID: 103021226
#Date Created: 2024/05/24

#Imports
import sys

#Variables/Inputs

if len(sys.argv) != 2:
    timer = 3
else:
    timer = int(sys.argv[1])


#Script
while timer != 0:
    print(timer)
    timer = (timer - 1)
print("blast off!")