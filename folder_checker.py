import os
from file_sorter import *

path = r'/Users/bathiyaseneviratne/Desktop/Distributor'

def check():
    if len(os.listdir(path) ) == 0:
        print("Directory is empty") # remove later
        pass
    else:    
        print("Directory is not empty")
        sorter(path)