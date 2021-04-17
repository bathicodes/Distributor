import os
from file_sorter import *

path = r'/Users/bathiyaseneviratne/Desktop/Distributor'

def check():
    if len(os.listdir(path) ) == 0:
        pass
    else:    
        sorter(path)