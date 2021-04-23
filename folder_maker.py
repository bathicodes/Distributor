import os
from environment import *

path = path()

# create a folder on the desktop
# If folder is already exists just pass
def create_folder_osx():
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass