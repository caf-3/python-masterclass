import os

source = 'files/fileToMove.txt'
destination = "files/movedFiles/fileToMove.txt"

try:
    if os.path.exists(destination):
        print(f'{source} already exists inside {destination}')
    else:
        os.replace(source, destination)
except FileNotFoundError as e:
    print(e)
    print(f'{source} was not found')