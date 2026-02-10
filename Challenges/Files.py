# files challenge
import os
from os import path
from pathlib import Path
def file_info():
    totalbytes = 0
    folder = "deps"
    # get a list of all the files in the current directory
    dirlist = os.listdir(folder)
    for file in dirlist:
        # make sure its a file
        if os.path.isfile(folder + "/" + file) and file.endswith(".txt"):
            filesize = os.path.getsize(folder + "/" + file)
            totalbytes += filesize
    return totalbytes
        

