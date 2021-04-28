import platform
import folder_maker
import folder_checker

def handler():  
    folder_maker.create_folder()
    folder_checker.check()

handler()