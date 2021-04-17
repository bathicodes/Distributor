import os

path = r'/Users/bathiyaseneviratne/Desktop/Distributor'

# create a folder on the desktop
# If folder is already exists just pass
def create_folder():
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass