from pathlib import Path



# -------------------- path_osx for mac os -------------------- #
home = str(Path.home())

def path_osx():
    return f"{home}/Desktop/Distributor"
     
def documents_osx():
    return f"{home}/Documents/"

def music_osx():
    return f"{home}/Music/"

def pictures_osx():
    return f"{home}/Pictures/"

def movies_osx():
    return f"{home}/Movies/"