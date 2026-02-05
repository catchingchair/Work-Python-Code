import os
from os import path
from datetime import datetime
import time

# print the name of the OS (operating system)
print(os.name)
filename = "textfile.txt"
# Check for item existence and type
print(f"Item exists: {path.exists(filename)}")
print(f"Item is a file: {path.isfile(filename)}")
print(f"Item is a directory: {path.isdir(filename)}")

# Work with file paths
print(f"Item's path: {path.realpath(filename)}")
print(f"Item's path and name: {path.split(path.realpath(filename))}")
# Get the modification time
t = time.ctime(path.getmtime(filename))
print(t)
print(datetime.fromtimestamp(path.getmtime(filename)))

# Calculate how long ago the item was modified
td = datetime.now() - datetime.fromtimestamp(path.getmtime(filename))
print(f"it has been {td} since thefile was modified")
print(f"or, {td.total_seconds()} seconds")