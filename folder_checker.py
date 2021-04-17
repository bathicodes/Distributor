import os
from file_sorter import *
from environment import *

path = path()

# Method for check if the target folder is empty or not
def check():
    # check if the target folder is empty
    if len(os.listdir(path) ) == 0:
        pass
    else:    
        # If folder is contains other data sorter method will execute.
        sorter(path)