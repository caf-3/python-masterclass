import os
import shutil

# path = "files/deleteme"
# path = "files/empty_folder"
path = "files/folder"

try:
    # os.remove(path)
    # os.rmdir(path)
    shutil.rmtree(path)
except FileNotFoundError:
    print(path+" not found")
except IsADirectoryError:
    print("use another function to delete a directory")
except OSError:
    print("use another function to delete a non empty directory")
else:
    print(path+" was deleted!")