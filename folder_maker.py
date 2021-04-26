import os
import platform
from environment import *

path_osx = path_osx()

# create a folder on the desktop
# If folder is already exists just pass

def create_folder():

    # macOS folder creating
    if platform.system() == "Darwin":
        if not os.path.exists(path_osx):
            os.makedirs(path_osx)
    else:
        pass