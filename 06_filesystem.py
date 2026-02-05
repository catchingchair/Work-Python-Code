# using the filesystem

import os
from os import path
import shutil
from zipfile import ZipFile

# make a duplicate of an existing file
if path.exists("newfile.txt"):
    # get the path to the file in the current directory
    src = path.realpath("newfile.txt")
    print(src)

    # make a backup copy by appending "bak" to the name
    dst = src + ".bak"

    # now use the shell to make a copy of the file
    shutil.copy(src,dst) #.copy2 copies the metadata along with the rest of the file.

    # rename the original file
    # os.rename("textfile.txt", "newfile.txt")

    # now put things into a ZIP archive
    # root_dir, tail = path.split(src)
    # shutil.make_archive("archive", "zip", root_dir)
    
    # more fine-grained control over ZIP files
    with ZipFile("testzip.zip", "w") as newzip:
        newzip.write("newfile.txt")
        newzip.write("textfile.txt.bak")
