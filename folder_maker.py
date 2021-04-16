import os

def create_folder():
    if not os.path.exists('my_folder'):
        os.makedirs('my_folder')