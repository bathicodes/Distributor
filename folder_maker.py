import os

path = r'/Users/bathiyaseneviratne/Desktop/Distributor'

def create_folder():
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass