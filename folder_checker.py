import os
import file_sorter
import environment

path = environment.path_osx()

# Method for check if the target folder is empty or not
def check():
    # check if the target folder is empty
    if len(os.listdir(path) ) == 0:
        pass
    else:    
        # If folder is contains other data sorter method will execute.
        file_sorter.sorter(path)