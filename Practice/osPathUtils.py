# read a file
from os import path
import os

# find the file path
#find if the file exists
if (path.exists("01_helloworld.py")):
    print("the file exists!")
else:
    print("could not find that file")
# file = open("01_helloworld.py","r")
# print(file.read())

# note: cannot find the file to hello world.py because its not in the current working directory.