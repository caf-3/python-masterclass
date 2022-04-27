import os

path = "/home/tomasc/Projects/python-masterclass/files/fileDetection.py"

if os.path.exists(path):
    print("This path exists")
    if os.path.isfile(path):
        print("The path is pointing to a file")
    elif os.path.isdir(path):
        print("The path is pointing to a directory")
else:
    print("This path doesn't exists")