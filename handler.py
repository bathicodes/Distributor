import platform
from folder_maker import *
from folder_checker import *

def handler():
    if platform.system() == "Darwin":
        create_folder_osx()
    check()

handler()